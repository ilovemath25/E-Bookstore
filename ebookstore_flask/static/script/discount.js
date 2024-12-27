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
