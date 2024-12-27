// Toggle the dropdown options visibility when the "Gender" field is clicked
document.querySelector('#gender').addEventListener('click', function () {
    var optionDiv = document.getElementById('option-gen');
    optionDiv.style.display = optionDiv.style.display === 'none' || optionDiv.style.display === '' ? 'block' : 'none';
});

// Add click event listeners to all dropdown options
document.querySelectorAll('.option-gen p').forEach(function (option) {
    option.addEventListener('click', function () {
        var selectedGender = this.textContent; // Get the selected gender text
        var optionDiv = document.getElementById('option-gen');

        // Update the input field with the selected gender
        document.getElementById('gender').value = selectedGender;

        // Optionally, close the dropdown after selection
        optionDiv.style.display = 'none';
    });
});

// Close the dropdown if the user clicks outside of it
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


