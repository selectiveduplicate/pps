#! /usr/bin/python3
#extracts email addresses and contact numbers

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
