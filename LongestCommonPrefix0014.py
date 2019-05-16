class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]

        strA = strs.pop()
        strB = strs.pop()
        ans = self.find_longest_common_prefix(strA, strB)

        while len(strs) > 0:
            str = strs.pop()
            ans = self.find_longest_common_prefix(ans, str)

        return ans

    def find_longest_common_prefix(self, strA, strB):
        ans = ""

        lenOfStrA = len(strA)
        lenOfStrB = len(strB)
        i = 0

        while i < lenOfStrA and i < lenOfStrB:
            if strA[i] == strB[i]:
                ans = ans + strA[i]
                i = i + 1
            else:
                return ans
        return ans
