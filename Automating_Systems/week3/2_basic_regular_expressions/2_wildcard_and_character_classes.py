#!/usr/bin/env python3

import re

# Testing for lower and upper cases.
print(re.search(r"[Pp]ython", "python")) # <re.Match object; span=(0, 6), match='Python'>

print(re.search(r"[a-z]way", "The end of the highway")) # <re.Match object; span=(18, 22), match='hway'>

print(re.search(r"[a-z]way", "What a way to go")) # None

print(re.search(r"cloud[a-zA-Z0-9]", "cloudy")) # <re.Match object; span=(0, 6), match='cloudy'>

print(re.search(r"cloud[a-zA-Z0-9]", "cloud9")) # <re.Match object; span=(0, 6), match='cloud9'>


'''
Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.
'''


import re
def check_punctuation (text):
  result = re.search(r"[,.:;?!]", text)
  return result != None

print("\nCheck Punctuation Function Testing")
print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

print("\nMatching characters that aren't in a group using circumflex ^")
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces.")) # <re.Match object; span=(4, 5), match=' '>
print(re.search(r"[^a-zA-Z] ", "This is a sentence with spaces.")) # None

print("\nSearching either/or with the |")
print(re.search(r"cat|dog", "I like dogs")) # <re.Match object; span=(7, 10), match='dog'>
print(re.search(r"cat|dog", "I like both cats and dogs")) # <re.Match object; span=(12, 15), match='cat'>

print("\nFindall module")
print(re.findall(r"cat|dog", "I like both cats and dogs.")) # ['cat', 'dog']






