#! /usr/bin/python3
# adds UNICODE bullet point character at the beginning of each line of text copied from clipboard.

import pyperclip

tobF = pyperclip.paste()
lines = tobF.split('\n')

for i in range(len(lines)):
    if len(lines[i]) > 1:           
        lines[i] = u'\u2022' + ' ' + lines[i]

modd_lines = '\n'.join(lines)
pyperclip.copy(modd_lines)
