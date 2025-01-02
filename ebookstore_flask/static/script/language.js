function translateInputPlaceholder(input) {
   if (!input) return
   const text = input.placeholder.trim();
   if (input && translateDataSets[text]) {
      input.placeholder = translateDataSets[text];
   }
}
function translateInputValue(input) {
   if (!input) return
   const text = input.value.trim();
   if (input && translateDataSets[text]) {
      input.value = translateDataSets[text];
   }
}
function applyTranslations() {
   const elementsToTranslate = document.querySelectorAll('.translate');
   elementsToTranslate.forEach(element => {
      const text = element.textContent.trim();
      if (translateDataSets[text]) {
         element.textContent = translateDataSets[text];
      }
      if (element.tagName === 'INPUT') {
         translateInputValue(element);
         translateInputPlaceholder(element);
      }
   });
}

document.addEventListener('DOMContentLoaded', () => {
   const storedLanguage = localStorage.getItem('selectedLanguage') || 'en';
   if (storedLanguage !== 'en') applyTranslations();
   const languageButton = document.querySelector('.language');
   if (languageButton) {
      languageButton.addEventListener('click', () => {
         const dropdown = document.querySelector('.language-dropdown');
         dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
      });
   }
   const languageOptions = document.querySelectorAll('.language-dropdown a');
   languageOptions.forEach(option => {
      option.addEventListener('click', (event) => {
         const selectedLanguage = event.target.getAttribute('data-lang');
         localStorage.setItem('selectedLanguage', selectedLanguage);
         location.reload();
      });
   });
});