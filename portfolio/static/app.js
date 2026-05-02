const fmt = (n) => n == null ? '—' : Number(n).toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const fmtShares = (n) => Number(n).toLocaleString(undefined, { minimumFractionDigits: 0, maximumFractionDigits: 6 });

// ── Portfolio ──────────────────────────────────────────────────────────────

async function refreshPortfolio() {
  const btn = document.getElementById('btn-refresh');
  btn.disabled = true;
  btn.textContent = 'Loading…';
  try {
    const res = await fetch('/api/portfolio');
    const data = await res.json();
    renderSummary(data.summary);
    renderPositions(data.positions);
  } catch (e) {
    console.error(e);
  } finally {
    btn.disabled = false;
    btn.innerHTML = '&#8635; Refresh prices';
  }
}

function renderSummary(s) {
  document.getElementById('s-value').textContent = '$' + fmt(s.total_value);
  document.getElementById('s-cost').textContent = '$' + fmt(s.total_cost);
  document.getElementById('s-gain').textContent = (s.total_gain >= 0 ? '+$' : '-$') + fmt(Math.abs(s.total_gain));
  document.getElementById('s-gain-pct').textContent = (s.total_gain_pct >= 0 ? '+' : '') + fmt(s.total_gain_pct) + '%';
  document.getElementById('s-div').textContent = '$' + fmt(s.total_dividends);

  const card = document.getElementById('card-gain');
  card.classList.remove('gain-pos', 'gain-neg');
  card.classList.add(s.total_gain >= 0 ? 'gain-pos' : 'gain-neg');
}

function renderPositions(positions) {
  const tbody = document.getElementById('positions-body');
  if (!positions.length) {
    tbody.innerHTML = '<tr><td colspan="8" style="color:#64748b;text-align:center;padding:1rem">No positions yet</td></tr>';
    return;
  }
  tbody.innerHTML = positions.map(p => `
    <tr>
      <td><strong>${p.ticker}</strong></td>
      <td>${fmtShares(p.shares)}</td>
      <td>$${fmt(p.avg_cost)}</td>
      <td>$${fmt(p.live_price)}</td>
      <td>$${fmt(p.market_value)}</td>
      <td class="${p.gain >= 0 ? 'pos' : 'neg'}">${p.gain >= 0 ? '+' : ''}$${fmt(Math.abs(p.gain))}</td>
      <td class="${p.gain_pct >= 0 ? 'pos' : 'neg'}">${p.gain_pct >= 0 ? '+' : ''}${fmt(p.gain_pct)}%</td>
      <td>$${fmt(p.dividends_received)}</td>
    </tr>
  `).join('');
}

// ── Transactions ───────────────────────────────────────────────────────────

async function loadTransactions() {
  const res = await fetch('/api/transactions');
  const rows = await res.json();
  const tbody = document.getElementById('tx-body');
  if (!rows.length) {
    tbody.innerHTML = '<tr><td colspan="9" style="color:#64748b;text-align:center;padding:1rem">No transactions yet</td></tr>';
    return;
  }
  tbody.innerHTML = rows.map(r => `
    <tr>
      <td>${r.date}</td>
      <td><strong>${r.ticker}</strong></td>
      <td><span class="badge-${r.type}">${r.type.toUpperCase()}</span></td>
      <td>${fmtShares(r.shares)}</td>
      <td>$${fmt(r.price)}</td>
      <td>$${fmt(r.fees)}</td>
      <td>$${fmt(r.shares * r.price + r.fees)}</td>
      <td>${r.notes || ''}</td>
      <td><button class="danger" onclick="deleteTx(${r.id})">✕</button></td>
    </tr>
  `).join('');
}

async function submitTransaction(e) {
  e.preventDefault();
  const form = e.target;
  const fd = new FormData(form);
  const payload = Object.fromEntries(fd.entries());
  payload.ticker = payload.ticker.toUpperCase();

  const res = await fetch('/api/transactions', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) { alert('Error: ' + (await res.text())); return; }
  form.reset();
  await loadTransactions();
  await refreshPortfolio();
}

async function deleteTx(id) {
  if (!confirm('Delete this transaction?')) return;
  await fetch('/api/transactions/' + id, { method: 'DELETE' });
  await loadTransactions();
  await refreshPortfolio();
}

// ── Dividends ──────────────────────────────────────────────────────────────

async function loadDividends() {
  const res = await fetch('/api/dividends');
  const rows = await res.json();
  const tbody = document.getElementById('div-body');
  if (!rows.length) {
    tbody.innerHTML = '<tr><td colspan="5" style="color:#64748b;text-align:center;padding:1rem">No dividends yet</td></tr>';
    return;
  }
  tbody.innerHTML = rows.map(r => `
    <tr>
      <td>${r.date}</td>
      <td><strong>${r.ticker}</strong></td>
      <td>$${fmt(r.amount)}</td>
      <td>${r.notes || ''}</td>
      <td><button class="danger" onclick="deleteDiv(${r.id})">✕</button></td>
    </tr>
  `).join('');
}

async function submitDividend(e) {
  e.preventDefault();
  const form = e.target;
  const fd = new FormData(form);
  const payload = Object.fromEntries(fd.entries());
  payload.ticker = payload.ticker.toUpperCase();

  const res = await fetch('/api/dividends', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) { alert('Error: ' + (await res.text())); return; }
  form.reset();
  await loadDividends();
  await refreshPortfolio();
}

async function deleteDiv(id) {
  if (!confirm('Delete this dividend?')) return;
  await fetch('/api/dividends/' + id, { method: 'DELETE' });
  await loadDividends();
  await refreshPortfolio();
}

// ── Init ───────────────────────────────────────────────────────────────────

(async () => {
  // set today's date as default in date fields
  const today = new Date().toISOString().slice(0, 10);
  document.querySelectorAll('input[type="date"]').forEach(el => el.value = today);

  await Promise.all([refreshPortfolio(), loadTransactions(), loadDividends()]);
})();
