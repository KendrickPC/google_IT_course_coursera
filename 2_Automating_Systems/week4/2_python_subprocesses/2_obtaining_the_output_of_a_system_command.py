#!/usr/bin/env python3

import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print("\nReturn Code:")
print(result.returncode)

print("\nSTDOUT:")
# print(result.stdout) # b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'

# operating with the output of the command
print(result.stdout.decode().split()) # ['8.8.8.8.in-addr.arpa', 'domain', 'name', 'pointer', 'dns.google.']

'''
Which of the following is a Unicode standard used to convert an array of bytes into a string?
Answer: UTF-8 

Woohoo! This encoding is part of the Unicode standard that can transform an array of bytes into a string.
'''

print("\nReturn Code for a file that doesn't exist:")
result_2 = subprocess.run(["rm", "phantom_file_again.py"], capture_output=True)
print(result_2.returncode)

print("\nstdout code:")
print(result_2.stdout)

print("\nstderr code:")
print(result_2.stderr)