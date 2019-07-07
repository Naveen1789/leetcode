class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        hMapOfLastOccurrence = {}

        lenOfS = len(s)

        i = 0

        ans = 0
        curCount = 0
        startingIndex = 0

        while i < lenOfS:
            if s[i] in hMapOfLastOccurrence:
                if hMapOfLastOccurrence[s[i]] < startingIndex:
                    curCount = curCount + 1
                    hMapOfLastOccurrence[s[i]] = i
                else:
                    if curCount > ans:
                        ans = curCount
                    startingIndex = hMapOfLastOccurrence[s[i]] + 1
                    curCount = i - hMapOfLastOccurrence[s[i]]
                    hMapOfLastOccurrence[s[i]] = i

            else:
                curCount = curCount + 1
                hMapOfLastOccurrence[s[i]] = i
            i = i + 1

        if curCount > ans:
            return curCount
        else:
            return ans
