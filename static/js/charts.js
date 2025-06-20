function formatData(entries) {
  const labels = entries.map(e => e.date);
  const amounts = entries.map(e => e.amount);
  return { labels, amounts };
}

document.addEventListener('DOMContentLoaded', () => {
  const income = formatData(incomeData);
  const expense = formatData(expenseData);
  new Chart(document.getElementById('incomeExpenseChart'), {
    type: 'line',
    data: {
      labels: income.labels,
      datasets: [
        { label: 'Income', data: income.amounts, borderColor: 'green', fill: false },
        { label: 'Expenses', data: expense.amounts, borderColor: 'red', fill: false }
      ]
    }
  });

  const debt = formatData(debtData);
  new Chart(document.getElementById('debtChart'), {
    type: 'line',
    data: {
      labels: debt.labels,
      datasets: [{ label: 'Debt', data: debt.amounts, borderColor: 'blue', fill: false }]
    }
  });
});
