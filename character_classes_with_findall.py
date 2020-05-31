"""
regex pattern with zero or one groups and applied findall returns a list of strings as o/p
regex pattern with two or more groups and applied findall returns a list of tuple of strings as o/p
\d  - matches any numeric digit from 0 to 9
\D  - matches any character that is not numeric digit from 0 to 9
\w  - matches any letter, numeric digit, or underscore character
\W  - macthes any charatcer that is not a letter, numeric digit and underscore
\s  - matches any space or newline character
\S - any character that is not space or new line
^ before character class makes it negative class

"""
import re
# pattern having one group
phn_rgx = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phn_rgx.findall('508-555-5467 and 567-786-1234')    #  o/p is ['508-555-5467','567-786-1234']

# pattern having 2 groups
phn_rgx = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phn_rgx.findall('508-555-5467 and 567-786-1234')    #  o/p is [('508','555-5467'),('567','786-1234')]

# pattern having 3 groups
phn_rgx = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
phn_rgx.findall('508-555-5467 and 567-786-1234')
# o/p is [('508-555-5467','508','555-5467'),('567-786-1234','567','786-1234')]

lyrics = '12 drummers drumming, 11 pipers piping'
xmas_regex = re.compile(r'\d+\s\w+')
xmas_regex.findall(lyrics)  # o/p is ['12 drumers', '11 pipers']

# own character classes

vowel_rgx = re.compile(r'[aeiouAEIOU]')
vowel_rgx.findall("Robocap eats baby food")
# o/p is ['o','o','a','e,'a','a','o','o']

doublevowel_rgx = re.compile(r'[aeiouAEIOU]{2}')
doublevowel_rgx.findall("Robocap eats baby food")
# o/p is ['ea','oo']

consonant_rgx = re.compile(r'[^aeiouAEIOU]')
consonant_rgx.findall("Robocap eats baby food.")

# o/p is ['R','b','c','t','s',' ', ' ','b','b','y',' ','f','d','.']
