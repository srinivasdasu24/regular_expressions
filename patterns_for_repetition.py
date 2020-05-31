"""
Regex patterns for repetition match
 ? says group matches zero or one times
 * says group matches zero or more times
 + says group matches one or more times
 {n} can match a specific number of times
 {n,m} can match a min(n) and max(m) no of times
 {,m} - no min match pattern required starts from zero
 {n,} - no max match pattern required ends to infinity
 Greedy matching matches longest possible string match
 putting a ? mark after {} makes it non greedy {}? - finds minimum possible string match
"""

import re

bat_reg = re.compile(r'Bat(wo)?man')  # (wo)? - this pattern can occur 0 or 1 times
mo = bat_reg.search('The Adventures of Batman')
mo.group()  # o/p is 'Batman'

mo = bat_reg.search('The Adventures of Batwoman')
mo.group()  # o/p is 'Batwoman'

# this pattern matches phone number with area code and w/o area code too
phone_reg = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phone_reg.search('My number is 415-555-5674. Call me  when you receive it')
phone_reg.search('My number is 555-5674. Call me  when you receive it')

# regex pattern (pattern)* -- 0 or more times
bat_reg = re.compile(r'Bat(wo)*man')  # (wo)? - this pattern can occur 0 or more times
mo = bat_reg.search('The Adventures of Batman')
mo.group()  # o/p is 'Batman'

mo = bat_reg.search('The Adventures of Batwoman')
mo.group()  # o/p is 'Batwoman'

mo = bat_reg.search('The Adventures of Batwowowoman')
mo.group()  # o/p is 'Batwowowoman'

# regex pattern (pattern)+ -- one or more times

bat_reg = re.compile(r'Bat(wo)+man')
mo = bat_reg.search('The Adventures of Batman')
mo = bat_reg.search('The Adventures of Batman') == None   # prints True

mo = bat_reg.search('The Adventures of Batwoman')
mo = bat_reg.search('The Adventures of Batwowowoman')

# pattern matching *+?

regex = re.compile(r'\+\*\?')
regex.search('I learnt about +?* regex syntax')

# pattern having exactly n number of entries

no_regx = re.compile(r'(Ha){3}')  # matches string having 3 times of ha
no_regx.search('He said "HaHa')

phn_rgx = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){4}')
phn_rgx.search('My numbers are 415-567-8967,546-789-1432')

# pattern with min and max repetitions (pattern){3,5)

ha_regx = re.compile(r'(ha){3,5}')
ha_regx.search('He said "hahaha')

ha_regx = re.compile(r'(ha){3,}')  # this matches minimum with 3 pattern and max can be any

# digit regex , does greedy match
digit_regx = re.compile(r'(\d){3,5}')  # tries to match longest possible string
digit_regx.search('1234567890')  # o/p is 12345

digit_regx = re.compile(r'(\d){3,5}?')   # this pattern will do non-greedy match, matches min pattern
digit_regx.search('1234567890')   # o/p is 123

