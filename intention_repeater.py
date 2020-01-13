#Intention Repeater created by Thomas Sweet
#Updated 1/12/2020
#Repeats intention a million or more times per second
#Depending on the intensity chosen and the hardware capability.
#Python script. Run using: python3 intention_repeater.py

import time
from math import ceil, log10
import sys

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T', 'P'][magnitude])

print("Intention Repeater v0.5 software created by Thomas Sweet.\n")
print("This software comes with no guarantees or warranty of any kind.\n")

list_write = []

intention = ''
intentionval = ''

while intention == '':
        intention = input("What is your intent? [Or filename of TXT file]: ")

intensity = ''

#We want to cancel negative intentions. Regulate energy so that it doesn't get overpowering.
#Choose the most effective and efficient path. And conclude with it is done on each iteration.
process_energy_statement = 'CANCEL NEGATIVE INTENTIONS. PURIFY THE ENERGY. CLEAR THE BLOCKAGES. REGULATE THE ENERGY. BALANCE THE ENERGY. USE THE MOST EFFICIENT PATH. INTEGRATE THE ENERGY. PROCESS THE CHANGES. IT IS DONE.'
intentionval += intention + ' ' + process_energy_statement

benchmark = 0
start_time = float(time.time())

#See how many iterations the processor can run in one second.
while float(time.time()) - start_time < 1.0:
    benchmark += 1
    list_write.append(intentionval)

list_write.clear()

#Determine how many 0's the benchmark number would equate to. Like 100k or a million or so iterations in a second.
#Add 1 for any partial million or 100k left over.
maxintensitylevel = ceil(log10(benchmark)) + 1

while intensity is not int:
    try:
        intensity = int(input("Intensity [1-" + str(maxintensitylevel) + "]: "))
        break
    except ValueError:
        print("Please enter a valid intensity value.")

if intensity > maxintensitylevel:
    intensity = maxintensitylevel

if intensity < 1:
    intensity = 1

if intensity == maxintensitylevel:
    maxintensity = benchmark
else:
    maxintensity = 10**(intensity-1)

num_writes = 0

print("Press CTRL-C to stop running.\n")

#Calculate how long it takes to run the number of iterations for level of intensity chosen.
start_time = float(time.time())
for d in range(maxintensity):
    list_write.append(intentionval)

#If run the last second before midnight, benchmark again.
if float(time.time() - start_time) < 0:
    list_write.clear()
    for d in range(maxintensity):
        list_write.append(intentionval)

sleeptime = 1.0 - float(time.time() - start_time)

list_write.clear()

#We write to memory a certain number of times to repeat the intention
try:
    while True:
        for d in range(maxintensity):
            list_write.append(intentionval)
            num_writes += 1
            if num_writes % maxintensity == 0:
                sys.stdout.write(time.strftime('%H:%M:%S', time.gmtime(int(num_writes/maxintensity))) + " [" + human_format(num_writes) + "] " + intention + '   \r')
                sys.stdout.flush()
                list_write.clear()
        if sleeptime > 0:
            time.sleep(sleeptime)

except KeyboardInterrupt:
    pass

print("\nIntention repeated " + human_format(num_writes) + " times. IT IS DONE.")

list_write.clear()