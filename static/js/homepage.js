document.addEventListener('DOMContentLoaded', function() {
    // Initialize select2
    $('#multiple-select-optgroup-field-2').select2({
        theme: "bootstrap-5",
        width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
        placeholder: $(this).data('placeholder'),
        closeOnSelect: false,
    });

    $('#multiple-select-optgroup-field-3').select2({
        theme: "bootstrap-5",
        width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
        placeholder: $(this).data('placeholder'),
        closeOnSelect: false,
    });

    $('#multiple-select-optgroup-field-4').select2({
        theme: "bootstrap-5",
        width: $(this).data('width') ? $(this).data('width') : $(this).hasClass('w-100') ? '100%' : 'style',
        placeholder: $(this).data('placeholder'),
        closeOnSelect: false,
    });

    // Add highlight effect to tiles
    addHighlightEffect();

    // Initialize sliders
    initializeSlider('moodRange', 'moodRangeValue','coffeeRange');
    initializeSlider('sleepRange', 'sleepRangeValue', 'coffeeRangeValue');
});


// Function to add highlight effect to tiles
function addHighlightEffect() {
    const tiles = document.querySelectorAll('.tile');
    tiles.forEach(tile => {
        tile.addEventListener('mouseover', function() {
            this.classList.add('highlighted');
        });
        tile.addEventListener('mouseout', function() {
            this.classList.remove('highlighted');
        });
    });
}

// Function to initialize sliders
function initializeSlider(sliderId, valueId) {
    const rangeInput = document.getElementById(sliderId);
    const rangeValue = document.getElementById(valueId);
    rangeInput.addEventListener('input', function() {
        updateValue(rangeInput, rangeValue);
    });
    updateValue(rangeInput, rangeValue); // Initialize position on page load
}

// Function to update the value displayed below the slider
function updateValue(rangeInput, rangeValue) {
    const value = rangeInput.value;
    rangeValue.textContent = value;

    // Calculate the position of the range value
    const rangeWidth = rangeInput.offsetWidth;
    const thumbWidth = 20; // Same as the thumb width in CSS
    const offset = ((value - rangeInput.min) / (rangeInput.max - rangeInput.min)) * (rangeWidth - thumbWidth);
    rangeValue.style.left = `${offset + thumbWidth / 1}px`;

    // Call the functions to update the slider color and background
    updateSliderColor(rangeInput, offset + thumbWidth / 2);
    updateSliderBackground(rangeInput);
}

// Function to update the color of the slider
function updateSliderColor(rangeInput, width) {
    rangeInput.style.setProperty('--slider-before-width', `${width}px`);
}

// Function to update the background of the slider based on its value
function updateSliderBackground(rangeInput) {
    const value = rangeInput.value;
    const max = rangeInput.max;
    const percentage = (value / max) * 100;

let color;
if (percentage < 50) {
    const r = 245 + ((0 - 245) * (percentage / 50)); // Increase red value for lighter color
    const g = 250 + ((123 - 250) * (percentage / 50)); // Increase green value for lighter color
    const b = 255 + ((255 - 255) * (percentage / 50)); // Maintain blue value for lighter color
    color = `rgb(${r}, ${g}, ${b})`; // Interpolate between a lighter color and #007bff
} else {
    const r = 0 + ((0 - 0) * ((percentage - 50) / 50));
    const g = 123 + ((123 - 123) * ((percentage - 50) / 50));
    const b = 255 + ((255 - 255) * ((percentage - 50) / 50));
    color = `rgb(${r}, ${g}, ${b})`; // Interpolate between #007bff and #007bff
}


    rangeInput.style.setProperty('--slider-before-color', color);
}
