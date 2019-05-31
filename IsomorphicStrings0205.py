class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        lenOfS = len(s)
        lenOfT = len(t)

        if lenOfS != lenOfT:
            return False

        sToT = {}
        tToS = {}

        i = 0
        while i < lenOfS:
            sChar = s[i]
            tChar = t[i]
            if sChar in sToT:
                if sToT[sChar] != tChar:
                    return False
            else:
                if tChar in tToS:
                    return False
                sToT[sChar] = tChar
                tToS[tChar] = sChar
            i = i+1

        return True
