const showelement = new IntersectionObserver((entries) => {
   entries.forEach((entry) => {
      if (entry.isIntersecting){
         entry.target.classList.add('show-animation');
      }
   });
});
const hiddenElements = document.querySelectorAll('.hidden-animation');
hiddenElements.forEach((el) => showelement.observe(el));