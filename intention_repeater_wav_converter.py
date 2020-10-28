#!/usr/bin/python
# -*- coding: utf-8 -*-

# Intention Repeater WAV Converter created by Thomas Sweet
# Updated 10/26/2020 v1.2
# Requires Python v3.5.3 or greater
# Run using Windows: python intention_repeater_wav_converter.py
# Run using Linux: python3 intention_repeater_wav_converter.py
# Automated Example Linux: python3 intention_repeater_wav_converter.py "HH:MM:SS" "IN Filename" "OUT WAV Filename"
# Automated Example Windows: intention_repeater_wav.py "HH:MM:SS" "IN Filename" "OUT WAV Filename"
# The HH:MM:SS determines how long you want your WAV file to be.
# Intention Repeater is powered by a Servitor (20 Years / 2000+ hours in the making)
# Servitor Info: https://web.archive.org/web/20200915191532/https://enlightenedstates.com/2017/04/07/servitor-just-powerful-spiritual-tool/
# Website: https://www.intentionrepeater.com/
# Forum: https://forums.intentionrepeater.com/
# Licensed under GNU General Public License v3.0
# This means you can modify, redistribute and even sell your own modified software, as long as it's open source too and released under this same license.
# https://choosealicense.com/licenses/gpl-3.0/

import time
import sys
import wave
import struct

VOLUME_LEVEL = 0.950 # Volume level should be from 0.000 to 1.000. Set at 95% to prevent possible clipping.
SAMPLING_RATE = 96000.0 #Hz.

def human_format(num):
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), [
        '',
        'k',
        'M',
        'B',
        'T',
        'Q',
        ][magnitude])
        
def getTimeFromSeconds(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%02d:%02d:%02d" % (hour, minutes, seconds)

sys.stdout.write('Intention Repeater WAV Converter v1.2 software created by Thomas Sweet.\n')
sys.stdout.write('Converts and repeats any file to a 96kHz Mono WAV.\n')
sys.stdout.write('This software comes with no guarantees or warranty of any kind and is for entertainment purposes only.\n\n')

args = list(sys.argv)

try:
    duration_param = str(args[1])
    in_filename_param = str(args[2])
    out_filename_param = str(args[3])
except:
    duration_param = 'Until Stopped'
    in_filename_param = ''
    out_filename_param = ''

string_to_write = ''
string_to_write_value = ''
in_filename = ''
out_filename = ''
duration_sec = '00'
duration_minutes = '00'
duration_hours = '00'

#Find number of seconds is in the provided duration of the output WAV file.

if duration_param != 'Until Stopped':
    duration_sec = str(duration_param[6:8])
    duration_minutes = str(duration_param[3:5])
    duration_hours = str(duration_param[0:2])
    duration_seconds = int(duration_hours) * 3600 + int(duration_minutes) * 60 + int(duration_sec)
    total_samples = duration_seconds * SAMPLING_RATE
else:
    total_samples = -1

# print ("duration_sec: " + duration_sec);
# print ("duration_minutes: " + duration_minutes);
# print ("duration_hours: " + duration_hours);
# print ("duration_seconds: " + str(duration_seconds));
# print ("total_samples: " + str(total_samples));

# quit()
    
peak_value = 32767
peak_value_2 = peak_value * 2

if in_filename_param == '':
    while in_filename == '':
        in_filename = input('Input Filename: ')
else:
    in_filename = in_filename_param

if out_filename_param == '':
    while out_filename == '':
        out_filename = input('Output Filename (.wav): ')
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
    print("File has no data!")
    quit()

multiplier = peak_value_2 / widthval

num_writes = 0
num_seconds = 0

print("Press CTRL-C to stop running.\n")

obj = wave.open(out_filename, 'wb')
obj.setnchannels(1)  # mono
obj.setsampwidth(2)
obj.setframerate(SAMPLING_RATE)

# We write to the WAV file repeatedly until file length is reached.
try:
    while True:
        sample_num = 0
        num_seconds += 1
        while sample_num != total_samples:
            for element in string_to_write_value:
                sample_num += 1
                seconds = int(sample_num / SAMPLING_RATE)
                normalized_element = int((element * multiplier - peak_value) * VOLUME_LEVEL)
                value = normalized_element
                if value < -peak_value:
                    value = -peak_value
                elif value > peak_value:
                    value = peak_value
                
                data = struct.pack('<h', value)
                obj.writeframesraw(data)
                if sample_num % 25000 == 0:
                    if total_samples == -1: #No duration entered in command line.
                        sys.stdout.write('Status: (' + human_format(sample_num*2) + '): ' + in_filename + ' -> ' + out_filename + '     \r' )
                    else:
                        sys.stdout.write('Status: <' + str(int(sample_num/total_samples*100)) + '%> (' + human_format(sample_num*2) + '/' + human_format(total_samples*2) + '): ' + in_filename + ' -> ' + out_filename + '     \r' )
                
                if total_samples == sample_num:
                    if total_samples == -1: #No duration entered in command line.
                        sys.stdout.write('Status: (' + human_format(sample_num*2) + '): ' + in_filename + ' -> ' + out_filename + '     \r' )
                    else:
                        sys.stdout.write('Status: <' + str(int(sample_num/total_samples*100)) + '%> (' + human_format(sample_num*2) + '/' + human_format(total_samples*2) + '): ' + in_filename + ' -> ' + out_filename + '     \r' )

                    sys.stdout.write('\nInput Filename: ' + in_filename + '\n')
                    sys.stdout.write('Output Filename: ' + out_filename + '\n')
                    sys.stdout.write('Num Times File Repeated: ' + human_format(num_writes) + '\n')
                    sys.stdout.write('Num Samples Written: ' + human_format(total_samples*2) + '\n')
                    obj.close()
                    quit()
            num_writes += 1

        if total_samples == -1: #No duration entered in command line.
            sys.stdout.write('Status: [' + getTimeFromSeconds(num_seconds) + '] (' + human_format(sample_num) + '): ' + in_filename + ' -> ' + out_filename + '     \r' )
        else:
            sys.stdout.write('Status: <' + str(int(sample_num/total_samples*100)) + '%> [' + getTimeFromSeconds(num_seconds) + '] (' + human_format(sample_num) + 'B/' + human_format(total_samples) + 'B): ' + in_filename + ' -> ' + out_filename + '     \r' )

        sys.stdout.write('\nInput Filename: ' + in_filename + '\n')
        sys.stdout.write('Output Filename: ' + out_filename + '\n')
        sys.stdout.write('Num Times File Repeated: ' + human_format(num_writes) + '\n')
        sys.stdout.write('Num Samples Written: ' + human_format(total_samples*2) + '\n')
        obj.close()
        sys.stdout.flush()
        quit()
        
except KeyboardInterrupt:

    pass

if total_samples == -1: #No duration entered in command line.
    sys.stdout.write('Status: [' + getTimeFromSeconds(num_seconds) + '] (' + human_format(sample_num) + '): ' + in_filename + ' -> ' + out_filename + '     \r' )
else:
    sys.stdout.write('Status: <' + str(int(sample_num/total_samples*100)) + '%> [' + getTimeFromSeconds(num_seconds) + '] (' + human_format(sample_num) + '/' + human_format(total_samples) + '): ' + in_filename + ' -> ' + out_filename + '     \r' )

sys.stdout.write('\nInput Filename: ' + in_filename + '\n')
sys.stdout.write('Output Filename: ' + out_filename + '\n')
sys.stdout.write('Num Times File Repeated: ' + human_format(num_writes) + '\n')
sys.stdout.write('Num Samples Written: ' + human_format(total_samples*2) + '\n')
obj.close()
sys.stdout.flush()

obj.close()
