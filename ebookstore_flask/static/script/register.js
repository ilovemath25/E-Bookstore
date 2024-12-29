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


