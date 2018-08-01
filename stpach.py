#A Python script that checks if a password is strong
#at least 8 digits, both uppercase and lowercase letters and at least one number.


import re

eght_char_long = re.compile(r'(\w|\W){8,}')
has_low = re.compile(r'[a-z]{1,}')
has_up = re.compile(r'[A-Z]{1,}')
has_dig = re.compile(r'(\d){1,}')

while True:
    pwd = input("Enter a password.\n")
    if eght_char_long.search(pwd) == None or has_low.search(pwd) == None or has_up.search(pwd) == None or has_dig.search(pwd) == None:
        print("Your password is not strong. Try again")
                                          
    else:
        print("Your password is strong. Good job!")
        break


        
        
        
        
