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
            this.toggleButton.style.left = '10px';
            this.container.style.marginLeft = '0';
        } else {
            this.toggleButton.style.left = '240px';
            this.container.style.marginLeft = '0px';
        }
    }
}

document.addEventListener('DOMContentLoaded', function() {
    new SidebarToggle('toggle-button', 'sidebar', 'content');
});

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

