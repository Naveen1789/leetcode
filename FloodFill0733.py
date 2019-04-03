class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # print image
        # print sr
        # print sc
        # print newColor
        numOfRows = len(image)
        numOfCols = len(image[0])
        initialPixel = image[sr][sc]
        self.updateGrid(image, sr, sc, numOfRows, numOfCols, initialPixel, newColor)
        return image

    def updateGrid(self, grid, row, col, numOfRows, numOfCols, initialPixel, newColor):
        grid[row][col] = newColor
        # up
        if (row > 0) and grid[row-1][col] != newColor and grid[row-1][col] == initialPixel:
            self.updateGrid(grid, row-1, col, numOfRows, numOfCols, initialPixel, newColor)
        # down
        if (row < numOfRows -1) and grid[row+1][col] != newColor and grid[row+1][col] == initialPixel:
            self.updateGrid(grid, row+1, col, numOfRows, numOfCols, initialPixel, newColor)
        # left
        if (col > 0) and grid[row][col-1] != newColor and grid[row][col-1] == initialPixel:
            self.updateGrid(grid, row, col-1, numOfRows, numOfCols, initialPixel, newColor)
        # right
        if (col < numOfCols -1) and grid[row][col+1] != newColor and grid[row][col+1] == initialPixel:
            self.updateGrid(grid, row, col+1, numOfRows, numOfCols, initialPixel, newColor)
        
