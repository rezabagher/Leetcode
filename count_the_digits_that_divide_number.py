# -*- coding: utf-8 -*-
"""
Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.
"""

f =[int(input()) ]# taking a number as an input an converting it tot

# Using map
output = list(map(int, str(f[0])))

cout = 0
for i in range(len(output)):
  if f[0]%output[i]==0:
    cout =cout+1

print(cout)
