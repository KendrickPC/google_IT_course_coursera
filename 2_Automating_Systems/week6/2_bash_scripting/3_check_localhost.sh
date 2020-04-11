#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then 
	echo "Everything ok"
else
	echo "Error! 127.0.0.1 is not in /etc/hosts"
fi

# A conditional block in Bash that starts with 'if', ends with which of the following lines?
# Answer: fi (Backwards if)

