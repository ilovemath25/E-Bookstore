document.addEventListener('DOMContentLoaded', function() {
   const cartSummary = document.querySelector('.cart-summary');
   const totalItemsElement = cartSummary.querySelector('.total-item');
   const subtotalElement = cartSummary.querySelector('.cart-summary-item:last-child');
   const cartItems = document.querySelectorAll('.cart-item');
   const selectAllCheckboxes = document.querySelectorAll('#select-all');
   const itemCheckboxes = document.querySelectorAll('.select-item');
   const paymentMethodInputs = document.querySelectorAll('.payment-method-input');
   const paymentAccountSection = document.querySelector('.select-payment-account');
   const addAnotherCardButton = document.getElementById('add-another-card');
   const creditCardModal = document.querySelector('.credit-card-modal-container');
   const saveButton = document.getElementById('confirm-edit');
   const cancelButton = document.getElementById('cancel-edit');
   const addCardContainer = document.querySelector('.add-card-container');
   const errorMessage = document.querySelector('.error-message');
   const itemSubtotalElement = document.getElementById('item-subtotal');
   const discountElement = document.getElementById('discount');
   const shippingSubtotalElement = document.getElementById('shipping-subtotal');
   const totalElement = document.getElementById('total');
   const discountInput = document.querySelector('.discount-input');
   const discountError = document.querySelector('.discount-error');
   const applyDiscountButton = document.querySelector('.apply-discount');

   let discountAmount = 0;

   const updateCartSummary = () => {
      let totalItems = 0;
      let subtotal = 0;
      cartItems.forEach(item => {
         const quantityInput = item.querySelector('.quantity-input');
         const bookPrice = parseFloat(item.querySelector('.book-price').textContent.replace('$', ''));
         const quantity = parseInt(quantityInput.value);
         const itemCheckbox = item.querySelector('.select-item');
         if (itemCheckbox.checked) {
            totalItems += quantity;
            subtotal += bookPrice * quantity;
         }
      });
      totalItemsElement.textContent = totalItems;
      subtotalElement.textContent = `$${subtotal.toFixed(2)}`;
      updateCheckoutDetails(subtotal);
   };

   const updateTotalPrice = (quantityInput, bookPrice, totalPriceElement) => {
      let quantity = parseInt(quantityInput.value);
      if (quantity < 1) {
         quantityInput.value = 1;
         quantity = 1;
      }
      const totalPrice = (bookPrice * quantity).toFixed(2);
      totalPriceElement.textContent = `$${totalPrice}`;
      updateCartSummary();
   };

   const updateCheckoutDetails = (subtotal) => {
      const shippingSubtotal = 0;
      const total = subtotal - discountAmount + shippingSubtotal;

      itemSubtotalElement.textContent = `$${subtotal.toFixed(2)}`;
      discountElement.textContent = `-$${discountAmount.toFixed(2)}`;
      shippingSubtotalElement.textContent = `$${shippingSubtotal.toFixed(2)}`;
      totalElement.textContent = `$${total.toFixed(2)}`;
   };

   const checkDiscount = () => {
      const discountCode = discountInput.value;
      fetch('/check_discount', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json'
         },
         body: JSON.stringify({ discount: discountCode })
      })
      .then(response => response.json())
      .then(data => {
         console.log(data);
         if (!data.valid) {
            discountError.textContent = "Invalid discount code";
            discountAmount = 0;
         } else {
            discountError.textContent = "";
            discountAmount = data.amount;
         }
         updateCartSummary();
      });
   };

   applyDiscountButton.addEventListener('click', () => {
      checkDiscount();
   });

   cartItems.forEach(item => {
      const quantityInput = item.querySelector('.quantity-input');
      const bookPrice = parseFloat(item.querySelector('.book-price').textContent.replace('$', ''));
      const totalPriceElement = item.querySelector('.total-price');
      quantityInput.addEventListener('input', (event) => {
         event.preventDefault(); // Prevent the default form submission
         updateTotalPrice(quantityInput, bookPrice, totalPriceElement);
      });
      item.querySelectorAll('.quantity-btn').forEach(btn => {
         btn.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent the default form submission
            let currentQuantity = parseInt(quantityInput.value);
            if (this.textContent === '-') {
               if (currentQuantity > 1) {
                  quantityInput.value = currentQuantity - 1;
               }
            } else if (this.textContent === '+') {
               quantityInput.value = currentQuantity + 1;
            }
            updateTotalPrice(quantityInput, bookPrice, totalPriceElement);
         });
      });
      item.querySelector('.select-item').addEventListener('change', updateCartSummary);
      updateTotalPrice(quantityInput, bookPrice, totalPriceElement);
   });

   selectAllCheckboxes.forEach(selectAll => {
      selectAll.addEventListener('change', function() {
         const isChecked = this.checked;
         itemCheckboxes.forEach(item => item.checked = isChecked);
         selectAllCheckboxes.forEach(checkbox => checkbox.checked = isChecked);
         updateCartSummary();
      });
   });

   itemCheckboxes.forEach(item => {
      item.addEventListener('change', function() {
         const allChecked = Array.from(itemCheckboxes).every(item => item.checked);
         selectAllCheckboxes.forEach(selectAll => selectAll.checked = allChecked);
         updateCartSummary();
      });
   });

   const luhnAlgorithm = (number) => {
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
   };

   const maskCardNumber = (cardNumber) => '**** **** **** ' + cardNumber.slice(-4);

   document.getElementById('card-expiry').addEventListener('input', (e) => {
      let value = e.target.value.replace(/[^\d]/g, '');
      if (value.length > 2) value = value.slice(0, 2) + '/' + value.slice(2);
      e.target.value = value.slice(0, 5);
      const isValid = /^(0[1-9]|1[0-2])\/\d{2}$/.test(value);
      errorMessage.textContent = isValid || value === '' ? '' : 'Invalid format. Use MM/YY.';
   });

   document.getElementById('card-number').addEventListener('input', function() {
      const cardNumber = this.value;
      if (cardNumber.length < 13 || cardNumber.length > 19 || !luhnAlgorithm(cardNumber)) {
         errorMessage.textContent = 'Invalid card number. Please check and try again.';
      }
      else {
         errorMessage.textContent = '';
      }
   });

   addAnotherCardButton.addEventListener('click', () => {
      creditCardModal.classList.remove('credit-card-hidden');
   });

   cancelButton.addEventListener('click', () => {
      creditCardModal.classList.add('credit-card-hidden');
   });

   saveButton.addEventListener('click', function(event) {
      event.preventDefault();
      const cardNumber = document.getElementById('card-number').value;
      fetch('/check_bin', {
         method: 'POST',
         headers: {
            'Content-Type': 'application/json'
         },
         body: JSON.stringify({ number: cardNumber })
      })
      .then(response => response.json())
      .then(data => {
         if (data.error) {
            errorMessage.textContent = data.error;
         } else {
            document.querySelector('.add-card-container .card-number').textContent = maskCardNumber(cardNumber);
            document.querySelector('.add-card-container .card-type').textContent = data.Brand;
            document.querySelector('.add-card-container .card-center p').textContent = data.Issuer;
            creditCardModal.classList.add('credit-card-hidden');
            addAnotherCardButton.style.display = 'none';
            addCardContainer.classList.remove('credit-card-hidden');
         }
      });
   });

   document.querySelectorAll('.card-container').forEach(card => {
      card.addEventListener('click', () => {
         document.querySelectorAll('.card-container').forEach(c => c.classList.remove('selected-card'));
         card.classList.add('selected-card');
      });
   });

   paymentMethodInputs.forEach(input => {
      input.addEventListener('change', function() {
         if (this.checked) {
            paymentMethodInputs.forEach(otherInput => {
               if (otherInput !== this) {
                  otherInput.checked = false;
               }
            });
            if (this.id === 'credit-card') {
               paymentAccountSection.classList.remove('payment-method-hidden');
            } else if (this.id === 'cod') {
               paymentAccountSection.classList.add('payment-method-hidden');
            }
         }
      });
   });

   document.querySelectorAll('.fa-circle-xmark').forEach((element) => {
      element.addEventListener('click', () => {
         const cardNumber = element.getAttribute('data-card-number');
         document.getElementById('delete-item-id').value = cardNumber;
         document.querySelector(".delete-card-container").classList.remove('credit-card-hidden');
      });
   });
   document.getElementById('cancel-delete').addEventListener('click', () => {
      document.querySelector(".delete-card-container").classList.add('credit-card-hidden');
   });

   window.addEventListener('scroll', function() {
      if (cartSummary.getBoundingClientRect().bottom > window.innerHeight - 15) cartSummary.classList.add('shadow');
      else cartSummary.classList.remove('shadow');
   });

   updateCartSummary();
});
