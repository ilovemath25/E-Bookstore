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

        // if (selectedText.textContent != 'Discount ID'){
        //     console.log('msk order selecteedlang')
        //     selectedText.textContent = 'Discount ID'
        // }

        selectedText.textContent = selectedLang;
        console.log(selectedLang);
        localStorage.setItem("option_filter", selectedText.textContent);
        document.querySelector('.selected-filter').style.color = "black";
        optionDiv.style.display = 'none';
        if (!['Member ID', 'Name', 'Email'].includes(selectedLang)) {
            selectedLang = 'Member ID';
        }
        if (selectedLang === 'Member ID'){
            document.getElementById('filter_field').value = 'memberID';
        }
        else if (selectedLang === 'Name'){
            document.getElementById('filter_field').value = 'name';
        }
        else if (selectedLang === 'Email'){
            document.getElementById('filter_field').value = 'email';
        }
    });
});
document.addEventListener("DOMContentLoaded", () => {
    var selectedText = document.getElementById('selectedText');
    var savedOption = localStorage.getItem("option_filter");
    if (savedOption) {
        if (!['Member ID', 'Name', 'Email'].includes(savedOption)) {
            savedOption = 'Member ID';
        }
        selectedText.textContent = savedOption;
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
    if (!['Member ID', 'Name', 'Email'].includes(optionText)) {
        optionText = 'Member ID';
    }
    selectedText.textContent = optionText;
}

