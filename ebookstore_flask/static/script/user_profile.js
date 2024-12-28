const user_profile_page = () => {

document.getElementById('logout').addEventListener('click', () => {
   document.querySelector(".logout-modal-container").classList.remove('logout-hidden');
});
document.getElementById('cancel-logout').addEventListener('click', () => {
   document.querySelector(".logout-modal-container").classList.add('logout-hidden');
});
document.getElementById('add-card').addEventListener('click', () => {
   document.querySelector(".credit-card-modal-container").classList.remove('credit-card-hidden');
});
document.getElementById('cancel-edit').addEventListener('click', () => {
   document.querySelector(".credit-card-modal-container").classList.add('credit-card-hidden');
});

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
   const form = document.querySelector(".section-container");
   const oldPasswordInput = document.getElementById("old-password");
   const currentPasswordInput = document.getElementById("currentPassword");
   const newPasswordInput = document.getElementById("newPassword");
   const confirmNewPasswordInput = document.getElementById("confirmNewPassword");
   const messageElement = document.querySelector(".change-password-error-message");
   const submitButton = document.querySelector(".change-password-button");
   document.querySelector(".change-password-container").querySelectorAll('.profile-input').forEach(input => {
      input.addEventListener('input', () => {
         input.dispatchEvent(new Event('input'));
         // Clear previous messages
         messageElement.textContent = "";

         // Get input values
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
  
      };

document.addEventListener('DOMContentLoaded', () => {
   const main = document.querySelector('main'); // Select the <main> tag
   if (main) {
      if (main.classList.contains('user_profile')) {
         user_profile_page();
      } else if (main.classList.contains('user_profile_change_password')) {
         user_profile_change_password_page();
      }
   } else {
         console.error("No <main> tag found!");
         }
     });