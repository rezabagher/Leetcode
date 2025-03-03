class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        i  = 0 # creating two pointers 
        j = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while i < j:
            if s[i] in vowels:
                if s[j] in vowels: # exchanging i , j values
                    s[i], s[j] = s[j], s[i]
                    i = i + 1
                j = j - 1
            else:
             i = i + 1
        return "".join(s) # changing the list into string 
