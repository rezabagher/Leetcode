# -*- coding: utf-8 -*-
"""palinimdrome number.ipynb

Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""

class Solution(object):
    def isPalindrome(self, x):
      if str(x) [::-1] == str(x) :
        return True
      else:
        return False
