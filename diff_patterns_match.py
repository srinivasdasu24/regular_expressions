"""
Regular expression basics, regex groups and pipe character usage in regex 

"""

import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phoneNum_regex = re.compile(
    r'\d\d\d-\d\d\d-\d\d\d\d')  # re.compile to create regex object  \d is - digit numeric character
mob_num = phoneNum_regex.search(message)
# print(phoneNum_regex.findall(message)) # findall returns a list of all occurences of the pattern
print(mob_num.group)  # regex object has group method which tells the matching pattern

# pattern with different groups - groups are created in regex strings using parentheses
phoneNum_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # this pattern will have twwo groups
mob_num = phoneNum_regex.search(message)
mob_num.group()  # gives entire match
mob_num.group(1)  # gives first 3 digits  1 is first set of parentheses , 2 is second and so on
mob_num.group(2)  # gives remaining pattern
# o/p is : '415-555-1011'
#        :'415'
#        : '555-1011'

# pattern with matching braces( () )
phoneNum_regex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo = phoneNum_regex.search('My number is (415) 555-4243')
mo.group()
# o/p is : '(415) 555-4243

# matching multiple patterns
bat_regx = re.compile(r'Bat(man|mobile|copter|bat)')  # pipe | symbol used to match more than one pattern
mo = bat_regx.search('I like Batman movie')
mo.group()  # o/p is 'Batman'

# if search method doesn't find pattern it returns None
mo = bat_regx.search('Batmotorcycle lost a wheel')
mo == None  # prints True


