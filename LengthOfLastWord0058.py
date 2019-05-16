class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        prevCount = 0
        count = 0
        for ch in s:
            if ch == ' ' and count > 0:
                prevCount = count
                count = 0
            elif ch == ' ':
                count = 0
            else:
                count = count + 1

        if count > 0:
            return count

        return prevCount
