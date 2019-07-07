class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """

        if A == None or len(A) == 0:
            return []

        ans = list(A[0])
        lenOfA = len(A)
        i = 1
        while len(ans) > 0 and i < lenOfA:
            newAns = []

            strArr = list(A[i])
            lenOfStrArr = len(strArr)
            lenOfAns = len(ans)
            j = 0
            while j < lenOfAns and j < lenOfStrArr:
                if ans[j] in strArr:
                    newAns.append(ans[j])
                    strArr.remove(ans[j])
                j = j + 1
            ans = newAns
            i = i + 1

        return ans
