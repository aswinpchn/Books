var view = {
    displayMessage: function(msg) {
        var messageArea = document.getElementById("messageArea");
        messageArea.innerHTML = msg;
    },
    displayHit: function(location) {
        var cell = document.getElementById(location);
        cell.setAttribute("class", "hit");
    },
    displayMiss: function(location) {
        var cell = document.getElementById(location);
        cell.setAttribute("class", "miss");
    }
};

var model = {
    boardSize: 7,
    numShips: 3,
    shipLength: 3,
    shipsSunk: 0,
    /*ships: [{ locations: ["06", "16", "26"], hits: ["", "", ""] },
        { locations: ["24", "34", "44"], hits: ["", "", ""] },
        { locations: ["10", "11", "12"], hits: ["", "", ""] }],*/
    ships: [{ locations: ["", "", ""], hits: ["", "", ""] },
        { locations: ["", "", ""], hits: ["", "", ""] },
        { locations: ["", "", ""], hits: ["", "", ""] }],
    fire: function(guess) {
        for (var i = 0; i < this.numShips; i++) {
            var ship = this.ships[i];
            var index = ship.locations.indexOf(guess);
            if (index >= 0) {
                ship.hits[index] = "hit";
                view.displayHit(guess);
                view.displayMessage("HIT!");
                if (this.isSunk(ship)) {
                    this.shipsSunk++;
                    view.displayMessage("You sank my battleship!");
                }
                return true;
            }
        }
        view.displayMiss(guess);
        view.displayMessage("You missed.");
        return false;
    },
    isSunk: function(ship) {
        for (var i = 0; i < this.shipLength; i++) {
            if (ship.hits[i] !== "hit") {
                return false;
            }
        }
        return true;
    },
    generateAllShips: function() {
        for(var i = 0; i < this.numShips; i++) {
            do {
                var temp = this.generateShip();
                console.log(temp);
                if(this.isColliding(temp)) {
                }
                else {
                    this.ships[i].locations = temp;
                    break;  
                }
            }while(1)
        }
    },
    generateShip: function() {
        var direction = Math.floor(2 * Math.random());
        var temp = [];
        var x,y;
        if(direction == 0) {     // horziontal
            x = Math.floor((this.boardSize)*Math.random());
            y = Math.floor((this.boardSize-this.shipLength)*Math.random());
            
            temp.push(x + "" + y, (x+1) + "" + y, (x+2) + "" + y);
        }
        else if(direction == 1) {      // vertical
            x = Math.floor((this.boardSize-this.shipLength)*Math.random());
            y = Math.floor((this.boardSize)*Math.random());

            temp.push(x + "" + y, x + "" + (y+1), x + "" + (y+2));
        }

        return temp;
    },
    isColliding: function (temp) {
        var colliding = false;
        for(var i = 0 ; i < temp.length; i++) {
            for(var j = 0; j < this.ships.length; j++) {
                for(var k = 0; k < this.ships[j].locations.length; k++) {
                    if(temp[i].localeCompare(this.ships[j].locations[k]) == 0) {
                        colliding = true;    
                    }
                }
            }
        }
        
        return colliding;
    }
};

var controller = {
    guesses: 0,
    
    processGuess: function(guess) {
        var location = parseGuess(guess);
        if (location) {
            this.guesses++;
            var hit = model.fire(location);
            if (hit && model.shipsSunk === model.numShips) {
                view.displayMessage("You sank all my battleships, in " + this.guesses + " guesses");
            }
        } 
    }
};

function parseGuess(guess) {
    var alphabet = ["A", "B", "C", "D", "E", "F", "G"];
    if (guess === null || guess.length !== 2) {
        alert("Oops, please enter a letter and a number on the board.");
    } else {
        firstChar = guess.charAt(0);
        var row = alphabet.indexOf(firstChar);
        var column = guess.charAt(1);
        if (isNaN(row) || isNaN(column)) {
            alert("Oops, that isn't on the board.");
        } else if (row < 0 || row >= model.boardSize || column < 0 || column >= model.boardSize) {
            alert("Oops, that's off the board!");
        } else {
            return row + column;
        }
    }
    return null;
}

function init() {
    var fireButton = document.getElementById("fireButton");
    fireButton.onclick = handleFireButton;

    var guessInput = document.getElementById("guessInput");
    guessInput.onkeypress = handleKeyPress;

    model.generateAllShips();
}
function handleFireButton() {
    var guessInput = document.getElementById("guessInput");
    var guess = guessInput.value;
    controller.processGuess(guess);
    guessInput.value = "";
}
function handleKeyPress(e) {
    var fireButton = document.getElementById("fireButton");
    if (e.keyCode === 13) {
        fireButton.click();
        return false;
    }
}
window.onload = init;

// console.log(parseGuess("A0"));
// model.fire("53");
// model.fire("06");
// model.fire("16");
// model.fire("26");
// model.fire("34");
// model.fire("24");
// model.fire("44");
// model.fire("12");
// model.fire("11");
// model.fire("10");
//controller.processGuess("A0");