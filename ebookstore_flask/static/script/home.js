function Slider(containerSelector) {
   document.querySelectorAll(containerSelector).forEach(slider => {
      const bookWidth = slider.children[0].offsetWidth;
      slider.parentElement.querySelector('.left-arrow').addEventListener('click', () => {
         slider.scrollBy({
            left: -bookWidth,
            behavior: 'smooth'
         });
      });
      slider.parentElement.querySelector('.right-arrow').addEventListener('click', () => {
         slider.scrollBy({
            left: bookWidth,
            behavior: 'smooth'
         });
      });
   });
}
Slider('.book-slider');
Slider('.promotion-slider');