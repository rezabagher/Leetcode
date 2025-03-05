"""
s = "  hello world  "
s = s.rstrip()
s = s.lstrip()
n = s.split(" ")
i = 0 
j = len(n)-1
print(j)
while  i < j:
    n[i], n[j] = n[j], n[i]
    i = i + 1
    j = j - 1
print(n)"""
class Solution(object):
    def reverseWords(self, s):
        s = s.rstrip()
        s = s.lstrip()
        s = s.split(" ")
        i = 0 
        j = len(s)-1
        while  i < j:
            s[i], s[j] = s[j], s[i]
            i = i + 1
            j = j - 1
        return "".join(s)


