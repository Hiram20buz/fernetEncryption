import os
import sys


#scriptDir = os.path.dirname(os.path.abspath(sys.argv[0])) + "/"
files = []
dirs = []
for file in os.listdir():
    if os.path.isfile(file):
        files.append(file)
    else:
        dirs.append(file)
        
print(files)
print(dirs)
#print(scriptDir)