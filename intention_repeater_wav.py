#!/usr/bin/python
# -*- coding: utf-8 -*-

# Intention Repeater WAV Writer created by Thomas Sweet
# Updated 10/11/2020 v1.0
# Requires Python v3.5.3 or greater
# Run using Windows: intention_repeater_wav.py
# Run using Linux/MacOS: python3 intention_repeater_wav.py
# Automated Example Linux/MacOS: python3 intention_repeater_wav.py "HH:MM:SS" "WAV Filename" "Intentions/Filename with Intentions"
# Automated Example Windows: intention_repeater_wav.py "HH:MM:SS" "WAV Filename" "Intentions/Filename with Intentions"
# Intention Repeater is powered by a Servitor (20 Years / 2000+ hours in the making)
# Servitor Info: https://enlightenedstates.com/2017/04/07/servitor-just-powerful-spiritual-tool/
# Website: https://www.intentionrepeater.com/
# Forum: https://forums.intentionrepeater.com/
# Licensed under GNU General Public License v3.0
# This means you can modify, redistribute and even sell your own modified software, as long as it's open source too and released under this same license.
# https://choosealicense.com/licenses/gpl-3.0/
# Note, 5 seconds of running can produce an 8 MB file.

import time
import sys
import wave
import struct


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


print("Intention Repeater WAV Writer v1.0 software created by Thomas Sweet.\n")
print("This software comes with no guarantees or warranty of any kind.\n")

args = list(sys.argv)

try:
    runtimeparam = str(args[1])
    filenameparam = str(args[2])
    intentparam = str(args[3])
except:
    runtimeparam = ''
    intentparam = ''
    filenameparam = ''

list_write = []

intention = ''
intentionval = ''
filename = ''

if filenameparam == '':
    while filename == '':
        filename = input('Filename to Write: ')
else:
    filename = filenameparam

if intentparam == '':
    while intention == '':
        intention = input('What is your intent?: ')
else:
    intention = intentparam

# We want to cancel negative intentions. Regulate energy so that it doesn't get overpowering.
# Choose the most effective and efficient path. And conclude with it is done on each iteration.

process_energy_statement = \
    'ONE INFINITE CREATOR. INTELLIGENT INFINITY. INFINITE ENERGY. INTELLIGENT ENERGY. LOGOS. HR 6819. BY GRACE. IN COOPERATION WITH FATHER GOD, MOTHER GODDESS, AND SOURCE. PURE ADAMANTINE PARTICLES OF LOVE/LIGHT. IN THE HIGHEST AND GREATEST GOOD OF ALL, REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRONS CUBE. 0010110. GREAT CENTRAL SUN. SIRIUS A. SIRIUS B. SOL. ALL AVAILABLE BENEFICIAL ENERGY GRIDS OF EARTH/GAIA FOCUSED THROUGH CRYSTAL GRID OF EARTH/GAIA. NODES AND NULLS OF EARTH/GAIA. CREATE STABILIZATION FIELD. CREATE ZONE OF MANIFESTATION. ALL AVAILABLE ORGONE AETHER RESONATORS. ALL AVAILABLE ORGONE BUBBLES. USE EVERY AVAILABLE RESOURCE (RESPECTING FREE WILL). MANIFEST ASAP AT HIGHEST DENSITY POSSIBLE INTO BEST DENSITY FOR USER. CREATE STRUCTURE. 963HZ GOD FREQUENCY. 432HZ MANIFESTATION. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS. PURIFY THE ENERGY. CLEAR THE BLOCKAGES. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. FULLY OPTIMIZE THE ENERGY. INTEGRATE THE ENERGY. PROCESS THE CHANGES. GUIDED BY MY HIGHER SELF. GROUNDED TO GAIA, CONNECTED TO SOURCE, INTEGRATING BOTH WITHIN THE SACRED HEART. SEND ALL SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRED MANIFESTATIONS, OR BETTER. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES MANIFEST. IF THE USER IS UNABLE TO ACHIEVE THE NECESSARY VIBRATION TO MANIFEST THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, BUT THERE ARE BEINGS WHO COULD AND THEY ARE WILLING TO ASSIST IN MANIFESTING THE SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, PLEASE ENLIST THEIR AID. IT IS DONE. SO SHALL IT BE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU AND THANK YOU. GUT/HEART/MIND COHERENCE WITH REPEATER. CLEAR INTERFERENCE. FOCUS DOWN FROM AKASHIC RECORDS. SUPERCOOLED MOST PERFECTLY BALANCED, PURIST AND MOST POWERFUL QUASAR. OM'

intentionval += intention + ' ' + process_energy_statement

benchmark = 0
start_time = float(time.time())

# See how many iterations the processor can run in one second.

minval = 1000
maxval = 0

for element in intentionval:
    if ord(element) > maxval:
        maxval = ord(element)

    if ord(element) < minval:
        minval = ord(element)

widthval = maxval - minval
halfval = int(widthval / 2)
multiplier = int(32767 / widthval)

obj = wave.open('benchmark.dat', 'wb')
obj.setnchannels(1)  # mono
obj.setsampwidth(2)
obj.setframerate(48000.0)

while float(time.time()) - start_time < 1.0:
    benchmark += 1
    list_write.append(intentionval)
    for element in intentionval:
        value = ord(element) * multiplier - minval * multiplier
        data = struct.pack('<h', value)
        obj.writeframesraw(data)
obj.close()

list_write.clear()

num_writes = 0

print("Press CTRL-C to stop running.\n")

# Calculate how long it takes to run the number of iterations for level of intensity chosen.

start_time = float(time.time())
for d in range(benchmark):
    list_write.append(intentionval)

# If run the last second before midnight, benchmark again.

if float(time.time() - start_time) < 0:
    list_write.clear()
    for d in range(benchmark):
        list_write.append(intentionval)

sleeptime = 1.0 - float(time.time() - start_time)

list_write.clear()

obj = wave.open(filename, 'wb')
obj.setnchannels(1)  # mono
obj.setsampwidth(2)
obj.setframerate(48000.0)

# We write to memory a certain number of times to repeat the intention

try:
    while True:
        for d in range(benchmark):
            for element in process_energy_statement:
                value = ord(element) * multiplier - minval * multiplier
                data = struct.pack('<h', value)
                obj.writeframesraw(data)

            list_write.append(intentionval)
            num_writes += 1
            if num_writes % benchmark == 0:
                sys.stdout.write('  ' + time.strftime('%H:%M:%S',
                                 time.gmtime(int(num_writes
                                 / benchmark))) + ' ['
                                 + human_format(num_writes) + '] '
                                 + intention + '   \r')
                sys.stdout.flush()
                list_write.clear()
                if runtimeparam == time.strftime('%H:%M:%S',
                        time.gmtime(int(num_writes / benchmark))):
                    print("\nIntention repeated " \
                        + human_format(num_writes) \
                        + " times. IT IS DONE.")
                    obj.close()
                    quit()
        if sleeptime > 0:
            time.sleep(sleeptime)
except KeyboardInterrupt:

    pass

print("\nIntention repeated " + human_format(num_writes) \
    + " times. IT IS DONE.")

obj.close()

list_write.clear()
