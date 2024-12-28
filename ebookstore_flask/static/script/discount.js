function toggleFields(selectedType) {
    const dateFields = document.getElementById('date-fields');
    const shippingFields = document.getElementById('shipping-fields');

    if (selectedType === 'Shipping') {
        dateFields.style.display = 'none';
        shippingFields.style.display = 'block';
    } else {
        dateFields.style.display = 'block';
        shippingFields.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', function () {
    const selectedType = "{{ discount.Disc_type }}";
    toggleFields(selectedType);
});
document.getElementById('delete').addEventListener('click', () => {
    document.querySelector(".logout-modal-container").classList.remove('delete-hidden');
 });
 document.getElementById('cancel-delete').addEventListener('click', () => {
    document.querySelector(".logout-modal-container").classList.add('delete-hidden');
 });

 document.addEventListener('DOMContentLoaded', function () {
    const discValidToInput = document.getElementById('Disc_validTo');
    const discValidFromInput = document.getElementById('Disc_validFrom');
    const discMinInput = document.getElementById('Disc_min');
    const selectedType = document.querySelector('input[name="Disc_type"]:checked');

    if (selectedType && selectedType.value === 'Shipping') {
        discMinInput.setAttribute('required', 'required');
        discValidFromInput.removeAttribute('required');
        discValidToInput.removeAttribute('required');
    } else if(selectedType && (selectedType.value === 'Seasoning' || selectedType.value === 'Special Event')) {
        discMinInput.removeAttribute('required');
        discValidFromInput.setAttribute('required');
        discValidToInput.setAttribute('required');
    }

    document.querySelectorAll('input[name="Disc_type"]').forEach(radio => {
        radio.addEventListener('change', () => {
            if (radio.value === 'Seasoning' || radio.value === 'Special Event') {
                discMinInput.removeAttribute('required');
                discValidFromInput.setAttribute('required');
                discValidToInput.setAttribute('required');
            } else {
                discMinInput.removeAttribute('required');
                discValidFromInput.setAttribute('required');
                discValidToInput.setAttribute('required');
            }
        });
    });
});

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
    }
});