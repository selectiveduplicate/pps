#! python3

#******************************************************
#An insecure password locker/manager program written using Python.

#Provided Python is installed and the two files are in the same folder and in the "system PATH" on Windows, the script can be run by pressing WIN+R on Windows and typing:
#pw account_name
#If the account_name exists, then the password will be copied to clipboard and a relevent message will be displayed.

#Of course the dictionary used in the script may be modified to store passwords of more user accounts and can be accessed in the same way.

#I will be porting this project to Linux as soon as I can to learn how things can be done there, and will update the instructions.

#On Linux, for convenience, pw.py should be in the /home/username folder, also the shebang line
#need to be changed to proper format. Then the file's permission must be changed to make it executable.
#Then the script can be run.

#Note: There might be a "Pyperclip could not find a copy/paste mechanism for your system" message. To solve this, xclip or xsel needs to be installed by typing:
#sudo apt-get install xsel utility
*******************************************************

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
