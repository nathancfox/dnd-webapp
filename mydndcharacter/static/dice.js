let dice = document.querySelectorAll('.die');
let dice_objs = new Map();
for (let i = 0; i < dice.length; i++) {
    new_die = new Object();
    new_die.number = dice[i].getAttribute('number');
    for (let j = 0; j < dice[i].children.length; j++) {
        if (dice[i].children[j].className === 'die-result') {
            new_die.result_id = dice[i].children[j].id;
        } else if (dice[i].children[j].className === 'die-button-container') {
            new_die.button_id = dice[i].children[j].children[0].id;
        }
    }
    dice_objs.set(dice[i].id, new_die);
}

for (let [key, value] of dice_objs) {
    button = document.querySelector('#' + value.button_id);
    // WORKS
    if (value.button_id === 'roll-d100') {
        button.addEventListener('click',
            function() {
                updateResult(value.number, value.result_id, 10);
            }
        )
    } else {
        button.addEventListener('click',
            function() {
                updateResult(value.number, value.result_id, 1);
            }
        )
    }
    // FAILS
    // if (value.button_id === 'roll-d100') {
    //     multiplier = 10;
    // } else {
    //     multiplier = 1;
    // }
    // button.addEventListener('click',
    //     function() {
    //         updateResult(value.number, value.result_id, multiplier);
    //     }
    // )
}

function updateResult(number, result_id, multiplier) {
    result = document.querySelector('#' + result_id);
    roll_result = roll(number, multiplier);
    if (multiplier == 10) {
        roll_result -= 10;
        if (roll_result == 0) {
            roll_result = "00";
        }
    }
    result.textContent = roll_result;
}

function roll(max, multiplier) {
    return (getRandomInt(max) + 1) * multiplier ;
}

function getRandomInt(max) {
    // Returns random integer in interval [0, max)
    return Math.floor(Math.random() * max);
}
