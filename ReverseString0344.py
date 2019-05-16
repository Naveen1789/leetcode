class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lenOfS = len(s)
        i = 0
        j = lenOfS - 1

        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i = i+1
            j = j-1

        return s
