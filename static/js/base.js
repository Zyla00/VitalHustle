function extractUserId() {
    const dropdownElement = document.querySelector('.dropdown-toggle');
    const userId = dropdownElement.id.split('-')[1];
    return userId;
}

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

