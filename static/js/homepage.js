function addHighlightEffect() {
    const tiles = document.querySelectorAll('.tile');
    tiles.forEach(tile => {
        tile.addEventListener('mouseover', function () {
            this.classList.add('highlighted');
        });
        tile.addEventListener('mouseout', function () {
            this.classList.remove('highlighted');
        });
    });
}

function initializeFormAutoSubmit() {
    const forms = document.querySelectorAll('.form-container form');

    forms.forEach(form => {
        const saveButton = form.querySelector('button[type="submit"]');

        form.addEventListener('input', (event) => {
            if (!event.target.matches('button[type="submit"]')) {
                event.preventDefault();
                autoSubmitForm(form);
            }
        });

        if (saveButton) {
            saveButton.addEventListener('click', (event) => {
                event.preventDefault();
                autoSubmitForm(form);
            });
        }

        $(form).find('select').each(function () {
            const selectElement = $(this);
            selectElement.select2({
                theme: "bootstrap-5",
                width: selectElement.data('width') ? selectElement.data('width') : selectElement.hasClass('w-100') ? '100%' : 'style',
                placeholder: selectElement.data('placeholder'),
                closeOnSelect: false,
            }).on('change', function () {
                autoSubmitForm(form);
            });
        });
    });
}

function autoSubmitForm(form) {
    const formData = new FormData(form);
    formData.append('form_id', form.id);

    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                console.log('Form submitted successfully');
            } else {
                console.log('Form submission failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}