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
        localStorage.setItem("option_filter", selectedText.textContent);
        document.querySelector('.selected-filter').style.color = "black";
        optionDiv.style.display = 'none';
        if (!['Product ID', 'Book Name', 'Category'].includes(selectedLang)) {
            selectedLang = 'Product ID';
        }
        document.getElementById('filter_field').value = selectedLang === 'Product ID' ? 'product_id' : (selectedLang === 'Book Name' ? 'product_name' : 'category');
    });
});
document.addEventListener("DOMContentLoaded", () => {
    var selectedText = document.getElementById('selectedText');
    var savedOption = localStorage.getItem("option_filter");
    console.log(savedOption);
    if (savedOption) {
        if (!['Product ID', 'Book Name', 'Category'].includes(savedOption)) {
            savedOption = 'Product ID';
        }
        selectedText.textContent = savedOption;
            document.getElementById('filter_field').value = savedOption === 'Product ID' ? 'product_id' : (savedOption === 'Book Name' ? 'product_name' : 'category');
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
    if (!['Product ID', 'Book Name', 'Category'].includes(optionText)) {
        optionText = 'Product ID';
    }
    selectedText.textContent = optionText;
}