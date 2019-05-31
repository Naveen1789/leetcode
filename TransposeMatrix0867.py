class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        numOfRows = len(A)
        numOfCols = len(A[0])

        ans = []
        i = 0
        while i < numOfCols:
            j = 0
            tempArr = []
            while j < numOfRows:
                tempArr.append(A[j][i])
                j = j + 1
            ans.append(tempArr)
            i = i + 1

        return ans
