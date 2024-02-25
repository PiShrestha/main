// script.js
const selectedOptionsList = document.getElementById('selectedOptions');

function filterOptions(value) {
    const optionsList = document.getElementById('optionsList');
    const options = optionsList.getElementsByTagName('option');
    let otherOption = optionsList.querySelector('option[value="Other"]');

    for (let option of options) {
        if (option.value.toLowerCase().includes(value.toLowerCase()) || value.toLowerCase() === "other") {
            option.style.display = 'block';
        } else {
            option.style.display = 'none';
        }
    }

    if (value.toLowerCase() === "other") {
        otherOption.style.display = 'block';
    } else {
        otherOption.style.display = 'none';
    }
}

document.getElementById('searchInput').addEventListener('change', function (event) {
    addToSelectedList(event.target.value);
});

document.getElementById('searchInput').addEventListener('blur', function (event) {
    if (event.target.value.toLowerCase() === "other") {
        let customValue = prompt("Enter your custom value:");
        if (customValue) {
            addToSelectedList(customValue);
        }
    }
});

function addToSelectedList(value) {
    if (!selectedOptionsList.querySelector(`li[data-value="${value}"]`)) {
        let listItem = document.createElement('li');
        listItem.textContent = value;
        listItem.setAttribute('data-value', value);

        listItem.addEventListener('click', function () {
            listItem.remove();
        });
        selectedOptionsList.appendChild(listItem);
    }
}

let video = document.querySelector("#videoElement")
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true }).then(function (stream) {
        track = stream.getTracks()[0];
        video.srcObject = stream;
    }).catch(function (error) {
        console.error("Something is wrong", error)
    });
} else {
    console.log("User media not supported")
}
