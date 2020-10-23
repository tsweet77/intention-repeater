from time import sleep
import sys

print("Intention Repeater v0.3 software written by Thomas Sweet.\n")

print("Sample Intentions:")
print("My chakras are balanced.")
print("My heart chakra is balanced.")
print("I AM Universal Love.")
print("I am aligned to Source.")
print("My coffee attracts financial abundance.")
print("I attract financial abundance.")
print("My dog's water is charged with healing energy.")
print("My energy is calm and stilled.")
print("or whatever you desire or intend, as if it's already happened.")
print("Negative intentions will be cancelled.\n")

print("You can use a file if you wish to work with a lot of intentions")
print("or the story of how you want things to go.")
print("Keep similar elements grouped in one file. Use different files for different people or things.")
print("More focused intention files will be more effective. Otherwise the energy will thin out.")
print("For working on chakras or a person, start with 300-500 intensity for 5 mins, then up to 120 mins.")
print("For charging water or other drink, start with 500 intensity for up to 60 mins.")
print("For charging your dog's water like 5 gallons, use 5000 intensity for up to 60 mins.")
print("For many different intentions, start with intensity of 500 for up to 120 mins.\n")

print("If the energy gets too much, run with intent of 'pause'")
print("without the quotes at 500-1000 intensity for 10 mins.")
print("Also, 'block unnecessary energy to me' works.\n")

print("This software comes with no guarantees or warranty of any kind.\n")

intention = ''

while intention == '':
        intention = input("What is your intent? [Or filename of TXT file]: ")

intensity = ''
num_minutes = ''

while intensity is not int:
    try:
        intensity = int(input("Intensity [1-10000]: "))
        break
    except ValueError:
        print("Please enter a valid intensity value.")

while num_minutes is not int:
    try:
        num_minutes = int(input("Minutes to run: "))
        break
    except ValueError:
        print("Please enter a valid duration in minutes.")
        
if intensity > 10000:
    intensity = 10000

if intensity < 1:
    intensity = 1
    
if num_minutes < 1:
    num_minutes = 1
    
list_write = []

num_seconds = num_minutes * 60 + 1
num_writes = 0

sys.stdout.write(intention + "\n")

#We want to cancel negative intentions. Regulate energy so that it doesn't get overpowering.
#Choose the most effective and efficient path. And conclude with it is done on each iteration.
intention += " CANCEL NEGATIVE INTENTIONS. REGULATE ENERGY. USE MOST EFFICIENT PATH. IT IS DONE."

for i in range(num_seconds):
    #We write to memory a certain number of times to repeat the intention
    for d in range(intensity):
        list_write.append(intention)
        num_writes += 1
        if num_writes % 1000000 == 0:
            list_write.clear()
        
    #num_status is how many "=" signs are printed out of 20 to show progress
    num_status = int(i/(3*num_minutes))
    percent_done = int(i/(3*num_minutes)/20*100)
    sys.stdout.write('\r')
    sys.stdout.write(": [%-20s] %d%%" % ('='*num_status,percent_done))
    sys.stdout.flush()
    sleep(1)

print("\nIntention repeated " + str(num_writes) + " times. IT IS DONE.")

list_write.clear()