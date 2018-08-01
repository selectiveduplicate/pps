#! python3
# An isecure password locker program

import sys, pyperclip

# Users may insert account names as his wish in the dictionary
pass_words = {'email': 'dummypassworD-=-=-=',
              'blog': 'blogDummypasSword',
              'twitter': 'whateveryouwannaTWEET'}

# checks to see if both file name and account name has been provided
if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()  

# the second arg is the account name
account = sys.argv[1]

# password will be coppied to clipboard in case the account exists in the dict
if account in pass_words:
    pyperclip.copy(pass_words[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print("There's no password for the account named " + account)