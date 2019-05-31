class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        h = {}

        for ch in s:
            if ch in h:
                h[ch] = h[ch] + 1
            else:
                h[ch] = 1

        for ch in t:
            if not(ch in h) or h[ch] == 0:
                return ch
            else:
                h[ch] = h[ch] - 1
