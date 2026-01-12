#!/usr/bin/python3
import sys
i = 1
for i in range(len(sys.argv)):
    if i == 0:
        print(sys.argv[i].replace("./", ""))
    else:
        print(sys.argv[i])