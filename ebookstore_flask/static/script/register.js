// Toggle the dropdown options visibility when the "Gender" field is clicked
document.querySelector('#gender').addEventListener('click', function () {
    var optionDiv = document.getElementById('option-gen');
    optionDiv.style.display = optionDiv.style.display === 'none' || optionDiv.style.display === '' ? 'block' : 'none';
});

document.querySelectorAll('.option-gen p').forEach(function (option) {
    option.addEventListener('click', function () {
        var selectedGender = this.textContent;
        var optionDiv = document.getElementById('option-gen');

        document.getElementById('gender').value = selectedGender;

        optionDiv.style.display = 'none';
    });
});

document.addEventListener('click', function (event) {
    var dropdown = document.querySelector('.dropdown-container');
    var optionDiv = document.getElementById('option-gen');

    if (!dropdown.contains(event.target)) {
        optionDiv.style.display = 'none';
    }
});


const modal = document.getElementById("privacyPolicyModal");

const link = document.getElementById("privacyPolicyLink");

const closeBtn = document.querySelector(".modal .close-button");

link.onclick = function(event) {
    event.preventDefault(); 
    modal.style.display = "block";
};

closeBtn.onclick = function() {
    modal.style.display = "none";
};

document.addEventListener("DOMContentLoaded", () => {
    const passwordInput = document.getElementById("password");
    const confirmPasswordInput = document.getElementById("confirmPassword");
    const phoneNumberInput = document.getElementById("phoneNumber");
    const emailInput = document.getElementById("email"); // Assuming you have an email input field
    const submitButton = document.querySelector(".register-button");
    const messageElement = document.querySelector(".register-error-message");
    const birthDateInput = document.getElementById("birthDate");

    // Form submission validation
    function validateForm() {
        const password = passwordInput.value.trim();
        const confirmPassword = confirmPasswordInput.value.trim();
        const phoneNumber = phoneNumberInput.value.trim();
        const email = emailInput.value.trim(); // Retrieve email value
        const birthDate = birthDateInput.value.trim();
        messageElement.textContent = "";

        let isValid = true;

        // Check if all inputs are empty
        if (!password && !confirmPassword && !phoneNumber && !email && !birthDate) {
            messageElement.textContent = ""; // Clear error messages
            submitButton.disabled = true;
            return;
        }

        // Validate password length
        if (password.length < 8) {
            messageElement.textContent = "Password must be more than 8 characters.";
            messageElement.style.color = "red";
            isValid = false;
        }

        // Validate password match
        if (password !== confirmPassword) {
            messageElement.textContent = "Passwords do not match.";
            messageElement.style.color = "red";
            isValid = false;
        }

        // Validate phone number length
        if (phoneNumber && phoneNumber.length !== 10) {
            messageElement.textContent = "Phone number must be 10 digits.";
            messageElement.style.color = "red";
            isValid = false;
        }

        // Validate email format
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email && !emailRegex.test(email)) {
            messageElement.textContent = "Invalid email format.";
            messageElement.style.color = "red";
            isValid = false;
        }

        const birthDateRegex = /^(19|20)\d{2}\/(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])$/;
        if (birthDate!=="" && !birthDateRegex.test(birthDate)) {
            messageElement.textContent = "Invalid Birth Date format. Use YYYY/MM/DD.";
            messageElement.style.color = "red";
            isValid = false;
        }
        // Enable or disable the submit button based on validation
        submitButton.disabled = !isValid;
    }

    // Add event listeners to the input fields
    passwordInput.addEventListener("input", validateForm);
    confirmPasswordInput.addEventListener("input", validateForm);
    phoneNumberInput.addEventListener("input", validateForm);
    emailInput.addEventListener("input", validateForm); // Listen for changes in the email field
    birthDateInput.addEventListener("input", validateForm);
});


