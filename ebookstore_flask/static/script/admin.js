const selected = document.getElementById('selected-gender');
const selectedHidden = document.getElementById('selected-gender-hidden');
const optionsContainer = document.querySelector('.dropdown-options');
const options = document.querySelectorAll('.dropdown-option');

selected.addEventListener('click', () => {
   optionsContainer.style.display = "block";
});
options.forEach(option => {
   option.addEventListener('click', () => {
      selected.value = option.textContent;
      selectedHidden.value = option.textContent;
      optionsContainer.style.display = "none";
   });
});
document.addEventListener('click', (e) => {
   if (!selected.contains(e.target) && !optionsContainer.contains(e.target)) {
      optionsContainer.style.display = "none";
   }
});
document.querySelector('.delete-user').addEventListener('click', () => {
   document.querySelector(".delete-user-container").classList.remove('modal-hidden');
});
document.getElementById('cancel-delete').addEventListener('click', () => {
   document.querySelector(".delete-user-container").classList.add('modal-hidden');
});