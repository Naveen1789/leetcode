class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        lenOfPattern = len(pattern)
        strArr = str.split()
        lenOfStrArr = len(strArr)

        if lenOfPattern != lenOfStrArr:
            return False

        patternToStr = {}
        strToPattern = {}

        i = 0
        while i < lenOfPattern:
            ch = pattern[i]
            word = strArr[i]
            if ch in patternToStr:
                if patternToStr[ch] != word:
                    return False
            else:
                if word in strToPattern:
                    return False
                patternToStr[ch] = word
                strToPattern[word] = ch
            i = i+1

        return True
