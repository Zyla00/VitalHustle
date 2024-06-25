function initializeFormListener() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        submitForm(form);
    });
}

function submitForm(form) {
    const formData = new FormData(form);
    const url = form.action;

    fetch(url, {
        method: 'POST',
        body: formData,
        credentials: 'same-origin',
        headers: {
            'X-CSRFToken': formData.get('csrfmiddlewaretoken')
        }
    })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                Object.keys(data.errors).forEach(field => {
                    const cleanField = field.replace('__all__', '');
                    const message = cleanField ? `${cleanField}: ${data.errors[field].join(', ')}` : `${data.errors[field].join(', ')}`;
                    window.alertManager.error(message);
                });
            } else {
                window.location.href = data.redirect_url || '/';
            }
        })
        .catch(error => {
            window.alertManager.error('Unexpected issue. Try again later!');
        });
}