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
   const cancelButton = document.getElementById('cancel-edit');
   const errorMessage = document.querySelector('.error-message');
   const itemSubtotalElement = document.getElementById('item-subtotal');
   const discountElement = document.getElementById('discount');
   const shippingSubtotalElement = document.getElementById('shipping-subtotal');
   const totalElement = document.getElementById('total-price');
   let discountAmount = 1;
   let shippingDiscountAmount = 1;
   let isFormModified = false;

   const updateCartSummary = () => {
      let totalItems = 0;
      let subtotal = 0;
      cartItems.forEach(item => {
         const quantity = parseInt(item.querySelector('.quantity-input').value);
         const bookPrice = parseFloat(item.querySelector('.book-price').textContent.replace('$', ''));
         if (item.querySelector('.select-item').checked) {
            totalItems += quantity;
            subtotal += bookPrice * quantity;
         }
      });
      totalItemsElement.textContent = totalItems;
      subtotalElement.textContent = `$${subtotal.toFixed(2)}`;
      updateCheckoutDetails(subtotal);
   };

   const updateTotalPrice = (quantityInput, bookPrice, totalPriceElement) => {
      let quantity = Math.max(1, parseInt(quantityInput.value));
      quantityInput.value = quantity;
      totalPriceElement.textContent = `$${(bookPrice * quantity).toFixed(2)}`;
      updateCartSummary();
   };

   const updateCheckoutDetails = (subtotal) => {
      const shippingSubtotal = 30 * shippingDiscountAmount;
      const total = subtotal * discountAmount + shippingSubtotal;
      itemSubtotalElement.textContent = `$${subtotal.toFixed(2)}`;
      shippingSubtotalElement.textContent = `$${shippingSubtotal.toFixed(2)}`;
      totalElement.textContent = `$${total.toFixed(2)}`;
   };

   const applyDiscount = () => {
      const discountType = document.querySelector('.discount-type').value;
      const discountValue = parseFloat(document.querySelector('.discount-value').value);
      if (discountType === 'Shipping') shippingDiscountAmount = discountValue;
      else discountAmount = discountValue;
      updateCartSummary();
   };

   cartItems.forEach(item => {
      const quantityInput = item.querySelector('.quantity-input');
      const bookPrice = parseFloat(item.querySelector('.book-price').textContent.replace('$', ''));
      const totalPriceElement = item.querySelector('.total-price');
      quantityInput.addEventListener('input', (event) => {
         event.preventDefault();
         isFormModified = true;
         updateTotalPrice(quantityInput, bookPrice, totalPriceElement);
      });
      item.querySelectorAll('.quantity-btn').forEach(btn => {
         btn.addEventListener('click', function(event) {
            event.preventDefault();
            isFormModified = true;
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
      item.querySelector('.select-item').addEventListener('change', () => {
         isFormModified = true;
         updateCartSummary();
      });
      updateTotalPrice(quantityInput, bookPrice, totalPriceElement);
   });

   selectAllCheckboxes.forEach(selectAll => {
      selectAll.addEventListener('change', function() {
         isFormModified = true;
         const isChecked = this.checked;
         itemCheckboxes.forEach(item => item.checked = isChecked);
         selectAllCheckboxes.forEach(checkbox => checkbox.checked = isChecked);
         updateCartSummary();
      });
   });

   itemCheckboxes.forEach(item => {
      item.addEventListener('change', function() {
         isFormModified = true;
         const allChecked = Array.from(itemCheckboxes).every(item => item.checked);
         selectAllCheckboxes.forEach(selectAll => selectAll.checked = allChecked);
         updateCartSummary();
      });
   });

   const luhnAlgorithm = (number) => {
      const digits = number.split('').reverse().map(digit => parseInt(digit, 10));
      const total = digits.map((digit, idx) => idx % 2 ? (digit * 2 > 9 ? digit * 2 - 9 : digit * 2) : digit)
                          .reduce((sum, digit) => sum + digit, 0);
      return total % 10 === 0;
   };

   document.getElementById('card-expiry').addEventListener('input', (e) => {
      let value = e.target.value.replace(/[^\d]/g, '');
      if (value.length > 2) value = value.slice(0, 2) + '/' + value.slice(2);
      e.target.value = value.slice(0, 5);
      const isValid = /^(0[1-9]|1[0-2])\/\d{2}$/.test(value);
      errorMessage.textContent = isValid || value === '' ? '' : 'Invalid format. Use MM/YY.';
   });

   document.getElementById('card-number').addEventListener('input', function() {
      const cardNumber = this.value;
      errorMessage.textContent = cardNumber.length < 13 || cardNumber.length > 19 || !luhnAlgorithm(cardNumber) ? 'Invalid card number. Please check and try again.' : '';
   });

   addAnotherCardButton.addEventListener('click', () => {
      creditCardModal.classList.remove('credit-card-hidden');
   });

   cancelButton.addEventListener('click', () => {
      creditCardModal.classList.add('credit-card-hidden');
   });
   
   document.querySelectorAll('.card-container').forEach((card, index) => {
      card.addEventListener('click', () => {
         document.querySelectorAll('.card-container').forEach(c => c.classList.remove('selected-card'));
         card.classList.add('selected-card');
      });
   });
   document.querySelectorAll('.fa-circle-xmark').forEach((element) => {
      element.addEventListener('click', () => {
         const productID = element.getAttribute('product-id');
         document.getElementById('delete-item-id').value = productID;
         document.querySelector(".delete-card-container").classList.remove('credit-card-hidden');
      });
   });
   document.getElementById('cancel-delete').addEventListener('click', () => {
      document.querySelector(".delete-card-container").classList.add('credit-card-hidden');
   });
   paymentMethodInputs.forEach(input => {
      input.addEventListener('change', function() {
         if (this.checked) {
            paymentMethodInputs.forEach(otherInput => {
               if (otherInput !== this) {
                  otherInput.checked = false;
               }
            });
            paymentAccountSection.classList.toggle('payment-method-hidden', this.id !== 'credit-card');
         }
      });
   });
   const checkoutButton = document.querySelector(".checkout-btn");

   checkoutButton.addEventListener("click", async (event) => {
      event.preventDefault();
      const selectedProducts = Array.from(document.querySelectorAll(".select-item:checked"))
         .map(item => ({
            id: item.value,
            quantity: item.closest(".cart-item").querySelector(".quantity-input").value
         }));

      if (selectedProducts.length === 0) {
         alert("Please select at least one product to checkout.");
         return;
      }
      const paymentMethod = Array.from(document.querySelectorAll(".payment-method-input:checked"))
         .map(item => item.id)
         .join(", ");
      if (!paymentMethod) {
         alert("Please select a payment method.");
         return;
      }
      let selectedCardIndex = null;
      if (paymentMethod === "credit-card") {
         document.querySelectorAll(".card-container").forEach((card, index) => {
            if (card.classList.contains("selected-card")) selectedCardIndex = index;
         });
         if (selectedCardIndex === null) {
            alert("Please select a credit card.");
            return;
         }
      }
      const addressInputs = Array.from(document.querySelectorAll(".address-input"));
      const addressData = addressInputs.reduce((acc, input) => {
         acc[input.placeholder] = input.value;
         return acc;
      }, {});

      if (Object.values(addressData).some(value => !value.trim())) {
         alert("Please fill out all information fields.");
         return;
      }
      const totalPrice = parseInt(document.getElementById('total-price').textContent);
      
      const checkoutData = {
         products: selectedProducts,
         paymentMethod: paymentMethod,
         selectedCardIndex: selectedCardIndex,
         address: addressData,
         totalPrice: totalPrice
      };

      try {
         const response = await fetch("/cart/checkout", {
            method: "POST",
            headers: {
               "Content-Type": "application/json"
            },
            body: JSON.stringify(checkoutData)
         });
         const result = await response.json();
         if (response.ok) {
            alert("Checkout successful!");
            window.location.href = "/user/profile/order_history";
         }
         else {
            alert(`Checkout failed: ${result.message}`);
         }
      }
      catch (error) {
         console.error("Error during checkout:", error);
         alert("An error occurred during checkout. Please try again.");
      }
   });

   window.addEventListener('scroll', function() {
      if (cartSummary.getBoundingClientRect().bottom > window.innerHeight - 15) cartSummary.classList.add('shadow');
      else cartSummary.classList.remove('shadow');
   });

   window.addEventListener('beforeunload', (e) => {
      if (isFormModified) e.preventDefault();
   });

   updateCartSummary();
   applyDiscount();
});
