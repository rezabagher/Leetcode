# -*- coding: utf-8 -*-
"""You are given a 0-indexed binary string s having an even length.

A string is beautiful if it's possible to partition it into one or more substrings such that:

Each substring has an even length.
Each substring contains only 1's or only 0's.
You can change any character in s to 0 or 1.

Return the minimum number of changes required to make the string s beautiful.
"""

class Solution(object):
    def minChanges(self, s):
       spl= 2
       c = 0
       while s:
          g, s=s[:spl],s[spl:]
          if g.count(g[0]) != len(g):
                c = c+1
       return c

ff = Solution()

ff.minChanges("0101")
