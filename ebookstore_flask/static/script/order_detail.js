document.querySelector('.selected-filter').addEventListener('click', function() {
    const optionDiv = document.querySelector('.option-filter');
    optionDiv.style.display = optionDiv.style.display === 'none' ? 'block' : 'none';
});

function selectOption(optionText, optionValue) {
    const selectedText = document.getElementById('selected-text');
    const filterField = document.getElementById('filterField');

    selectedText.textContent = optionText;
    filterField.value = optionValue;

    const optionDiv = document.querySelector('.option-filter');
    optionDiv.style.display = 'none';
}

document.addEventListener('click', function(event) {
    const dropdown = document.getElementById('dropdown_o');
    if (!dropdown.contains(event.target) && !event.target.matches('.selected-filter')) {
        document.querySelector('.option-filter').style.display = 'none';
    }
});

