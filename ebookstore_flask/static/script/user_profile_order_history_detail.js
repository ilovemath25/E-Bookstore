console.log("history detail page");
document.querySelectorAll('.book-review').forEach(bookRate => {
    const stars = bookRate.querySelectorAll('.fa-star');
    // const productId = bookRate.getAttribute('data-book-id');
    let ratingInput = bookRate.querySelector(".book-rate-input");
    const reviewInput = bookRate.querySelector(".book-review-input");
    const submitButton = bookRate.querySelector('.submit-review-btn');
    
        // Disable submit button initially
    submitButton.disabled = true;

        // Function to check if form inputs are valid
    function validateForm() {
        const rating = ratingInput.value;
        const review = reviewInput.value.trim();
        if (rating !== '0' && review.length > 0) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    }


    // Attach click event listeners to each star in this book-rate container
    stars.forEach(star => {
        star.addEventListener('click', function () {
            // Get the clicked star's value
            
            let rating = this.getAttribute('data-value');
            const currentRating = bookRate.getAttribute('data-rating');
            ratingInput.value = rating;
            console.log(`Submitting Rating: ${ratingInput.value}`);
            ratingInput.value = rating;

            // Check if the user clicked the current highest yellow star
            if (rating === currentRating) {
                // Reset rating and turn all stars gray
                rating = '0';
                bookRate.setAttribute('data-rating', 0);
                stars.forEach(star => {
                    star.classList.add('gray');
                    star.classList.remove('yellow');
                });
                console.log("Rating reset to 0.");
                console.log("Selected Rating:", rating);
                return;
            }

            // Update the rating in the current book-rate container
            bookRate.setAttribute('data-rating', rating);
            console.log("Selected Rating:", rating);

            // Update the stars' classes within this book-rate container
            stars.forEach(star => {
                if (star.getAttribute('data-value') <= rating) {
                    // Turn stars yellow up to the clicked rating
                    star.classList.add('yellow');
                    star.classList.remove('gray');
                } else {
                    // Turn stars gray beyond the clicked rating
                    star.classList.add('gray');
                    star.classList.remove('yellow');
                }
            });
        validateForm();
        });
    });
        // Attach input event listener to the review text field
    reviewInput.addEventListener('input', () => {
        console.log(`Review Text: ${reviewInput.value}`);
        validateForm();
    });
});

document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.submit-review-btn').forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default anchor behavior

            const ProductId = this.getAttribute('data-form-id');
            const CustomerId = this.getAttribute('data-customer-id');
            const starRating = document.getElementById(`ratingStarInput_${ProductId}`).value;
            const review = document.getElementById(`reviewTextInput_${ProductId}`).value;
            // const customerId = document.getElementById(`customerID_${CustomerId}`).value;
            console.log("Rating:", starRating);
            console.log("Review:", review);
            console.log("Product ID:", ProductId);
            console.log("Customer ID:", CustomerId);
            fetch('/submit_rating', {
                method: 'POST',
                headers: {
                   'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    product_id: ProductId,
                    rating: starRating,
                    review: review,
                    customer_id: CustomerId
                })
             })
             .then(response => response)
             .then(data => {
                alert('Review submitted successfully!');
             });
        });
    });
});

