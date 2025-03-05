class Solution(object):
    def reverseWords(self, s):
        s = s.split(" ")
        s[:] = (value for value in s if value != '') # removing all spaces
        i = 0 
        j = len(s)-1
        s = s[::-1]
        return " ".join(s)


