# 5_unit_test_case.py

import re 
  
my_txt = "A B C D E F G"

def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    return result

print(LetterCompiler(my_txt))