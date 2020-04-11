#!/usr/bin/env python3

import re

# Match py, followed by any number of regular characters, followed by n.
print(re.search(r"py.*n", "pygmalion")) # <re.Match object; span=(0, 9), match='pygmalion'>

# The start takes as many characters as possible. AKA Behavior is greedy.
print(re.search(r"P.*n", "Python programming")) # <re.Match object; span=(0, 17), match='Python programmin'>

# Taking the first occurrence of search string. AKA shortest amount of characters possible.
print(re.search(r"P[a-z]*", "Python programming")) # <re.Match object; span=(0, 6), match='Python'>

# Zero times is also a possibility.
print(re.search(r"Py[a-z]*", "Pyn"))

# The plus character matches one or more occurrences of the character that comes before it. Match pattern shows us the shortest possible matching string.
print(re.search(r"o+l+", "goldfish")) # <re.Match object; span=(1, 3), match='ol'>

print(re.search(r"o+l+", "woolly")) # <re.Match object; span=(1, 5), match='ooll'>

print(re.search(r"o+l+", "boil")) # None


print("\nZip Code Checking:")
'''
Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
'''

import re
def check_zip_code(text):
  result = re.search(r" [0-9]{5}", text)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


print("\n? mark multiplier. Either zero or one occurrence before it.")
# ? mark marks it as optional.
print(re.search(r"p?each", "To each their own.")) # <re.Match object; span=(3, 7), match='each'>
print(re.search(r"p?each", "I like peaches.")) # <re.Match object; span=(7, 12), match='peach'>

print(re.search(r"p?each", "I like preachers.")) # <re.Match object; span=(9, 13), match='each'>













