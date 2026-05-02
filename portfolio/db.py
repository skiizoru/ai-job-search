import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "portfolio.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS transactions (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker    TEXT    NOT NULL,
                type      TEXT    NOT NULL CHECK(type IN ('buy','sell')),
                shares    REAL    NOT NULL CHECK(shares > 0),
                price     REAL    NOT NULL CHECK(price > 0),
                date      TEXT    NOT NULL,
                fees      REAL    NOT NULL DEFAULT 0,
                notes     TEXT
            );

            CREATE TABLE IF NOT EXISTS dividends (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                ticker    TEXT    NOT NULL,
                amount    REAL    NOT NULL CHECK(amount > 0),
                date      TEXT    NOT NULL,
                notes     TEXT
            );
        """)
