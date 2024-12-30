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
const saveBtn = document.getElementById('save-btn');
const formFields = document.querySelectorAll('input[required]');

function validateFields() {
    let isValid = true;
    formFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.style.border = '2px solid red';
        } else {
            field.style.border = '';
        }
    });
    return isValid;
}

formFields.forEach(field => {
    field.addEventListener('input', function () {
        const allFilled = [...formFields].every(f => f.value.trim());
        if (!allFilled) {
            validateFields();
        }
        saveBtn.disabled = !allFilled;
    });
});

saveBtn.addEventListener('click', function (event) {
    const isValid = validateFields();
    if (!isValid) {
        event.preventDefault();
        alert('Please fill out all required fields before saving.');
}});