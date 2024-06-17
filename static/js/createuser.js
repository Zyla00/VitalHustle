function handleFormSubmit(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirm-password').value;

    if (password !== confirmPassword) {
        alert('Passwords do not match');
        return;
    }

    // Mockup for user creation
    alert(`User created:\nUsername: ${username}\nEmail: ${email}`);
}

function initializeForm() {
    const form = document.getElementById('create-user-form');
    form.addEventListener('submit', handleFormSubmit);
}

document.addEventListener('DOMContentLoaded', initializeForm);

// Function to disable form submissions if there are invalid fields
function initializeFormValidation() {
    'use strict';

    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation');

    // Loop over them and prevent submission
    Array.prototype.slice.call(forms).forEach((form) => {
        form.addEventListener('submit', (event) => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
}

// Initialize validation when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initializeFormValidation);
