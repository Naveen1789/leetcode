class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        if matrix == None or matrix == []:
            return ans

        numOfRows = len(matrix)
        numOfCols = len(matrix[0])
        self.printPerimeter(matrix, 0, 0, numOfRows-1, numOfCols-1, ans)
        return ans

    def printPerimeter(self, twoDimArr, stRow, stCol, endRow, endCol, ans):
        # print "stRow = %d, stCol = %d, endRow = %d, endCol = %d" %(stRow, stCol, endRow, endCol)
        if stRow > endRow or stCol > endCol:
            return
        elif stRow == endRow:
            c = stCol
            while c <= endCol:
                ans.append(twoDimArr[stRow][c])
                c = c + 1
        elif stCol == endCol:
            r = stRow
            while r <= endRow:
                ans.append(twoDimArr[r][stCol])
                r = r + 1
        else:
            r = stRow
            c = stCol
            # right
            while c <= endCol:
                ans.append(twoDimArr[r][c])
                c = c + 1

            r = stRow + 1
            c = endCol
            # down
            while r <= endRow:
                ans.append(twoDimArr[r][c])
                r = r + 1

            r = endRow
            c = endCol - 1
            # left
            while c >= stCol:
                ans.append(twoDimArr[r][c])
                c = c - 1

            r = endRow - 1
            c = stCol
            # up
            while r > stRow:
                ans.append(twoDimArr[r][c])
                r = r - 1

            stRow = stRow + 1
            stCol = stCol + 1
            endRow = endRow - 1
            endCol = endCol - 1
            self.printPerimeter(twoDimArr, stRow, stCol, endRow, endCol, ans)
