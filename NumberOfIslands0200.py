class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == None or len(grid) < 1:
            return 0

        numOfIslands = 0

        numOfRows = len(grid)
        numOfCols = len(grid[0])

        row = 0
        col = 0

        while row < numOfRows:
            col = 0
            while col < numOfCols:
                if grid[row][col] == '1':
                    print 'boats'
                    numOfIslands = numOfIslands + 1
                    self.updateGrid(grid, row, col, numOfRows, numOfCols)
                col = col + 1
            row = row + 1


        return numOfIslands

    def updateGrid(self, grid, row, col, numOfRows, numOfCols):
        grid[row][col] = '0'
        # up
        if (row > 0) and grid[row-1][col] == '1':
            self.updateGrid(grid, row-1, col, numOfRows, numOfCols)
        # down
        if (row < numOfRows -1) and grid[row+1][col] == '1':
            self.updateGrid(grid, row+1, col, numOfRows, numOfCols)
        # left
        if (col > 0) and grid[row][col-1] == '1':
            self.updateGrid(grid, row, col-1, numOfRows, numOfCols)
        # right
        if (col < numOfCols -1) and grid[row][col+1] == '1':
            self.updateGrid(grid, row, col+1, numOfRows, numOfCols)
        
