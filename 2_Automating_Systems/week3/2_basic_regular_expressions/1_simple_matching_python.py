#!/usr/bin/env python3
# chmod +x <file_name>

# Simple Matching Python
import re

result = re.search(r"aza", "plaza")
print(result) # <re.Match object; span=(2, 5), match='aza'>

result = re.search(r"aza", "bazaar")
print(result) # <re.Match object; span=(1, 4), match='aza'>

result = re.search(r"aza", "maze")
print(result) # none

# Running circumflex search for regex
result = re.search(r"^x", "xenon")
print(result) # <re.Match object; span=(0, 1), match='x'>

# Wildcard dot notation
result = re.search(r"p.ng", "penguin")
print(result) # <re.Match object; span=(0, 4), match='peng'>

result = re.search(r"p.ng", "clapping")
print(result) # <re.Match object; span=(4, 8), match='ping'>

result = re.search(r"p.ng", "sponge")
print(result) # <re.Match object; span=(1, 5), match='pong'>


print("\nCheck AEI function test")
# import re
def check_aei(text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

