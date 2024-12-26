document.querySelector('.selected-filter').addEventListener('click', function(){
    var optionDiv = document.querySelector('.option-filter');
    if(optionDiv.style.display == 'none') optionDiv.style.display = 'block';
    else optionDiv.style.display = 'none';
 });
 document.querySelectorAll('.option-filter p').forEach(function(option){
    option.addEventListener('click', function(){
       var selectedLang = this.textContent;
       var optionDiv = document.querySelector('.option-filter');
       var selectedText = document.getElementById('selectedText');
    //    document.querySelector('.selected-filter').textContent = selectedLang;
       selectedText.textContent = selectedLang;
       document.querySelector('.selected-filter').style.color = "black";
       optionDiv.style.display = 'none';
    });
 });
 function toggleDropdown() {
    const dropdown = document.getElementById('dropdown');
    dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}

 function selectOption(optionText) {
    const selectedText = document.getElementById('selectedText');
    selectedText.textContent = optionText;
}