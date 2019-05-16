class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        lenOfS = len(s)
        i = 0
        j = lenOfS - 1
        arrayOfVowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while i < j:
            while i < lenOfS and (not s[i] in arrayOfVowels):
                i = i + 1
            while j > 0 and (not s[j] in arrayOfVowels):
                j = j - 1

            if i < j:
                temp = s[i]
                s[i] = s[j]
                s[j] = temp
                i = i+1
                j = j-1


        return ''.join(s)
