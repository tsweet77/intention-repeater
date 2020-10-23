#!/usr/bin/python
# -*- coding: utf-8 -*-

# Intention Repeater Spiritual Chat created by Thomas Sweet
# Updated 10/17/2020 v1.1
# Requires word list from here: https://www.intentionrepeater.com/Python/word_list_2.txt
# Requires Python v3.5.3 or greater
# Lets you chat with spiritual entities who can control what "random" words come out to a certain extent.
# Run using Windows/Linux/MacOS: python3 intention_repeater_chat.py
# Intention Repeater is powered by a Servitor (20 Years / 2000+ hours in the making)
# Servitor Info: https://enlightenedstates.com/2017/04/07/servitor-just-powerful-spiritual-tool/
# Website: https://www.intentionrepeater.com/
# Forum: https://forums.intentionrepeater.com/
# Licensed under GNU General Public License v3.0
# This means you can modify, redistribute and even sell your own modified software, as long as it's open source too and released under this same license.
# https://choosealicense.com/licenses/gpl-3.0/

import time
import sys
import random

# The higher this number, the more processing it does and allows spirits to work better,
# but can be slow when 50000 or more.
think_depth = 30000

# Number of words you want to allow them to say up to in each response.
max_words_response = 6

# Filename of the text file with the word list.
wordlist_file_name = 'word_list_2.txt'

def most_frequent(List):
    return max(set(List), key=List.count)


def randomize(x):
    random.seed(a=None, version=2)
    rand1 = random.randrange(0, 1E6)
    random.seed(a=random_seed, version=2)
    rand2 = random.randrange(0, 1E6)
    random.seed(a=rand1 * rand2, version=2)


sys.stdout.write('Intention Repeater Spiritual Chat v1.1 software created by Thomas Sweet.\n')
sys.stdout.write('This software comes with no guarantees or warranty of any kind.\n')
sys.stdout.write('Press Ctrl-C to quit.\n\n')

process_query = []

query = ''
query_value = ''
benchmark = 0

random_seed = ''

word_list = open(wordlist_file_name).readlines()
num_words = len(word_list)

selected_words = []

while random_seed == '':
    random_seed = int(input('Please provide a random number: '))

while query == '':
    query = input('Query: ')

# We want to cancel negative intentions. Regulate energy so that it doesn't get overpowering.
# Choose the most effective and efficient path. And conclude with it is done on each iteration.

process_energy_statement = \
    'ONE INFINITE CREATOR. INTELLIGENT INFINITY. INFINITE ENERGY. INTELLIGENT ENERGY. LOGOS. HR 6819. BY GRACE. IN COOPERATION WITH FATHER GOD, MOTHER GODDESS, AND SOURCE. PURE ADAMANTINE PARTICLES OF LOVE/LIGHT. IN THE HIGHEST AND GREATEST GOOD OF ALL, REQUESTING AID FROM ALL BEINGS WHO ARE WILLING TO ASSIST. METATRONS CUBE. 0010110. GREAT CENTRAL SUN. SIRIUS A. SIRIUS B. SOL. ALL AVAILABLE BENEFICIAL ENERGY GRIDS OF EARTH/GAIA FOCUSED THROUGH CRYSTAL GRID OF EARTH/GAIA. NODES AND NULLS OF EARTH/GAIA. CREATE STABILIZATION FIELD. CREATE ZONE OF MANIFESTATION. ALL AVAILABLE ORGONE AETHER RESONATORS. ALL AVAILABLE ORGONE BUBBLES. USE EVERY AVAILABLE RESOURCE (RESPECTING FREE WILL). MANIFEST ASAP AT HIGHEST DENSITY POSSIBLE INTO BEST DENSITY FOR USER. CREATE STRUCTURE. 963HZ GOD FREQUENCY. 432HZ MANIFESTATION. CANCEL DESTRUCTIVE OR FEARFUL INTENTIONS. PURIFY THE ENERGY. CLEAR THE BLOCKAGES. REGULATE AND BALANCE THE ENERGY. USE THE MOST EFFECTIVE PATH IN THE MOST EFFICIENT WAY. FULLY OPTIMIZE THE ENERGY. INTEGRATE THE ENERGY. PROCESS THE CHANGES. GUIDED BY MY HIGHER SELF. GROUNDED TO GAIA, CONNECTED TO SOURCE, INTEGRATING BOTH WITHIN THE SACRED HEART. SEND ALL SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRED MANIFESTATIONS, OR BETTER. PLEASE HELP USER TO RAISE THEIR VIBRATION TO THE LEVEL REQUIRED TO MAKE THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES MANIFEST. IF THE USER IS UNABLE TO ACHIEVE THE NECESSARY VIBRATION TO MANIFEST THEIR SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, BUT THERE ARE BEINGS WHO COULD AND THEY ARE WILLING TO ASSIST IN MANIFESTING THE SPECIFIED INTENTIONS, AFFIRMATIONS, AND/OR DESIRES, PLEASE ENLIST THEIR AID. IT IS DONE. SO SHALL IT BE. NOW RETURN A PORTION OF THE LOVE/LIGHT RECEIVED AND ACTIVATED BACK INTO THE HIGHER REALMS OF CREATION. I LOVE YOU AND THANK YOU. GUT/HEART/MIND COHERENCE WITH REPEATER. CLEAR INTERFERENCE. FOCUS DOWN FROM AKASHIC RECORDS. SUPERCOOLED MOST PERFECTLY BALANCED, PURIST AND MOST POWERFUL QUASAR. OM'

query_value = query + ' ' + process_energy_statement

wordval = ''
response_value = ''
num_writes = 0

try:
    while True:
        randomize(0)
        num_words_response = random.randint(1, max_words_response)

        while query == '':
            query = input('Query: ')

        query_value = query + ' ' + process_energy_statement

        divisor = (num_words_response * think_depth)
        start_time = float(time.time())
        for c in range(1, num_words_response + 1):
            for d in range(1, think_depth + 1):
                progress = num_writes / divisor * 100
                if round(progress, 1) == round(progress,2):
                    percentage = round(progress, 3)
                    sys.stdout.write('\r[' + str(percentage) + '%] PROCESSING QUERY     \r')
                process_query.append(query_value)
                randomize(0)
                r = random.randint(0, num_words - 1)
                wordval = word_list[r]
                selected_words.append(wordval)
                num_writes += 1
            sys.stdout.write('\r[' + str(percentage) + '%] FINDING WORD #' + str(c) + '/' + str(num_words_response) + '     \r')
            response_value += str(most_frequent(selected_words).rstrip()) + ' '
            selected_words.clear()
            process_query.clear()

        sys.stdout.write('\n[100%] ' + 'Response: ' + response_value + '\n')
        response_value = ''
        query = ''
except KeyboardInterrupt:

    pass
