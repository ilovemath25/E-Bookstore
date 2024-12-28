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
};


const user_profile_change_password_page = () => {
   document.querySelector('.submit-button').addEventListener('click', () => {
   changePassword();
   console.log("Password changed");
   });


   // Mock current password stored in the system

   const mockCurrentPassword = "haloinibv";
   function changePassword() {
   
      const currentPassword = document.getElementById("currentPassword").value;
      const newPassword = document.getElementById("newPassword").value;
      const confirmPassword = document.getElementById("confirmNewPassword").value;
      console.log(currentPassword, newPassword, confirmPassword);

      const message = document.getElementById("message");

      // Clear previous messages
      message.textContent = "";
      message.classList.remove("error", "success");

      // Check if the current password matches
      if (currentPassword !== mockCurrentPassword) {
         message.textContent = "The current password is incorrect.";
         message.classList.add("error");
         return;
         }

      // Check if the new password and confirm password match
      if (newPassword !== confirmPassword) {
         message.textContent = "New password and confirmation do not match.";
         message.classList.add("error");
         return;
         }

      // Check if the new password is different from the current password
      if (newPassword === mockCurrentPassword) {
         message.textContent = "The new password must be different from the current password.";
         message.classList.add("error");
         return;
         }

      // Successfully changed password
      message.textContent = "Password successfully changed!";
      message.classList.add("success");
   }

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
   document.getElementById('confirm-edit').addEventListener('click', () => {
      window.location.href = '/user/profile/credit_card/add';
   });
   document.querySelector('.fa-circle-xmark').addEventListener('click', () => {
      document.querySelector(".delete-card-container").classList.remove('credit-card-hidden');
   });
   document.getElementById('cancel-delete').addEventListener('click', () => {
      document.querySelector(".delete-card-container").classList.add('credit-card-hidden');
   });
   document.getElementById('confirm-delete').addEventListener('click', () => {
      window.location.href = '/user/profile/credit_card/delete';
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
}

document.addEventListener('DOMContentLoaded', () => {
   const main = document.querySelector('main');
   if (main) {
      if (main.classList.contains('user_profile')) {
         user_profile_page();
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