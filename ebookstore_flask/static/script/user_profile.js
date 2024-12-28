document.getElementById('logout').addEventListener('click', () => {
   document.querySelector(".logout-modal-container").classList.remove('logout-hidden');
});
document.getElementById('cancel-logout').addEventListener('click', () => {
   document.querySelector(".logout-modal-container").classList.add('logout-hidden');
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