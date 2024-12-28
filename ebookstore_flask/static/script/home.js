function Slider(containerSelector, autoScrollInterval) {
   document.querySelectorAll(containerSelector).forEach(slider => {
      let slideWidth = slider.children[0].offsetWidth;
      const parent = slider.parentElement;
      const indicatorContainer = parent.querySelector('.slider-indicators');
      const indicators = indicatorContainer ? indicatorContainer.querySelectorAll('input') : null;
      slider.offsetWidth;
      slideWidth = slider.children[0].offsetWidth;
      const updateIndicators = () => {
         if (!indicators) return;
         slider.offsetWidth;
         slideWidth = slider.children[0].offsetWidth;
         const currentIndex = Math.round(slider.scrollLeft / slideWidth);
         indicators.forEach((indicator, index) => {
            indicator.checked = index === currentIndex;
         });
      };
      const scrollNext = () => {
         slider.offsetWidth;
         slideWidth = slider.children[0].offsetWidth;
         const maxScrollLeft = slider.scrollWidth - slider.offsetWidth;
         if (slider.scrollLeft + slideWidth - 5 > maxScrollLeft) {
            slider.scrollTo({ left: 0, behavior: 'smooth' });
         }
          else {
            slider.scrollBy({ left: slideWidth, behavior: 'smooth' });
         }
      };
      parent.querySelector('.left-arrow')?.addEventListener('click', () => {
         slider.scrollBy({
            left: -slider.children[0].offsetWidth,
            behavior: 'smooth',
         });
      });
      parent.querySelector('.right-arrow')?.addEventListener('click', () => {
         slider.scrollBy({
            left: slider.children[0].offsetWidth,
            behavior: 'smooth',
         });
      });
      slider.addEventListener('scroll', () => {
         updateIndicators();
      });
      window.addEventListener('resize', () => {
         slider.offsetWidth;
         slideWidth = slider.children[0].offsetWidth;
         updateIndicators();
      });
      if (autoScrollInterval) {
         setInterval(scrollNext, autoScrollInterval);
      }
   });
}
function Indicators(containerSelector) {
   document.querySelectorAll(containerSelector).forEach(indicatorContainer => {
      const slider = indicatorContainer.parentElement.querySelector('.promotion-slider');
      const indicators = indicatorContainer.querySelectorAll('input');
      slider.offsetWidth;
      slideWidth = slider.children[0].offsetWidth;

      indicators.forEach((indicator, index) => {
         indicator.addEventListener('click', () => {
            slider.offsetWidth;
            slideWidth = slider.children[0].offsetWidth;
            slider.scrollTo({ left: slideWidth * index, behavior: 'smooth'});
         });
      });
      window.addEventListener('resize', () => {
         slider.offsetWidth;
         slideWidth = slider.children[0].offsetWidth;
      });
   });
}
document.addEventListener("DOMContentLoaded", () => {
   Slider('.book-slider', 0);
   Slider('.promotion-slider', 4000);
   Indicators('.promotion .slider-indicators');
});
