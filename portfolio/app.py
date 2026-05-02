from flask import Flask, jsonify, request, render_template, abort
from db import get_conn, init_db
import yfinance as yf
from collections import defaultdict

app = Flask(__name__)


# ---------------------------------------------------------------------------
# Portfolio calculation helpers
# ---------------------------------------------------------------------------

def _compute_positions(rows):
    """Return {ticker: {shares, cost_basis, avg_cost}} from transaction rows."""
    positions = defaultdict(lambda: {"shares": 0.0, "total_cost": 0.0})
    for r in rows:
        t = r["ticker"].upper()
        if r["type"] == "buy":
            positions[t]["total_cost"] += r["shares"] * r["price"] + r["fees"]
            positions[t]["shares"] += r["shares"]
        else:  # sell
            if positions[t]["shares"] > 0:
                avg = positions[t]["total_cost"] / positions[t]["shares"]
                positions[t]["total_cost"] -= avg * r["shares"]
            positions[t]["shares"] -= r["shares"]
            positions[t]["total_cost"] = max(0.0, positions[t]["total_cost"])
    # drop zero/negative positions
    return {
        t: {
            "shares": v["shares"],
            "avg_cost": v["total_cost"] / v["shares"] if v["shares"] > 0 else 0,
            "total_cost": v["total_cost"],
        }
        for t, v in positions.items()
        if v["shares"] > 0.0001
    }


def _fetch_prices(tickers):
    """Return {ticker: current_price} using yfinance fast_info."""
    prices = {}
    for ticker in tickers:
        try:
            info = yf.Ticker(ticker).fast_info
            prices[ticker] = info.last_price or info.previous_close or 0.0
        except Exception:
            prices[ticker] = 0.0
    return prices


# ---------------------------------------------------------------------------
# Routes – UI
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------------------------------------------
# Routes – Transactions
# ---------------------------------------------------------------------------

@app.route("/api/transactions", methods=["GET"])
def list_transactions():
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM transactions ORDER BY date DESC, id DESC"
        ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/transactions", methods=["POST"])
def add_transaction():
    data = request.get_json(force=True)
    required = ("ticker", "type", "shares", "price", "date")
    if not all(k in data for k in required):
        abort(400, "Missing required fields: ticker, type, shares, price, date")
    if data["type"] not in ("buy", "sell"):
        abort(400, "type must be 'buy' or 'sell'")
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO transactions (ticker, type, shares, price, date, fees, notes) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                data["ticker"].upper(),
                data["type"],
                float(data["shares"]),
                float(data["price"]),
                data["date"],
                float(data.get("fees", 0)),
                data.get("notes", ""),
            ),
        )
        row_id = cur.lastrowid
    return jsonify({"id": row_id}), 201


@app.route("/api/transactions/<int:tx_id>", methods=["DELETE"])
def delete_transaction(tx_id):
    with get_conn() as conn:
        conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
    return "", 204


# ---------------------------------------------------------------------------
# Routes – Dividends
# ---------------------------------------------------------------------------

@app.route("/api/dividends", methods=["GET"])
def list_dividends():
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT * FROM dividends ORDER BY date DESC, id DESC"
        ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.route("/api/dividends", methods=["POST"])
def add_dividend():
    data = request.get_json(force=True)
    required = ("ticker", "amount", "date")
    if not all(k in data for k in required):
        abort(400, "Missing required fields: ticker, amount, date")
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO dividends (ticker, amount, date, notes) VALUES (?, ?, ?, ?)",
            (
                data["ticker"].upper(),
                float(data["amount"]),
                data["date"],
                data.get("notes", ""),
            ),
        )
        row_id = cur.lastrowid
    return jsonify({"id": row_id}), 201


@app.route("/api/dividends/<int:div_id>", methods=["DELETE"])
def delete_dividend(div_id):
    with get_conn() as conn:
        conn.execute("DELETE FROM dividends WHERE id = ?", (div_id,))
    return "", 204


# ---------------------------------------------------------------------------
# Routes – Portfolio summary (live prices)
# ---------------------------------------------------------------------------

@app.route("/api/portfolio")
def portfolio():
    with get_conn() as conn:
        tx_rows = conn.execute("SELECT * FROM transactions").fetchall()
        div_rows = conn.execute("SELECT * FROM dividends").fetchall()

    positions = _compute_positions(tx_rows)

    # dividends per ticker
    dividends_by_ticker = defaultdict(float)
    total_dividends = 0.0
    for r in div_rows:
        dividends_by_ticker[r["ticker"].upper()] += r["amount"]
        total_dividends += r["amount"]

    live_prices = _fetch_prices(list(positions.keys()))

    items = []
    total_cost = 0.0
    total_value = 0.0
    for ticker, pos in positions.items():
        price = live_prices.get(ticker, 0.0)
        market_value = pos["shares"] * price
        gain = market_value - pos["total_cost"]
        gain_pct = (gain / pos["total_cost"] * 100) if pos["total_cost"] else 0.0
        items.append({
            "ticker": ticker,
            "shares": round(pos["shares"], 6),
            "avg_cost": round(pos["avg_cost"], 4),
            "total_cost": round(pos["total_cost"], 2),
            "live_price": round(price, 4),
            "market_value": round(market_value, 2),
            "gain": round(gain, 2),
            "gain_pct": round(gain_pct, 2),
            "dividends_received": round(dividends_by_ticker.get(ticker, 0.0), 2),
        })
    items.sort(key=lambda x: x["market_value"], reverse=True)

    total_cost = sum(i["total_cost"] for i in items)
    total_value = sum(i["market_value"] for i in items)
    total_gain = total_value - total_cost

    return jsonify({
        "positions": items,
        "summary": {
            "total_cost": round(total_cost, 2),
            "total_value": round(total_value, 2),
            "total_gain": round(total_gain, 2),
            "total_gain_pct": round((total_gain / total_cost * 100) if total_cost else 0, 2),
            "total_dividends": round(total_dividends, 2),
        },
    })


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5050)
