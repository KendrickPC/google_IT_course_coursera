#!/usr/bin/env python3

import subprocess
# subprocess.run(["date"]) # Fri Mar 13 18:28:00 CST 2020
# echo $?
# Return code of 0

# subprocess.run(args = ["sleep", "2"])
# You may have noticed that while the sleep command was running, the interpreter was blocked and we couldn't interact with it.
# That's exactly what we mean about the parent process being blocked until the child process is done. 
# Asking sleep command to wait for two seconds.

result = subprocess.run(["ls", "phantom_file.py"])
print("\nReturn Code:")
print(result.returncode)

'''
A system command that sends ICMP packets can be executed within a script by using which of the following?
Answer: subprocess.run
This function will execute a system command such as ping.
'''

