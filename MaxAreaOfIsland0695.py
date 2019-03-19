class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == None or len(grid) < 1:
            return 0

        maxArea = 0

        numOfRows = len(grid)
        numOfCols = len(grid[0])

        row = 0
        col = 0

        while row < numOfRows:
            col = 0
            while col < numOfCols:
                if grid[row][col] == 1:
                    area = self.updateGrid(grid, row, col, numOfRows, numOfCols)
                    # print area
                    if area > maxArea:
                        maxArea = area
                col = col + 1
            row = row + 1


        return maxArea

    def updateGrid(self, grid, row, col, numOfRows, numOfCols):
        grid[row][col] = 0
        a1 = a2 = a3 = a4 = 0
        # up
        if (row > 0) and grid[row-1][col] == 1:
            a1 = self.updateGrid(grid, row-1, col, numOfRows, numOfCols)
        # down
        if (row < numOfRows -1) and grid[row+1][col] == 1:
            a2 = self.updateGrid(grid, row+1, col, numOfRows, numOfCols)
        # left
        if (col > 0) and grid[row][col-1] == 1:
            a3 = self.updateGrid(grid, row, col-1, numOfRows, numOfCols)
        # right
        if (col < numOfCols -1) and grid[row][col+1] == 1:
            a4 = self.updateGrid(grid, row, col+1, numOfRows, numOfCols)

        return (a1 + a2 + a3 + a4 + 1)
