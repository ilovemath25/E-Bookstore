const user_profile_page = () => {

   function maskValue(originalValue, type) {
      if (type === 'email-value') {
         const [local, domain] = originalValue.split('@');
         return `${local.slice(0, 2)}${'*'.repeat(local.length - 2)}@${domain}`;
      }
      else if (type === 'phone-value') {
         return `${originalValue.slice(0, 2)}** *** ***`;
      }
      return '*****'; // Fallback
   }
   function toggleVisibility(targetId, iconId) {
      const valueElement = document.getElementById(targetId);
      const iconElement = document.getElementById(iconId);
      const originalValue = valueElement.getAttribute('data-original');
      if (iconElement.classList.contains('fa-eye-slash')) {
         valueElement.textContent = valueElement.getAttribute('data-original') || valueElement.textContent;
         iconElement.classList.remove('fa-eye-slash');
         iconElement.classList.add('fa-eye');
      }
      else {
         valueElement.textContent = maskValue(originalValue, targetId);
         iconElement.classList.remove('fa-eye');
         iconElement.classList.add('fa-eye-slash');
      }
   }

   document.getElementById('toggle-email').addEventListener('click', () => {toggleVisibility('email-value', 'toggle-email');});
   document.getElementById('toggle-phone').addEventListener('click', () => {toggleVisibility('phone-value', 'toggle-phone');});
   document.getElementById('email-value').textContent = maskValue(document.getElementById('email-value').getAttribute('data-original'),'email-value');
   document.getElementById('phone-value').textContent = maskValue(document.getElementById('phone-value').getAttribute('data-original'),'phone-value');

   const selected = document.getElementById('selected-gender');
   const optionsContainer = document.querySelector('.dropdown-options');
   const options = document.querySelectorAll('.dropdown-option');

   selected.addEventListener('click', () => {
      optionsContainer.classList.toggle('active');
   });

   options.forEach(option => {
      option.addEventListener('click', () => {
         selected.value = option.textContent;
         options.classList.remove('active');
      });
   });
};
const user_profile_edit_page = () => {

   const selected = document.getElementById('selected-gender');
   const selectedHidden = document.getElementById('selected-gender-hidden');
   const optionsContainer = document.querySelector('.dropdown-options');
   const options = document.querySelectorAll('.dropdown-option');

   selected.addEventListener('click', () => {
      optionsContainer.classList.toggle('active');
   });
   options.forEach(option => {
      option.addEventListener('click', () => {
         selected.value = option.textContent;
         selectedHidden.value = option.textContent;
         optionsContainer.classList.remove('active');
      });
   });
   document.addEventListener('click', (e) => {
      if (!selected.contains(e.target) && !optionsContainer.contains(e.target)) {
         optionsContainer.classList.remove('active');
      }
   });
};

const user_profile_change_password_page = () => {
   const form = document.querySelector(".section-container");
   const oldPasswordInput = document.getElementById("old-password");
   const currentPasswordInput = document.getElementById("currentPassword");
   const newPasswordInput = document.getElementById("newPassword");
   const confirmNewPasswordInput = document.getElementById("confirmNewPassword");
   const messageElement = document.querySelector(".change-password-error-message");
   const submitButton = document.querySelector(".change-password-button");
   document.querySelector(".change-password-container").querySelectorAll('.profile-input').forEach(input => {
      input.addEventListener('input', () => {
         messageElement.textContent = "";
         const oldPassword = oldPasswordInput.value.trim();
         const currentPassword = currentPasswordInput.value.trim();
         const newPassword = newPasswordInput.value.trim();
         const confirmNewPassword = confirmNewPasswordInput.value.trim();

         let checkAllFields = true;

         // Validate fields
         if (!currentPassword || !newPassword || !confirmNewPassword) {
             messageElement.textContent = "All fields are required.";
             messageElement.style.color = "red";
             checkAllFields = false;
         }
         else if (currentPassword !== oldPassword) {
            messageElement.textContent = "Old password is incorrect.";
            messageElement.style.color = "red";
            checkAllFields = false;
        }
        else if (newPassword.length < 8) {
            messageElement.textContent = "New password must be at least 8 characters long.";
            messageElement.style.color = "red";
            checkAllFields = false;
        }
         // Check if new password matches confirmation
         else if (newPassword !== confirmNewPassword) {
             messageElement.textContent = "New passwords do not match.";
             messageElement.style.color = "red";
             checkAllFields = false;
         }
         submitButton.disabled = !checkAllFields;
         submitButton.classList.toggle("disabled-button", submitButton.disabled);
     });
   });
   
   form.addEventListener('submit', (e) => {
      alert("Password changed successfully!");
   });
};

const user_profile_credit_card_page = () => {
   function luhnAlgorithm(number) {
      const digits = number.split('').reverse().map(digit => parseInt(digit, 10));
      const result = digits.map((digit, idx) => {
         if (idx % 2 === 1) {
            const doubled = digit * 2;
            return doubled > 9 ? doubled - 9 : doubled;
         }
         return digit;
      });
      const total = result.reduce((sum, digit) => sum + digit, 0);
      return total % 10 === 0;
   }
   function maskCardNumber(cardNumber) {
      return '**** **** **** ' + cardNumber.slice(-4);
   }
   document.getElementById('card-expiry').addEventListener('input', (e) => {
      let value = e.target.value.replace(/[^\d]/g, '');
      if (value.length > 2) value = value.slice(0, 2) + '/' + value.slice(2);
      e.target.value = value.slice(0, 5);
      const isValid = /^(0[1-9]|1[0-2])\/\d{2}$/.test(value);
      const errorMessage = document.querySelector('.error-message');
      errorMessage.textContent = isValid || value === '' ? '' : 'Invalid format. Use MM/YY.';
    });
    
   document.getElementById('add-card').addEventListener('click', () => {
      document.querySelector(".credit-card-modal-container").classList.remove('credit-card-hidden');
   });
   document.getElementById('cancel-edit').addEventListener('click', () => {
      document.querySelector(".credit-card-modal-container").classList.add('credit-card-hidden');
   });
   document.querySelectorAll('.fa-circle-xmark').forEach((element) => {
      element.addEventListener('click', () => {
         const cardNumber = element.getAttribute('data-card-number');
         document.getElementById('delete-card-number').value = cardNumber;
         document.querySelector(".delete-card-container").classList.remove('credit-card-hidden');
      });
   });
   document.getElementById('cancel-delete').addEventListener('click', () => {
      document.querySelector(".delete-card-container").classList.add('credit-card-hidden');
   });
   document.getElementById('card-number').addEventListener('input', function() {
      const cardNumber = this.value;
      const errorMessage = document.querySelector('.error-message');

      if (cardNumber.length<13 || cardNumber.length>19 || !luhnAlgorithm(cardNumber)) {
         errorMessage.textContent = 'Invalid card number. Please check and try again.';
      }
      else {
         errorMessage.textContent = '';
      }
   });
   document.querySelectorAll('.card-number').forEach((element) => {
      const cardNumber = element.getAttribute('data-card-number');
      element.textContent = maskCardNumber(cardNumber);
   });
}

document.addEventListener('DOMContentLoaded', () => {
   const main = document.querySelector('main');
   if (main) {
      if (main.classList.contains('user_profile')) {
         user_profile_page();
      }
      else if (main.classList.contains('user_profile_edit')) {
         user_profile_edit_page();
      }
      else if (main.classList.contains('user_profile_change_password')) {
         user_profile_change_password_page();
      }
      else if (main.classList.contains('user_profile_credit_card_page')) {
         user_profile_credit_card_page();
      }
   }
   else {
      console.error("No <main> tag found!");
   }
});
document.getElementById('logout').addEventListener('click', () => {
   document.querySelector(".logout-modal-container").classList.remove('logout-hidden');
});
document.getElementById('cancel-logout').addEventListener('click', () => {
   document.querySelector(".logout-modal-container").classList.add('logout-hidden');
});