#!/usr/bin/python
# -*- coding: utf-8 -*-

# Intention Repeater WAV Converter created by Thomas Sweet
# Updated 10/26/2020 v1.0
# Requires Python v3.5.3 or greater
# Run using Windows: python intention_repeater_wav_converter.py
# Run using Linux: python3 intention_repeater_wav_converter.py
# Automated Example Linux: python3 intention_repeater_wav_converter.py "HH:MM:SS" "IN Filename" "OUT WAV Filename"
# Automated Example Windows: intention_repeater_wav.py "HH:MM:SS" "IN Filename" "OUT WAV Filename"
# Intention Repeater is powered by a Servitor (20 Years / 2000+ hours in the making)
# Servitor Info: https://web.archive.org/web/20200915191532/https://enlightenedstates.com/2017/04/07/servitor-just-powerful-spiritual-tool/
# Website: https://www.intentionrepeater.com/
# Forum: https://forums.intentionrepeater.com/
# Licensed under GNU General Public License v3.0
# This means you can modify, redistribute and even sell your own modified software, as long as it's open source too and released under this same license.
# https://choosealicense.com/licenses/gpl-3.0/
# Note, 1 minute of running can produce an approx. 55 MB file that is approx. 5m long on an i3 with 4GB RAM and a SSD.

import time
import sys
import wave
import struct

VOLUME_LEVEL = 0.500 # Volume level should be from 0.000 to 1.000.
SAMPLING_RATE = 96000.0

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

sys.stdout.write('Intention Repeater WAV Converter v1.0 software created by Thomas Sweet.\n')
sys.stdout.write('Converts and repeats any file to a 96kHz Mono WAV.\n')
sys.stdout.write('This software comes with no guarantees or warranty of any kind and is for entertainment purposes only.\n')

args = list(sys.argv)

try:
    run_time_param = str(args[1])
    in_filename_param = str(args[2])
    out_filename_param = str(args[3])
except:
    run_time_param = ''
    in_filename_param = ''
    out_filename_param = ''

string_to_write = ''
string_to_write_value = ''

peak_value = 32767
peak_value_2 = peak_value * 2

if in_filename_param == '':
    while in_filename == '':
        in_filename = input('Input Filename: ')
else:
    in_filename = in_filename_param

if out_filename_param == '':
    while out_filename == '':
        out_filename = input('Input Filename: ')
else:
    out_filename = out_filename_param

if str.lower(out_filename[-4:]) != '.wav':
    if str.lower(out_filename[-1:]) == '.':
        out_filename += 'wav'
    else:
        out_filename += '.wav'

try:
    with open(in_filename, 'rb') as file:
        string_to_write_value = file.read()
except:
    print("Error Opening File!")
    quit()

minval = peak_value_2
maxval = -peak_value_2

for element in string_to_write_value:
    if element <= minval:
        minval = element

for element in string_to_write_value:
    if element >= maxval:
        maxval = element

widthval = maxval - minval

if widthval == 0:
    print("File has no data.")
    quit()

multiplier = peak_value_2 / widthval

num_writes = 0
num_seconds = 0

print("Press CTRL-C to stop running.\n")

obj = wave.open(out_filename, 'wb')
obj.setnchannels(1)  # mono
obj.setsampwidth(2)
obj.setframerate(SAMPLING_RATE)

# We write to the WAV file repeatedly until stopped or timer is reached.
try:
    while True:
        start_time = float(time.time())
        num_seconds += 1
        while float(time.time()) - start_time < 1.00:
            for element in string_to_write_value:
                normalized_element = int((element * multiplier - peak_value) * VOLUME_LEVEL)
                value = normalized_element
                if value < -peak_value:
                    value = -peak_value
                elif value > peak_value:
                    value = peak_value
                
                data = struct.pack('<h', value)
                obj.writeframesraw(data)
            num_writes += 1
        sys.stdout.write('  ' + time.strftime('%H:%M:%S',
                         time.gmtime(num_seconds)) + ' ['
                         + human_format(num_writes) + ' Times Repeated]: '
                         + in_filename + ' -> ' + out_filename
                         + string_to_write + '   \r')
        sys.stdout.flush()
        if run_time_param == time.strftime('%H:%M:%S',
                time.gmtime(int(num_seconds))):
            sys.stdout.write('\n' + in_filename + ' Written '
                + human_format(num_writes)
                + ' Times To ' + out_filename + '.')
            obj.close()
            quit()
except KeyboardInterrupt:

    pass

sys.stdout.write('\n' + in_filename + ' Written ' + human_format(num_writes) + ' Times To ' + out_filename + '.')

obj.close()
