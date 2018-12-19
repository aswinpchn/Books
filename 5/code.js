var fiat = {
    make: "Fiat",
    model: "500",
    year: 1957,
    color: "Medium Blue",
    passengers: 2,
    convertible: false,
    mileage: 88000,
    started: false,
    start: function() {
        this.started = true;                      // Whenever we are using another property within an object, we have to use This. to intimate to the js compiler.
    },
    stop: function() {
        this.started = false;
    },
    drive: function() {
        if (this.started) {
            alert("Zoom zoom!");
        } else {
            alert("You need to start the engine first.");
        }
    }
};

fiat.drive();    // This will say that you haven't started the engine.   // If we use started without this, It will say started is not defined.

/*fiat.start();        // This will work.
fiat.drive();
fiat.stop(); */

for(var prop in fiat) {    // prop is a string
    console.log(prop + "\t" + fiat[prop] + "\n");     // fiat.prop will not work as prop is a string.  [] is an alternate way to access property ["string"]
}