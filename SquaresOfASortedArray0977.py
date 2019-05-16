class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        lenOfA = len(A)
        breakPoint = lenOfA

        i = 0
        while i < lenOfA:
            if A[i] >= 0:
                breakPoint = i
                break
            i = i+1

        leftOfBreakPoint = breakPoint - 1

        while leftOfBreakPoint >= 0 and breakPoint < lenOfA:
            if abs(A[leftOfBreakPoint]) < abs(A[breakPoint]):
                ans.append(A[leftOfBreakPoint] * A[leftOfBreakPoint])
                leftOfBreakPoint = leftOfBreakPoint - 1
            else:
                ans.append(A[breakPoint] * A[breakPoint])
                breakPoint = breakPoint + 1

        while leftOfBreakPoint >= 0:
            ans.append(A[leftOfBreakPoint] * A[leftOfBreakPoint])
            leftOfBreakPoint = leftOfBreakPoint - 1
        while breakPoint < lenOfA:
            ans.append(A[breakPoint] * A[breakPoint])
            breakPoint = breakPoint + 1

        return ans
