#! /usr/bin/python3
# adds bullet points to every line of the copied text

import pyperclip

tobF = pyperclip.paste()
lines = tobF.split('\n')

for i in range(len(lines)):
    if len(lines[i]) > 1:           
        lines[i] = u'\u2022' + ' ' + lines[i]

modd_lines = '\n'.join(lines)
pyperclip.copy(modd_lines)
