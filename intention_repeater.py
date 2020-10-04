#!/usr/bin/python
# -*- coding: utf-8 -*-
# Intention Repeater created by Thomas Sweet
# Updated 10/4/2020 v6.4
# Requires Python v3.5.3 or greater
# Repeats intention a million or more times per second, depending on the intensity chosen and the hardware capability.
# Usage instructions: https://www.intentionrepeater.com/usage.html
# Run using Windows: intention_repeater.py
# Run using Linux: python3 intention_repeater.py
# Automated Example Linux: python3 intention_repeater.py YYYN8 "HH:MM:SS" "Intentions/Filename with Intentions"
# Automated Example Windows: intention_repeater.py YYYN8 "HH:MM:SS" "Intentions/Filename with Intentions"
# Intention Repeater is powered by a Servitor (20 Years / 2000+ hours in the making)
# Servitor Info: https://enlightenedstates.com/2017/04/07/servitor-just-powerful-spiritual-tool/
# Website: https://www.intentionrepeater.com/
# Forum: https://forums.intentionrepeater.com/
# Licensed under GNU General Public License v3.0
# This means you can modify, redistribute and even sell your own modified software, as long as it's open source too and released under this same license.
# https://choosealicense.com/licenses/gpl-3.0/

import time
from math import ceil, log10
import sys


def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), [
        '',
        'K',
        'M',
        'B',
        'T',
        'Q',
        ][magnitude])


print("Intention Repeater v6.4 software created by Thomas Sweet.\n'")
print("This software comes with no guarantees or warranty of any kind.\n")

args = list(sys.argv)

try:
    params = str.upper(args[1])
    gutheartmindcoherenceparam = str.upper(params[0])
    clearinterferenceparam = params[1]
    akashicrecordsparam = params[2]
    quasarparam = params[3]
    intensityparam = params[4]
    runtimeparam = str(args[2])
    intentparam = str(args[3])
except:
    params = ''
    gutheartmindcoherenceparam = ''
    clearinterferenceparam = ''
    akashicrecordsparam = ''
    quasarparam = ''
    intensityparam = ''
    runtimeparam = ''
    intentparam = ''

list_write = []

intention = ''
intentionval = ''
coherence = ''
clear_interference = ''
akashic_records = ''
quasar = ''

if intentparam == '':
    while intention == '':
        intention = input('What is your intent?: ')
else:
    intention = intentparam

if gutheartmindcoherenceparam == '':
    while coherence != 'Y' and coherence != 'N':
        coherence = \
            str.upper(input('Gut/Heart/Mind Coherence? [Stronger, but can be exhausting] (Y/N): '
                      ))
else:
    coherence = gutheartmindcoherenceparam

if clearinterferenceparam == '':
    while clear_interference != 'Y' and clear_interference != 'N':
        clear_interference = \
            str.upper(input('Clear Interference? [More effective, but can be exhausting] (Y/N): '
                      ))
else:
    clear_interference = clearinterferenceparam

if akashicrecordsparam == '':
    while akashic_records != 'Y' and akashic_records != 'N':
        akashic_records = \
            str.upper(input('Use Akashic Records? [Very expansive, but may be hard to focus down] (Y/N): '
                      ))
else:
    akashic_records = akashicrecordsparam

if quasarparam == '':
    while quasar != 'Y' and quasar != 'N':
        quasar = \
            str.upper(input('Use Quasar? [Powerful energy source, but can be exhausting] (Y/N): '
                      ))
else:
    quasar = quasarparam

if coherence != 'Y' and coherence != 'N':
    coherence = 'Y'

if clear_interference != 'Y' and clear_interference != 'N':
    clear_interference = 'Y'

if akashic_records != 'Y' and akashic_records != 'N':
    akashic_records = 'Y'

if quasar != 'Y' and quasar != 'N':
    quasar = 'N'

intensity = ''

# We want to cancel negative intentions. Regulate energy so that it doesn't get overpowering.
# Choose the most effective and efficient path. And conclude with it is done on each iteration.

process_energy_statement = \
    'ONE INFINITE CREATOR. INTELLIGENT INFINITY. INFINITE ENERGY. INTELLIGENT ENERGY. LOGOS. HR 6819. BY GRACE. IN COOPERATION WITH FATHER GOD, MOTHER GODDESS, AND SOURCE. PURE ADAMANTINE PARTICLES OF LOVE/LIGHT. IN THE HIGHEST AND GREATEST GOOD OF ALL, REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRONS CUBE. 0010110. GREAT CENTRAL SUN. SIRIUS A. SIRIUS B. SOL. ALL AVAILABLE BENEFICIAL ENERGY GRIDS OF EARTH/GAIA FOCUSED THROUGH CRYSTAL GRID OF EARTH/GAIA. NODES AND NULLS OF EARTH/GAIA. CREATE STABILIZATION FIELD. CREATE ZONE OF MANIFESTATION. ALL AVAILABLE ORGONE AETHER RESONATORS. ALL AVAILABLE ORGONE BUBBLES. USE EVERY AVAILABLE RESOURCE (RESPECTING FREE WILL). MANIFEST ASAP AT HIGHEST DENSITY POSSIBLE INTO BEST DENSITY FOR USER. CREATE STRUCTURE. 963HZ GOD FREQUENCY. 432HZ MANIFESTATION. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS. PURIFY THE ENERGY. CLEAR THE BLOCKAGES. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. FULLY OPTIMIZE THE ENERGY. INTEGRATE THE ENERGY. PROCESS THE CHANGES. GUIDED BY MY HIGHER SELF. GROUNDED TO GAIA, CONNECTED TO SOURCE, INTEGRATING BOTH WITHIN THE SACRED HEART. SEND ALL SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRED MANIFESTATIONS, OR BETTER. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES MANIFEST. IF THE USER IS UNABLE TO ACHIEVE THE NECESSARY VIBRATION TO MANIFEST THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, BUT THERE ARE BEINGS WHO COULD AND THEY ARE WILLING TO ASSIST IN MANIFESTING THE SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, PLEASE ENLIST THEIR AID. IT IS DONE. SO SHALL IT BE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU AND THANK YOU. '

intentionval += intention + ' ' + process_energy_statement

if coherence == 'Y':
    intentionval += 'GUT/HEART/MIND COHERENCE WITH REPEATER. '

if clear_interference == 'Y':
    intentionval += 'CLEAR INTERFERENCE. '

if akashic_records == 'Y':
    intentionval += 'FOCUS DOWN FROM AKASHIC RECORDS. '

if quasar == 'Y':
    intentionval += \
        'SUPERCOOLED MOST PERFECTLY BALANCED, PURIST AND MOST POWERFUL QUASAR. '

# This makes a huge difference as the highest vibration

intentionval += 'OM'

benchmark = 0
start_time = float(time.time())

# See how many iterations the processor can run in one second.

while float(time.time()) - start_time < 1.0:
    benchmark += 1
    list_write.append(intentionval)

list_write.clear()

# Determine how many 0's the benchmark number would equate to. Like 100k or a million or so iterations in a second.
# Add 1 for any partial million or 100k left over.

maxintensitylevel = ceil(log10(benchmark)) + 1

if intensityparam == '':
    while intensity is not int:
        try:
            intensity = int(input('Intensity [1-'
                            + str(maxintensitylevel) + ']: '))
            break
        except ValueError:
            print("Please enter a valid intensity value.")
else:
    intensity = int(intensityparam)

if intensity > maxintensitylevel:
    intensity = maxintensitylevel

if intensity < 1:
    intensity = 1

if intensity == maxintensitylevel:
    maxintensity = benchmark
else:
    maxintensity = 10 ** (intensity - 1)

num_writes = 0

print("Press CTRL-C to stop running.\n")

# Calculate how long it takes to run the number of iterations for level of intensity chosen.

start_time = float(time.time())
for d in range(maxintensity):
    list_write.append(intentionval)

# If run the last second before midnight, benchmark again.

if float(time.time() - start_time) < 0:
    list_write.clear()
    for d in range(maxintensity):
        list_write.append(intentionval)

sleeptime = 1.0 - float(time.time() - start_time)

list_write.clear()

# We write to memory a certain number of times to repeat the intention

try:
    while True:
        for d in range(maxintensity):
            list_write.append(intentionval)
            num_writes += 1
            if num_writes % maxintensity == 0:
                sys.stdout.write('  ' + time.strftime('%H:%M:%S',
                                 time.gmtime(int(num_writes
                                 / maxintensity))) + ' ['
                                 + human_format(num_writes) + '] '
                                 + intention + '   \r')
                sys.stdout.flush()
                list_write.clear()
                if runtimeparam == time.strftime('%H:%M:%S',
                        time.gmtime(int(num_writes / maxintensity))):
                    print("\nIntention repeated " \
                        + human_format(num_writes) \
                        + " times. IT IS DONE.")
                    quit()
        if sleeptime > 0:
            time.sleep(sleeptime)
except KeyboardInterrupt:

    pass

print("\nIntention repeated " + human_format(num_writes) \
    + " times. IT IS DONE.")

list_write.clear()
