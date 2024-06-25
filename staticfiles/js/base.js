class SidebarToggle {
    constructor(toggleButtonId, sidebarId, containerClass) {
        this.toggleButton = document.getElementById(toggleButtonId);
        this.sidebar = document.getElementById(sidebarId);
        this.container = document.querySelector(`.${containerClass}`);
        this.addEventListeners();
    }

    addEventListeners() {
        this.toggleButton.addEventListener('click', () => this.toggleSidebar());
    }

    toggleSidebar() {
        this.sidebar.classList.toggle('sidebar-collapsed');
        if (this.sidebar.classList.contains('sidebar-collapsed')) {
            this.toggleButton.style.left = '15px';
            this.container.classList.add('content-expanded');
        } else {
            this.toggleButton.style.left = '245px';
            this.container.classList.remove('content-expanded');
        }
    }
}


function initializeSidebarToggle() {
    new SidebarToggle('toggle-button', 'sidebar', 'content');
}

function initializeChangePasswordTrigger() {
    const changePasswordLink = document.getElementById('changePasswordLink');
    if (changePasswordLink) {
        changePasswordLink.addEventListener('click', function(event) {
            event.preventDefault();
            handleChangePassword();
        });
    }
}

function handleChangePassword() {
    const username = document.getElementById('username').textContent.trim();
    const offcanvasBody = document.getElementById('offcanvasElement').querySelector('.offcanvas-body');
    const offcanvasTitle = document.getElementById('offcanvasElementLabel');
    const offcanvas = new bootstrap.Offcanvas(document.getElementById('offcanvasElement'));

    offcanvasTitle.textContent = `Change password for User: ${username}`;
    fetchPasswordEditForm(function(htmlForm) {
        displayFormInOffcanvas(htmlForm, offcanvasBody, offcanvas);
        attachApplyListener();
    });
}

function fetchPasswordEditForm(callback) {
    const formEndpoint = '/edit-password/';

    fetch(formEndpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.text();
        })
        .then(htmlForm => {
            callback(htmlForm);
        })
        .catch(error => {
            callback('<p>Error loading the form.</p>');
        });
}

function displayFormInOffcanvas(htmlForm, offcanvasBody, offcanvas) {
    offcanvasBody.innerHTML = htmlForm;
    offcanvas.show();
}

function attachApplyListener() {
    const applyButtons = document.querySelectorAll('.user-edit-btn');
    applyButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            applyChangePasswordData();
        });
    });
}

function applyChangePasswordData() {
    const csrftoken = getCookie('csrftoken');
    const form = new FormData(document.getElementById('user-form'));

    fetch('/edit-password/', {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: form
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const username = data.username;
            window.alertManager.success(`User ${username} password updated successfully!`);
            hideOffcanvas();
        } else {
            Object.keys(data.errors).forEach(field => {
                const cleanField = field.replace('__all__', '');
                const message = cleanField ? `${cleanField}: ${data.errors[field].join(', ')}` : `${data.errors[field].join(', ')}`;
                window.alertManager.error(message);
            });
        }
    })
    .catch(error => {
        console.log(error)
        window.alertManager.error('Unexpected issue. Try again later!');
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function hideOffcanvas() {
    const offcanvasElement = document.getElementById('offcanvasElement');
    const offcanvas = bootstrap.Offcanvas.getInstance(offcanvasElement);
    offcanvas.hide();
}

function initializeSlider(sliderId, valueId) {
    const rangeInput = document.getElementById(sliderId);
    const rangeValue = document.getElementById(valueId);
    rangeInput.addEventListener('input', function () {
        updateValue(rangeInput, rangeValue);
    });
    updateValue(rangeInput, rangeValue);
}

function updateValue(rangeInput, rangeValue) {
    const value = rangeInput.value;
    rangeValue.textContent = value;

    const rangeWidth = rangeInput.offsetWidth;
    const thumbWidth = 20;
    const offset = ((value - rangeInput.min) / (rangeInput.max - rangeInput.min)) * (rangeWidth - thumbWidth);
    rangeValue.style.left = `${offset + thumbWidth / 1}px`;

    updateSliderColor(rangeInput, offset + thumbWidth / 2);
    updateSliderBackground(rangeInput);
}

function updateSliderColor(rangeInput, width) {
    rangeInput.style.setProperty('--slider-before-width', `${width}px`);
}

function updateSliderBackground(rangeInput) {
    const value = rangeInput.value;
    const max = rangeInput.max;
    const percentage = (value / max) * 100;

    let color;
    if (percentage < 50) {
        const r = 245 + ((0 - 245) * (percentage / 50));
        const g = 250 + ((123 - 250) * (percentage / 50));
        const b = 255 + ((255 - 255) * (percentage / 50));
        color = `rgb(${r}, ${g}, ${b})`;
    } else {
        const r = 0 + ((0 - 0) * ((percentage - 50) / 50));
        const g = 123 + ((123 - 123) * ((percentage - 50) / 50));
        const b = 255 + ((255 - 255) * ((percentage - 50) / 50));
        color = `rgb(${r}, ${g}, ${b})`;
    }


    rangeInput.style.setProperty('--slider-before-color', color);
}

function setupModalCleanup() {
    const modalElement = document.getElementById('modalElement');

    modalElement.addEventListener('hidden.bs.modal', function () {
        document.getElementById('modalElementTitle').textContent = '';
        document.getElementById('modalElementBody').innerHTML = '';
        document.getElementById('modalElementFooter').innerHTML = '';
    });
}