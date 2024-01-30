'''
importing a file located in one of the folders, called workplace
'''

import sys

sys.path.insert(1, r'C:\Users\swwai\.projects\python\python_programming\python-programming\modules\workplace')

import trial

'''Despite the highlighted error I can stil proceed because the interpreter know about the path
above even though the IDE doesn't '''

print(trial.names)