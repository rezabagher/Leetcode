# -*- coding: utf-8 -*-


f =[int(input()) ]# taking a number as an input an converting it tot

# Using map
output = list(map(int, str(f[0])))

cout = 0
for i in range(len(output)):
  if f[0]%output[i]==0:
    cout =cout+1

print(cout)