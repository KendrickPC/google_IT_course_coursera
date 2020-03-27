#!/usr/bin/env python3


import re


print(re.search(r"A.*a", "Argentina")) # <re.Match object; span=(0, 9), match='Argentina'>

print(re.search(r"A.*a", "Azerbaijan")) # <re.Match object; span=(0, 9), match='Azerbaija'>
# This above occured becasue we did not tell the search to return the entire string.

# Make clear that we only want to match lines that begin and end with the letter A
print(re.search(r"^A.*a$", "Azerbaijan")) # None

# 
print(re.search(r"^A.*a$", "Australia")) # <re.Match object; span=(0, 9), match='Australia'>

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name")) # <re.Match object; span=(0, 30), match='_this_is_a_valid_variable_name'>
print(re.search(pattern, "this isn't a valid variable")) # None
print(re.search(pattern, "my_variable1")) # <re.Match object; span=(0, 12), match='my_variable1'>
print(re.search(pattern, "2my_variable")) # None

'''
Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.
'''


import re
def check_sentence(text):
  result = re.search(r"^[A-Z][ |a-z]*[.!\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True




