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

        if (selectedText.textContent === 'Order ID'|| selectedText.textContent === 'Product'){
            console.log('msk order selecteedlang')
            selectedText.textContent = 'Discount ID'
        }

       selectedText.textContent = selectedLang;
       console.log(selectedLang);
       localStorage.setItem("option_filter", selectedText.textContent);
       document.querySelector('.selected-filter').style.color = "black";
       optionDiv.style.display = 'none';
       
       document.getElementById('filter_field').value = selectedLang === 'Discount ID' ? 'discountID' : 'discountCode';
    });
 });
 document.addEventListener("DOMContentLoaded", () => {
    var selectedText = document.getElementById('selectedText');
    var savedOption = localStorage.getItem("option_filter");
    if (savedOption) {
        if (savedOption === 'Order ID'|| savedOption === 'Product'){
            savedOption = 'Discount ID'
        }
        selectedText.textContent = savedOption;
        document.getElementById('filter_field').value = savedOption === 'Discount ID' ? 'discountID' : 'discountCode';
    }
    // if (selectedText.innerHTML == "Order ID") {
    //     selectedText.innerHTML = localStorage.getItem("option_filter");
    // }
 });
 function toggleDropdown() {
    const dropdown = document.getElementById('dropdown');
    dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
}

 function selectOption(optionText) {
    const selectedText = document.getElementById('selectedText');
    if (optionText === 'Order ID'|| optionText === 'Product'){
        optionText = 'Discount ID'
    }
    selectedText.textContent = optionText;
}