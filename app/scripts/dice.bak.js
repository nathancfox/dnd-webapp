const button = document.querySelector('#roll-d6');
button.addEventListener('click', updateResult);
result = document.querySelector('#d6-result');

function updateResult() {
    result.textContent = roll(6);
}

function getRandomInt(max) {
    // Returns random integer in interval [0, max)
    return Math.floor(Math.random() * max);
}

function roll(max) {
    return getRandomInt(max) + 1;
}
