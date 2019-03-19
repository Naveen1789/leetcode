class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        previousRow = [1]
        i = 1
        while i <= rowIndex:
            temp = []
            temp.append(1)
            j = 0
            lenOfPrevRow = len(previousRow)
            while j < (lenOfPrevRow - 1):
                temp.append(previousRow[j] + previousRow[j+1])
                j = j+1

            temp.append(1)
            previousRow = temp
            i = i+1
        return previousRow
