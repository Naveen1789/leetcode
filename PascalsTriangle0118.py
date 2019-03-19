class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]

        answer = [[1]]
        previousRow = [1]
        i = 2
        while i <= numRows:
            temp = []
            temp.append(1)
            j = 0
            lenOfPrevRow = len(previousRow)
            while j < (lenOfPrevRow - 1):
                temp.append(previousRow[j] + previousRow[j+1])
                j = j+1

            temp.append(1)
            answer.append(temp)
            previousRow = temp
            i = i+1
        return answer
