#!/bin/bash

# HEADS UP! There can be no spaces between the equal sign.
'''
example=hello
echo $example
'''

'''
When defining a variable you receive the "command not found" message. Which of the following commands will resolve this error?
Answer: User4=billy
'''

line="-----------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"
uptime; echo $line

echo "VM_STAT"
vm_stat; echo $line

echo "WHO"
who; echo $line

echo "Finishing at: $(date)"