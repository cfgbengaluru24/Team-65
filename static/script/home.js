const containers = document.querySelectorAll('.ticket-gap');
containers.forEach(container => {
    // Get the checkbox and image elements within this container
    const checkbox = container.querySelector('.checkbox');
    const image = container.querySelector('.ticket');

    // Add click event listener to the image
    image.addEventListener('click', function () {
        // Trigger a click event on the checkbox
        checkbox.click();
    });
});

window.onload = function () {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    var divElement = document.getElementById('bottom-navbar');

    function toggleDivVisibility() {
        var atLeastOneChecked = false;
        checkboxes.forEach(function (checkbox) {
            if (checkbox.checked) {
                atLeastOneChecked = true;
            }
        });

        if (atLeastOneChecked) {
            divElement.style.display = 'flex';
        } else {
            divElement.style.display = 'none';
        }
    }

    checkboxes.forEach(function (checkbox) {
        checkbox.addEventListener('change', toggleDivVisibility);
    });
    toggleDivVisibility();
};

function openForm() {
    // const bookingDateInput1 = document.getElementById('input-3');
    const bookingDateInput2 = document.getElementById('bookingDate');
    // const bookingTime = document.getElementById('startTime');
    // const bookingTime1 = document.getElementById('time');
    // const bookingTime2 = document.getElementById('endTime');
    // const bookingTime22 = document.getElementById('time2');
    //
    //
    // bookingTime.value = bookingTime1.value;
    // bookingTime2.value = bookingTime22.value;
    //
    // const dateValue = bookingDateInput1.value;
    // const date = new Date(dateValue);
    // const formattedDate = date.toISOString().split('T')[0]; // Get the date part only
    //
    // // Set the value of the second input to match the first input
    bookingDateInput2.value = moment(bookingDateInput2.value).format('dddd, MMMM Do YYYY');
}

document.addEventListener('DOMContentLoaded', function () {
    var reasonSelect = document.getElementById('reason');
    var reasonTextField = document.getElementById('reason_text');

    reasonTextField.style.display = 'none';

    reasonSelect.addEventListener('change', function () {
        var selectedOption = reasonSelect.value;
        if (selectedOption === 'OTHERS') {
            reasonTextField.style.display = 'block';
        } else {
            reasonTextField.style.display = 'none';
        }
    });
});

function validateTime() {
    var startTime = document.getElementById('time').value;
    var endTime = document.getElementById('time2').value;

    if (startTime >= endTime) {
        alert('Start time cannot be greater than or equal to end time.');
        return false;
    }
    openForm();
}

document.getElementById('popupButton').addEventListener('click', function (event) {
    // Code to display the popup
    event.preventDefault();
    event.stopPropagation();
});


document.addEventListener("DOMContentLoaded", function () {

    document.body.classList.add("loaded");
});

var backDropOverlay = document.getElementById("backDropDiv");

function toggleElementState(elementId, show, delay) {
    const element = document.getElementById(elementId);
    if (element) {
        if (!show) {
            element.classList.add('show');
            backDropOverlay.classList.add('hidden');
            setTimeout(() => {
                element.classList.add("hidden");
            }, 350);
        } else {
            element.classList.remove("hidden");
            setTimeout(() => {
                element.classList.remove('show');
                backDropOverlay.classList.remove('hidden');
            }, delay);
        }
        // bodyElement.classList.toggle('overflow-hidden', show);
        if (show) {
            openDrawerId = elementId;
            openModalId = elementId;
        } else {
            openDrawerId = null;
            openModalId = null;
        }
    }
}

const allModalButtons = document.querySelectorAll('[data-modal-target]');
const allModalCloseButtons = document.querySelectorAll('[data-modal-close]');
allModalButtons.forEach(element => {
    const modalId = element.getAttribute('data-modal-target');
    if (modalId) {
        element.addEventListener('click', function () {
            toggleElementState(modalId, true, 200);
        });
    }
});

// Attach click event listeners to modal close buttons
allModalCloseButtons.forEach(element => {
    const modalId = element.getAttribute('data-modal-close');
    if (modalId) {
        element.addEventListener('click', function () {
            toggleElementState(modalId, false, 200);
        });
    }
});

const classDictionary = {
    "B-1": {className: " sm:col-span-12 md:col-span-6 lg:col-span-3 xl:col-span-2",},
    "E-1": {className: " sm:col-span-12 md:col-span-6 lg:col-span-3 xl:col-span-3",},
    "F-1": {className: " sm:col-span-12 md:col-span-8 lg:col-span-6 xl:col-span-4",},
    "T-1": {className: " sm:col-span-12 md:col-span-4 lg:col-span-3 xl:col-span-2",},
    "SH-1": {className: " sm:col-span-6 md:col-span-3 lg:col-span-1 xl:col-span-1",},

    "G-1": {className: " sm:col-span-3 md:col-span-2 lg:col-span-1 lg:row-span-1 xl:col-span-1",},
    "D-1": {className: " sm:col-span-3 md:col-span-2 lg:col-span-1 lg:row-span-1 xl:col-span-1",},
    "LP-1": {className: " sm:col-span-12 md:col-span-5 lg:col-span-3 xl:col-span-2",},
    "LT-1": {className: " sm:col-span-12 md:col-span-12 lg:col-span-3 xl:col-span-2",},
    "L-1": {className: " sm:col-span-12 md:col-span-12 lg:col-span-12 xl:col-span-6",},
};


for (const id in classDictionary) {
    if (classDictionary.hasOwnProperty(id)) {
        const entry = classDictionary[id];
        const divElement = document.getElementById(id);
        if (divElement) {
            divElement.className = "col-span-12 card" + divElement.className + entry.className;
        }
    }
}
