function toggleFields(selectedType) {
    const dateFields = document.getElementById('date-fields');
    const shippingFields = document.getElementById('shipping-fields');
    if (selectedType === 'Shipping') {
        dateFields.style.display = 'none';
        shippingFields.style.display = 'block';
    }
    else if (selectedType === 'Seasoning' || selectedType === 'Special Event'){
        dateFields.style.display = 'block';
        shippingFields.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', function () {
    const radioInput = document.querySelectorAll(".radio-option input");
    if (radioInput[0].checked) toggleFields("Shipping");
    else if (radioInput[1].checked) toggleFields("Seasoning");
    else if (radioInput[2].checked) toggleFields("Special Event");
});
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

            if (selectedLang === 'Order ID'|| selectedLang === 'Product Name'){
                selectedLang = 'Discount ID'
            }

        selectedText.textContent = selectedLang;
        localStorage.setItem("option_filter", selectedText.textContent);
        document.querySelector('.selected-filter').style.color = "black";
        optionDiv.style.display = 'none';
        
        document.getElementById('filter_field').value = selectedLang === 'Discount ID' ? 'discountID' : 'discountName';
    });
});
document.addEventListener("DOMContentLoaded", () => {
    var selectedText = document.getElementById('selectedText');
    var savedOption = localStorage.getItem("option_filter");
    console.log("savedOption", savedOption);
    if (savedOption) {
        selectedText.textContent = savedOption;
        if (savedOption === 'Order ID'|| savedOption === 'Product Name'){
            savedOption = 'Discount ID'
        }
        document.getElementById('filter_field').value = savedOption === 'Discount ID' ? 'discountID' : 'discountName';
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
    if (optionText === 'Order ID'|| optionText === 'Product Name'){
        optionText = 'Discount ID'
    }
    selectedText.textContent = optionText;
}