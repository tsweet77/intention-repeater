var h = 0;
var m = 0;
var s = 0;
var i = 0;
var repeats = 0;
var intent = [""];
var INTENTION_VAL = document.getElementById('intention').value + " REGULATE/INTEGRATE/OM";
var NUM_INTENTS_PER_SECOND = 10000000;

function to_start() {

    switch (document.getElementById('btn').value) {
        case 'Stop':
            window.clearInterval(tm); // stop the timer 
			var value = repeats.toLocaleString(
			  undefined, // leave undefined to use the browser's locale, or use a string like 'en-US' to override it.
			  { minimumFractionDigits: 0 }
			);
            document.getElementById('n1').innerHTML = "Intention Repeated " + value + " times.";
			repeats = 0;
			s = 0;
			m = 0;
			h = 0;
			
            document.getElementById('btn').value = 'Start';
            break;
        case 'Start':
            tm = window.setInterval('disp()', 1000);
            document.getElementById('btn').value = 'Stop';
            break;
    }
}

function disp() {
    // Format the output by adding 0 if it is single digit //
    if (s < 10) {
        var s1 = '0' + s;
    } else {
        var s1 = s;
    }
    if (m < 10) {
        var m1 = '0' + m;
    } else {
        var m1 = m;
    }
    if (h < 10) {
        var h1 = '0' + h;
    } else {
        var h1 = h;
    }
    // Display the output //
    str = h1 + ':' + m1 + ':' + s1;
    document.getElementById('n1').innerHTML = str + ' ' + document.getElementById('intention').value;

    for (i = 0; i < NUM_INTENTS_PER_SECOND; i++) {
        intent.push(INTENTION_VAL);
        repeats += 1;
    }
    intent.length = 0;

    // Calculate the stop watch // 
    if (s < 59) {
        s = s + 1;
    } else {
        s = 0;
        m = m + 1;
        if (m == 60) {
            m = 0;
            h = h + 1;
        } // end if  m ==60
    } // end if else s < 59
    // end of calculation for next display

}
