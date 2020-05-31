"""

Phone_number_match program using normal way

"""


def isPhoneNumber(text):  # 415-555-1011
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # no area code
    if text[3] != '-':
        return False  # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # no first 3 digits
    if text[7] != '-':
        return False  # missing second dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # missing last 4 digits
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i + 12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Phone number not found')

"""
Using regex pattern to do same thing as above
"""
import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phoneNum_regex = re.compile(
    r'\d\d\d-\d\d\d-\d\d\d\d')  # re.compile to create regex object  \d is - digit numeric character
mob_num = phoneNum_regex.search(message)
# print(phoneNum_regex.findall(message)) # findall returns a list of all occurences of the pattern
print(mob_num.group)  # regex object has group method which tells the matching pattern

# pattern with different groups
phoneNum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # this pattern will have twwo groups
mob_num = phoneNum_regex.search(message)
mob_num.group()  # gives entire match
mob_num.group(1)  # gives first 3 digits
mob_num.group(2)  # gives remaining pattern
# o/p is : '415-555-1011'
#        :'415'
#        : '555-1011'

# pattern with matching braces( () )
phoneNum_regex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNum_regex.search('My number is (415) 555-4243')
mo.group()
# o/p is : '(415) 555-4243


