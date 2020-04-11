#!/usr/bin/env python3
import re

# .*+?^[]

# We want .com not lcom
print(re.search(r".com", "welcome")) # <re.Match object; span=(2, 6), match='lcom'>
print(re.search(r"\.com", "welcome")) # None
print(re.search(r"\.com", "cnn.com")) # <re.Match object; span=(3, 7), match='.com'>

# Matching everything that is a letter, but spaces are not included.
print(re.search(r"\w*", "This is an example")) # <re.Match object; span=(0, 4), match='This'>

print(re.search(r"\w*", "And_this_is_another_example")) # <re.Match object; span=(0, 27), match='And_this_is_another_example'>

'''
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
'''


import re

def check_character_groups(text):
  # result = re.search(r"\w\s", text)
  result = re.search(r"\w\s", text)
  return result != None

print("\nCheck Character Groups Testing:")
print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False

# regex101.com




