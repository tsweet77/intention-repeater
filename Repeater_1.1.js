var h = 0;
var m = 0;
var s = 0;
var i = 0;
var repeats = 0;
var intent = [""];
var INTENTION_VAL = document.getElementById('intention').value + " ONE INFINITE CREATOR. REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRON'S CUBE. ALL AVAILABLE BENEFICIAL ENERGY GRIDS, ORGONE AETHER RESONATORS, & ORGONE BUBBLES. CREATE MANIFESTATION ZONE. ASCENSION PYRAMID. USE EVERY AVAILABLE RESOURCE. MANIFEST ASAP. CREATE STRUCTURE. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS, OR INTENTIONS THAT CONFLICT WITH THE HIGHEST AND GREATEST GOOD OF THE USER. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. OPTIMAL ENERGY. INTEGRATE THE ENERGY IN THE MOST EFFECTIVE AND PLEASANT WAY POSSIBLE. PROCESS THE CHANGES. GUIDED BY THE USER'S HIGHER SELF. CONNECTED TO SOURCE. ENABLE AND UTILIZE THE SACRED HEART, QUANTUM HEART, AND QUANTUM MIND. MANIFEST ALL SPECIFIED INTENTIONS AND/OR DESIRES, OR BETTER. IF IT WOULD AID IN THE MANIFESTATION PROCESS, PLEASE HELP USER TO SENSE AND EMOTIONALLY FEEL WHAT IT WOULD BE LIKE TO ALREADY BE EXPERIENCING THEIR SPECIFIED INTENTIONS AND/OR DESIRES NOW. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS AND/OR DESIRES MANIFEST. ASSIST THE USER WITH ACHIEVING OPTIMAL GUT/HEART/MIND COHERENCE WITH THEIR SPECIFIED INTENTIONS AND/OR DESIRES. IF IT WOULD BENEFIT THE USER, ASSIST THEM WITH CLEARING & RELEASING ANY/ALL INTERNAL OR EXTERNAL INTERFERENCE OR BLOCKAGES TO THEIR SPECIFIED INTENTIONS AND/OR DESIRES. IT IS DONE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU. OM.";
var NUM_INTENTS_PER_SECOND = 1000000;

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