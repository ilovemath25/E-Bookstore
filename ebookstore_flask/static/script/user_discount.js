function showDiscounts(type) {
   document.querySelectorAll('.discount-list').forEach(list => list.style.display = 'none');
   document.getElementById(type).style.display = 'block';
   document.querySelectorAll('.header-title').forEach(title => title.classList.remove('checked'));
   document.querySelector(`.header-title[onclick="showDiscounts('${type}')"]`).classList.add('checked');
}