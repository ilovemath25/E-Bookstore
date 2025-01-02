function undisplay_left_menu(){
   document.querySelector(".navbar-side-space").style.display = "none";
   document.querySelector(".navbar-side-category").style.animation = "hidemenu 0.5s";
   document.querySelector(".navbar-side-category").addEventListener('animationend',() => {
      document.querySelector(".navbar-side-mobile").style.display = "none";
   })
   document.querySelector("*").style.overflow = "";
}
function display_left_menu(){
   document.querySelector(".navbar-side-mobile").style.display = "block";
   document.querySelector(".navbar-side-space").style.display = "block";
   document.querySelector(".navbar-side-category").style.animation = "showmenu 0.5s";
   document.querySelector(".navbar-side-category").addEventListener('animationend',() => {
      document.querySelector(".navbar-side-mobile").style.display = "block";
   })
   document.querySelector("*").style.overflow = "hidden";
}
const searchInput = document.querySelector(".search-input");
const suggestions = document.querySelector(".suggestions");
searchInput.addEventListener("input", () => {
   const query = searchInput.value.toLowerCase();
   suggestions.innerHTML = "";
   if (query) {
      suggestions.style.display = "block";
      const matches = dataset.filter(item => item.toLowerCase().includes(query));
      matches.forEach(match => {
         const li = document.createElement("li");
         li.textContent = match;
         li.addEventListener("click", () => {
            searchInput.value = match;
            suggestions.innerHTML = "";
            suggestions.style.display = "none";
         });
         suggestions.appendChild(li);
      });
   }
   else suggestions.style.display = "none";
});
const searchButton = document.querySelector(".search-button");
if (searchButton){
   searchButton.addEventListener("click", (e) => {
      e.preventDefault();
      suggestions.innerHTML = "";
      const searchInputValue = searchInput.value;
      if (searchInputValue) window.location.href = `/search/${encodeURIComponent(searchInputValue)}`;
   });
}