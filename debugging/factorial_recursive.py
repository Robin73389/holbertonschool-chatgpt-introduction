#!/usr/bin/python3

# factiorial: This is the function why allow the recursion
# n: This is the number of the recursion
# Return: f

import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)