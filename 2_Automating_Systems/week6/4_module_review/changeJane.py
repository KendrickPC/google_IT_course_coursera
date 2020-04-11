#!/usr/bin/env python3

import sys
import subprocess

#open version

f = open(sys.argv[1],"r")
for line in f.readlines():
  old_name = line.strip()
  new_name = old_name.replace("jane","jdoe")
  subprocess.run(["mv",old_name,new_name])
# f.close()

#with version
with open(sys.argv[1],"r") as files:
  for line in files.readlines():
    old_name = line.strip()
      new_name = old_name.replace("jane","jode")
      subprocess.run(["mv",old_name,new_name])  
  # files.close()


'''
chmod +x changeJane.py
./changeJane.py oldFiles.txt

'''