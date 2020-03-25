#!/usr/bin/env python3

'''
Which method do you use to prepare a new environment to modify environment variables?
Answer: Copy

Awesome! Calling this method of the os.environ dictionary will copy the current environment variables to store and prepare a new environment.
'''

'''
If we're automating a one-off, well-defined task, we're developing a solution quickly is the biggest requirement, then using system commands and subprocesses can help a lot. But if we're doing something more complex or long-running, it's usually a good idea to use the baked in or external modules that Python provides. So before deciding to use a sub processes, it's a good idea to check the standard library or pypi repository to see if we can do the task with native Python and to check if someone has already created the automation that we wanted to write.
'''


# https://docs.python.org/3/library/subprocess.html