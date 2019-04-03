class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        numOfRows = len(grid)
        numOfCols = len(grid[0])

        row = 0
        col = 0

        perimieter = 0
        while row < numOfRows:
            col = 0
            while col < numOfCols:
                if grid[row][col] == 1:
                    numOfOutwardEdges = 0
                    grid[row][col] = 9
                    # up
                    if (row == 0) or grid[row-1][col] == 0:
                        numOfOutwardEdges = numOfOutwardEdges + 1
                    # down
                    if (row == numOfRows -1) or grid[row+1][col] == 0:
                        numOfOutwardEdges = numOfOutwardEdges + 1
                    # left
                    if (col == 0) or grid[row][col-1] == 0:
                        numOfOutwardEdges = numOfOutwardEdges + 1
                    # right
                    if (col == numOfCols -1) or grid[row][col+1] == 0:
                        numOfOutwardEdges = numOfOutwardEdges + 1

                    perimieter = perimieter + numOfOutwardEdges
                col = col + 1
            row = row + 1

        return perimieter
        
# class Solution(object):
#     def islandPerimeter(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         numOfRows = len(grid)
#         numOfCols = len(grid[0])
#
#         row = 0
#         col = 0
#
#         numOfIslands = 0
#         numOfNeighbors = 0
#         while row < numOfRows:
#             col = 0
#             while col < numOfCols:
#                 if grid[row][col] == 1:
#                     numOfIslands = numOfIslands + 1
#                     # down
#                     if (row < numOfRows -1) and grid[row+1][col] == 1:
#                         numOfNeighbors = numOfNeighbors + 1
#                     # right
#                     if (col < numOfCols -1) and grid[row][col+1] == 1:
#                         numOfNeighbors = numOfNeighbors + 1
#                 col = col + 1
#             row = row + 1
#
#         return (numOfIslands * 4) - (numOfNeighbors * 2)
