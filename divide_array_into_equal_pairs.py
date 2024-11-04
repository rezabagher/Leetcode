"""You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false."""
#elitcode easy practice
class Solution(object):
    def __init__(self, num):
      self.num = num
    def divideArray(self):
        num = sorted(self.num) # sorting numbers 
        group= int(len(num)/2) # counting how many groups we are going to have
        spl= 2 # each groap length
        c = 0 # a variable in order to count the number of correct sub group
        while num:
           g, num = num[:spl], num[spl:]
           g_1= g.count(g[0])
           if g_1== len(g):
               c =c+1 
           else:
              break
        if c == group:
          return True
        # if c is equal to number of sub groups , means we have equal Trues.
        else:
          return False

s = Solution([2,2,2,2])

s.num

s.divideArray( )