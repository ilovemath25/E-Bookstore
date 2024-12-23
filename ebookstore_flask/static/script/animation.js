function show_up_animation(){
   document.querySelector(".show-up-animation").style.animation = "showup 1s forwards"
}
function fill_up_animation(){
   document.querySelector(".fill-up-animation").style.animation = "fillup 0.7s forwards"
}
function reset_fill_up_animation() {
   const element = document.querySelector(".fill-up-animation");
   if (element) {
      element.style.animation = "none";
      element.style.height = "0%";
   }
}
const links = document.querySelectorAll("a");
links.forEach(link => {
   link.addEventListener("click", event => {
      const href = link.getAttribute("href");
      if (href && href.startsWith("#")) return;
      event.preventDefault();
      fill_up_animation();
      setTimeout(() => {
         window.location.href = link.href;
      }, 700);
   });
});
const showelement = new IntersectionObserver((entries) => {
   entries.forEach((entry) => {
      if (entry.isIntersecting){
         entry.target.classList.add('show-animation');
      }
   });
});
document.addEventListener("DOMContentLoaded", show_up_animation);
window.addEventListener("pageshow", reset_fill_up_animation);
const hiddenElements = document.querySelectorAll('.hidden-animation');
hiddenElements.forEach((el) => showelement.observe(el));