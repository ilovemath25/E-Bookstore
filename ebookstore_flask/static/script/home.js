document.querySelectorAll('.book-slider').forEach(slider => {
   slider.parentElement.querySelector('.left-arrow').addEventListener('click', () => {
      slider.scrollBy({
         left: -200,
         behavior: 'smooth'
      });
   });
   slider.parentElement.querySelector('.right-arrow').addEventListener('click', () => {
      slider.scrollBy({
         left: 200,
         behavior: 'smooth'
      });
   });
});
