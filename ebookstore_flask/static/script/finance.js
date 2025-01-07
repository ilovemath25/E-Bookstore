document.getElementById('year1').addEventListener('click', function() {
   if (document.getElementById('dropdownOptions').style.display === 'block') document.getElementById('dropdownOptions').style.display = 'none';
   else document.getElementById('dropdownOptions').style.display = 'block';
});
function selectYear(year) {
   document.getElementById('selectedYear').innerText = year + ' ';
   if (year) window.location.href = '/admin/finance/' + year;
}
const ctx = document.getElementById('financialChart').getContext('2d');
const financialChart = new Chart(ctx, {
   type: 'line',
   data: {
      labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
      datasets: [
         {
            label: 'Total Revenue',
            data: monthlyRevenue,
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2,
            fill: false
         },
         {
            label: 'Total Expenses',
            data: monthlyExpenses,
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 2,
            fill: false
         },
         {
            label: 'Net Profit',
            data: monthlyProfit,
            borderColor: 'rgba(75, 192, 75, 1)',
            borderWidth: 2,
            fill: false
         }
      ]
   },
   options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
         x: {
            beginAtZero: true
         },
         y: {
            beginAtZero: true
         }
      }
   }
});