#uploads file to Dropbox using Dropbox SDK and API
#also creates a backup of the file on local hard drive

#! /usr/bin/python3


import os
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
from shutil import copyfile

TOKEN = ''

LOCALFILE = '/home/user_name/Desktop/new.txt'
BACKUPPATH = '/home/user_name/Documents/backup_new.txt'

#backup the file elsewhere on harddrive in case something goes wrong
#get extension of the file new.txt
#extension can also be got by an user function
#written at the end
exton = os.path.splitext(LOCALFILE)[1]  
LOCALBACKUP = '/home/user_name/backup' + exton #locally backup here
copyfile(LOCALFILE, LOCALBACKUP)

# Uploads contents of LOCALFILE to Dropbox
def backup():
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the contents of the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbox_obj.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

if __name__ == '__main__':
    # Create an instance of a Dropbox class, which can make requests to the API.
    dbox_obj = dropbox.Dropbox(TOKEN)
    
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. "
            "Kindly paste in your token in line 13 of the source code.")
    
    # Check that the access token is valid
    try:
        dbox_obj.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an access token")

    backup()
    print("Uploading done!")

    #user-defined function for extracting file extension
    def get_exton():
        file_base = os.path.basename(LOCALFILE)
        start = len(file_base) - 1
        while start:
            if file_base[start] == '.':
                exton = file_base[start:len(file_base)-1]
                break
            start = start - 1
        return exton
