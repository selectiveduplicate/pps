#! /usr/bin/python3
#*************************************
#Extracts all possible contact numbers and email addresses from clipboard.
#This is a work in progress and applicable to information that are only local to Bangladesh. It's not a complete project. In some cases it might not be able to extract all contact numbers(and email addressess) that don't fall under the general criteria or pattern. Apart from that, it should work just fine.

#Just run the following command in the Terminal:

#./mobemexB.py
#For demonstration, head over to the following webpage and copy everything, then run the script: http://www.bacco.org.bd/member-list
#*************************************

import re, pyperclip

#collects all info from clipboard
all_info = pyperclip.paste()

#regex for mobile numbers
mob_numb_regex = re.compile(r'''(
    ((\+)?880)?               #ISD  
    (\-)?                   #separator
    (0)?                    #
    (\d\d)?                 #
    (\-)?                   #separator
    (\d{7})                #last 7 digits
    )''', re.VERBOSE)

#regex for email addr
email_addr_regex = re.compile(r'''(   
    [a-zA-Z0-9._%+-]+       # local part
    @                       # @ symb
    [a-zA-Z0-9.-]+          # domain
    (\.[a-zA-Z]{2,4})       # dot extension
    )''', re.VERBOSE)

#extraced info stays here
mobems = []

#collect
for mob_groups in mob_numb_regex.findall(all_info):
    mobems.append(mob_groups[0])

for em_groups in email_addr_regex.findall(all_info):
    mobems.append(em_groups[0])

#check for results and do the rest
if len(mobems) > 0:
    pyperclip.copy('\n'.join(mobems))
    print('All information below has been copied to your clipboard:')
    print('\n'.join(mobems))
else:
    print('Sorry! No relevant information was found')
