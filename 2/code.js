var randomLoc = Math.floor(Math.random() * 5);
var location1 = randomLoc;
var location2 = randomLoc+1;
var location3 = randomLoc+2;

var current_guess;

var isSunk1 = false;
var isSunk2 = false;
var isSunk3 = false;

var tries = 0;

while(isSunk1 == false || isSunk2 == false || isSunk3 == false) {
    current_guess = prompt("Ready, aim, fire! (enter a number 0-6):");
    if (current_guess < 0 || current_guess > 6) {
        alert("Please enter a valid cell number!");
    } 
    else {
        tries = tries + 1;
        if(current_guess == location1) {
            isSunk1 = true;     
        }
        else if(current_guess == location2) {
            isSunk2 = true;
        }
        else if(current_guess == location3) {
            isSunk3 = true;
        }
    }
}
window.alert("The start location is " + randomLoc + "\nYour accuracy is" + 3/tries);

