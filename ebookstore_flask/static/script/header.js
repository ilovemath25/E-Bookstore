function undisplay_left_menu(){
   document.querySelector(".navbar-side-space").style.display = "none";
   document.querySelector(".navbar-side-category").style.animation = "hidemenu 0.5s";
   document.querySelector(".navbar-side-category").addEventListener('animationend',() => {
      document.querySelector(".navbar-side-mobile").style.display = "none";
   })
   // document.querySelector("*").style.overflow = "";
}
function display_left_menu(){
   document.querySelector(".navbar-side-mobile").style.display = "block";
   document.querySelector(".navbar-side-space").style.display = "block";
   document.querySelector(".navbar-side-category").style.animation = "showmenu 0.5s";
   document.querySelector(".navbar-side-category").addEventListener('animationend',() => {
      document.querySelector(".navbar-side-mobile").style.display = "block";
   })
   // document.querySelector("*").style.overflow = "hidden";
}