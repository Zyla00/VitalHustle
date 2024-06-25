function initializeAddDayTrigger() {
    const addDayButton = document.getElementById('addDayButton');
    if (addDayButton) {
        addDayButton.addEventListener('click', function (event) {
            event.preventDefault();
            handleAddDay();
        });
    }
}

function handleAddDay() {
    const offcanvasBody = document.getElementById('offcanvasElement').querySelector('.offcanvas-body');
    const offcanvasTitle = document.getElementById('offcanvasElementLabel');
    const offcanvas = new bootstrap.Offcanvas(document.getElementById('offcanvasElement'));

    offcanvasTitle.textContent = 'Add a new Day';
    fetchAddDayForm(function (htmlForm) {
        displayFormInOffcanvas(htmlForm, offcanvasBody, offcanvas);
        attachAddDayListener();
        initializeSelect2();
        const formElement = document.querySelector('form');
        const datepickerId = formElement.getAttribute('data-datepicker-id');
        initializeDatepicker(datepickerId);
    });
}

function fetchAddDayForm(callback) {
    const formEndpoint = '/day/create/';

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

function attachAddDayListener() {
    const addDayButton = document.querySelector('.add-edit-day-btn');
    if (addDayButton) {
        addDayButton.addEventListener('click', function (event) {
            event.preventDefault();
            applyAddDayData();
        });
    }
}

function applyAddDayData() {
    const csrftoken = getCookie('csrftoken');
    const form = new FormData(document.getElementById('day-form'));

    fetch('/day/create/', {
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
                window.alertManager.success('New day added successfully!');
                hideOffcanvas();
                addNewDayToDOM(data.day);
            } else {
                Object.keys(data.errors).forEach(field => {
                    const cleanField = field.replace('__all__', '');
                    const message = cleanField ? `${cleanField}: ${data.errors[field].join(', ')}` : `${data.errors[field].join(', ')}`;
                    window.alertManager.error(message);
                });
            }
        })
        .catch(error => {
            window.alertManager.error('Unexpected issue. Try again later!');
        });
}

function initializeSelect2() {
    const options = {
        theme: "bootstrap-5",
        width: '100%',
        placeholder: 'Select an option',
        closeOnSelect: false
    };

    const options2 = {
        theme: "bootstrap-5",
        width: '100%',
        placeholder: 'Select an option',
        closeOnSelect: true
    };

    $('#id_emotions').select2(options);
    $('#id_cigarette_type').select2(options2);
    $('#id_alcohol_type').select2(options);
    $('#id_exercise_type').select2(options);
}

function initializeDatepicker(datepickerId) {
    const dateInput = document.getElementById(datepickerId);
    if (dateInput) {
        flatpickr(dateInput, {
            dateFormat: 'd-m-Y',
            allowInput: true,
            defaultDate: new Date(),
            maxDate: new Date(),
            altInput: true,
            altFormat: "F j, Y",
        });
    }
}


function addNewDayToDOM(day) {
    const container = document.querySelector('.container .row');
    const days = Array.from(container.querySelectorAll('.col'));
    const maxItems = 12; // Adjust based on your pagination settings

    const newDayElement = createDayElement(day);
    const deleteButton = newDayElement.querySelector('.delete-button');
    const editButton = newDayElement.querySelector('.edit-button');
    bindDeleteEvent(deleteButton);
    bindEditEvent(editButton);

    const dayDate = new Date(day.date.split('-').reverse().join('-'));

    let inserted = false;
    for (let i = 0; i < days.length; i++) {
        const dayElement = days[i];
        const dateText = dayElement.querySelector('h2 strong').nextSibling.textContent.trim();
        const currentDate = new Date(dateText.split('-').reverse().join('-'));

        if (dayDate > currentDate) {
            container.insertBefore(newDayElement, dayElement);
            inserted = true;
            break;
        }
    }

    if (!inserted && days.length < maxItems) {
        container.appendChild(newDayElement);
    }

    const updatedDays = container.querySelectorAll('.col');

    if (updatedDays.length > maxItems) {
        container.removeChild(updatedDays[updatedDays.length - 1]);
    }
}

function createDayElement(day) {
    const newDayElement = document.createElement('div');
    const staticBaseUrl = document.body.getAttribute('data-static-base-url');
    const DeleteIconUrl = staticBaseUrl + 'img/delete_icon.svg';
    const EditIconUrl = staticBaseUrl + 'img/edit_icon.svg';
    newDayElement.classList.add('col', 'd-flex', 'flex-column');
    newDayElement.setAttribute('data-day-id', day.id);

    const formattedDate = formatDate(day.date);

    newDayElement.innerHTML = `
        <div class="tile flex-grow-1 d-flex flex-column">
            <div class="right-align mb-2">
                <button class="edit-button" data-day-id="${day.id}">
                    <img src="${EditIconUrl}" alt="Edit">
                </button>
                <button class="delete-button" data-day-id="${day.id}">
                    <img src="${DeleteIconUrl}" alt="Delete">
                </button>
            </div>
            <h2><strong>Date:</strong> ${formattedDate}</h2>
            <hr>
            ${day.mood_scale !== null ? `<h3 class="mood-scale"><strong>Mood:</strong> ${day.mood_scale}</h3>` : ''}
            ${day.emotions && day.emotions.length > 0 ? `
            <div class="emotions mb-2">
                <strong>Emotions:</strong>
                ${day.emotions.map(emotion => `<span class="badge bg-primary">${emotion}</span>`).join(' ')}
            </div>` : ''}
            ${day.note ? `<div class="note mb-2"><strong>Note:</strong> ${day.note}</div>` : ''}
            ${day.slept_scale !== null ? `<h3 class="sleep-scale"><strong>Sleep:</strong> ${day.slept_scale}h</h3>` : ''}
            <hr>
            ${day.coffee_amount !== null ? `<div class="coffee-habit"><h5><strong>Coffee:</strong> ${day.coffee_amount} ${day.coffee_unit}</h5></div><hr>` : ''}
            ${day.cigarettes !== null && day.cigarettes !== 0 ? `<div class="cigarette-habit"><h5><strong>Cigarettes:</strong> ${day.cigarettes} ${day.cigarette_type}</h5></div><hr>` : ''}
            ${day.alcohol_amount !== null && day.alcohol_amount !== 0 ? `
            <div class="alcohol-habit">
                <h5><strong>Alcohol:</strong> ${day.alcohol_amount} ${day.alcohol_unit}</h5>
                ${day.alcohol_type && day.alcohol_type.length > 0 ? `
                <div class="mb-2">
                    <strong>Type:</strong>
                    ${day.alcohol_type.map(alcohol => `<span class="badge bg-secondary">${alcohol}</span>`).join(' ')}
                </div>` : ''}
            </div>
            <hr>` : ''}
            ${day.exercise_times !== null || (day.exercise_type && day.exercise_type.length > 0) ? `
            <div class="exercise-details">
                ${day.exercise_times !== null ? `<h5><strong>Exercise:</strong> ${day.exercise_times} ${day.exercise_unit}</h5>` : ''}
                ${day.exercise_type && day.exercise_type.length > 0 ? `
                <div class="mb-2">
                    <strong>Type:</strong>
                    ${day.exercise_type.map(exercise => `<span class="badge bg-success">${exercise}</span>`).join(' ')}
                </div>` : ''}
            </div>` : ''}
        </div>
    `;

    return newDayElement;
}

function setupDeleteButtons() {
    document.querySelectorAll('.delete-button').forEach(button => {
        bindDeleteEvent(button);
    });
}

function bindDeleteEvent(button) {
    button.addEventListener('click', function () {
        const dayId = this.dataset.dayId;

        document.getElementById('modalElementTitle').textContent = 'Confirm day deletion';
        document.getElementById('modalElementBody').innerHTML = 'Are you sure you want to delete this day?';
        const modalFooter = document.getElementById('modalElementFooter');
        modalFooter.innerHTML = `
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
            <button type="button" class="btn btn-danger" id="confirmDelete">Delete</button>
        `;

        let deleteModal = new bootstrap.Modal(document.getElementById('modalElement'), {
            keyboard: false
        });
        deleteModal.show();

        document.getElementById('confirmDelete').onclick = function () {
            fetch(`/day/delete/${dayId}`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({'id': dayId})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    button.closest('.col').remove();
                    fetchPreviousDay();
                    deleteModal.hide();
                    window.alertManager.success('Day deleted successfully!');
                } else {
                    deleteModal.hide();
                    window.alertManager.error(data.error);
                }
            })
            .catch(error => {
                deleteModal.hide();
                window.alertManager.error('Unexpected issue. Try again later!');
            });
        };
    });
}

function fetchPreviousDay() {
    const lastDayElement = document.querySelector('.container .row .col:last-child');
    const lastDate = lastDayElement ? lastDayElement.querySelector('h2 strong').nextSibling.textContent.trim() : null;

    if (lastDate) {
        fetch(`/day/previous/?last_date=${lastDate}`, {
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            },
        })
            .then(response => {
                if (!response.ok) throw new Error('Failed to fetch the next day.');
                return response.json();
            })
            .then(data => {
                if (data.day) {
                    const container = document.querySelector('.container .row');
                    const newDayElement = createDayElement(data.day);
                    container.appendChild(newDayElement);
                    const deleteButton = newDayElement.querySelector('.delete-button');
                    const editButton = newDayElement.querySelector('.edit-button');
                    console.log('editButton ', editButton)
                    bindDeleteEvent(deleteButton);
                    bindEditEvent(editButton);
                }
            })
    }
}

function formatDate(dateStr) {
    const months = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"];

    const parts = dateStr.split('-');
    const day = parseInt(parts[0], 10);
    const month = parseInt(parts[1], 10) - 1;
    const year = parseInt(parts[2], 10);

    const date = new Date(year, month, day);

    return `${months[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}`;
}

function initializeEditButtons() {
    document.querySelectorAll('.edit-button').forEach(button => {
        bindEditEvent(button);
    });
}

function bindEditEvent(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        const dayId = this.dataset.dayId;
        console.log('dayId ', dayId);
        handleEditDay(dayId);
    });
}

function handleEditDay(dayId) {
    fetchEditDayForm(dayId, function(htmlForm) {
        const offcanvasBody = document.getElementById('offcanvasElement').querySelector('.offcanvas-body');
        const offcanvasTitle = document.getElementById('offcanvasElementLabel');
        const offcanvas = new bootstrap.Offcanvas(document.getElementById('offcanvasElement'));

        offcanvasTitle.textContent = 'Edit Day';
        displayFormInOffcanvas(htmlForm, offcanvasBody, offcanvas);
        disableDateField();
        attachEditDayListener(dayId);
        initializeFormEnvironment();
    });
}

function fetchEditDayForm(dayId, callback) {
    const formEndpoint = `/day/edit/${dayId}/`;

    fetch(formEndpoint)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.text();
        })
        .then(htmlForm => callback(htmlForm))
        .catch(error => {
            callback('<p>Error loading the form.</p>');
        });
}

function initializeFormEnvironment() {
    initializeSelect2();
    const formElement = document.querySelector('form');
    const datepickerId = formElement.getAttribute('data-datepicker-id');
    initializeDatepicker(datepickerId);
}

function applyEditDayData(dayId) {
    const csrftoken = getCookie('csrftoken');
    const form = new FormData(document.querySelector('form'));

    fetch(`/day/edit/${dayId}/`, {
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
            window.alertManager.success('Day updated successfully!');
            hideOffcanvas();
            updateDayInDOM(dayId, data.day);
        } else {
            Object.keys(data.errors).forEach(field => {
                const message = `${field}: ${data.errors[field].join(', ')}`;
                window.alertManager.error(message);
            });
        }
    })
    .catch(error => {
        console.log(error)
        window.alertManager.error('Unexpected issue. Try again later!');
    });
}

function updateDayInDOM(dayId, updatedDay) {
    const dayContainer = document.querySelector(`div[data-day-id="${dayId}"]`);
    if (dayContainer) {
        const newDayElement = createDayElement(updatedDay);
        dayContainer.innerHTML = newDayElement.innerHTML;
        const editButton = dayContainer.querySelector('.edit-button');
        const deleteButton = dayContainer.querySelector('.delete-button');
        bindEditEvent(editButton);
        bindDeleteEvent(deleteButton);
    }
}

function attachEditDayListener(dayId) {
    const editDayButtons = document.querySelectorAll('.add-edit-day-btn');
    editDayButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            applyEditDayData(dayId);
        });
    });
}

function disableDateField() {
    const dateField = document.querySelector('form input[name="date"]');
    if (dateField) {
        dateField.setAttribute('disabled', 'disabled');
    }
}
