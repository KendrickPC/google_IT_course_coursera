# https://www.coursera.org/learn/python-operating-system/discussions/weeks/7/threads/FQjLH6bTScyIyx-m05nMFw

# log_analysis_using_regular_expressions.py

#!/usr/bin/env python3

import re
import csv
import operator
import sys

per_user = {}
error = {}

logfile = sys.argv[1]

err_msg_out = 'error_message.csv'
user_stats_out = 'user_statistics.csv'

with open(logfile) as f:
    for line in f:
        # Any word character (letter, number, underscore)
        result = re.search(r'ticky: ([\w+]*) ([\w ]*) .* \((.*)\)$', line)
        print(result)
        # group() returns the string matched by the RE
        print(result.group(1))
        print(result.group(2))
        if result.group(1) == "INFO":
            if result.group(3) not in per_user:
                per_user[result.group(3)] = {"INFO": 1, "ERROR": 0}
            else:
                per_user[result.group(3)]["INFO"] += 1

        if result.group(1) == "ERROR":
            if result.group(3) not in per_user:
                per_user[result.group(3)] = {"INFO": 0, "ERROR": 1}
            else:
                per_user[result.group(3)]["ERROR"] += 1

            if result.group(2) not in error:
                error[result.group(2)] = 1
            else:
                error[result.group(2)] += 1


sorted_per_user = sorted(per_user.items())
sorted_error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)

sorted_error.insert(0, ("Error", "Count"))

with open(err_msg_out, "w") as errcsv:
    for err in sorted_error:
        col1, col2 = err
        errcsv.write(str(col1) + "," + str(col2) + "\n")

with open(user_stats_out, "w") as usercsv:
    usercsv.write("Username,INFO,ERROR\n")
    for stats in sorted_per_user:
        col1, col2n3 = stats
        usercsv.write(str(col1) + "," + str(col2n3["INFO"]) + "," + str(col2n3["ERROR"]) + "\n")

