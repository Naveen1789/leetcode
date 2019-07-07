class MinimumPathSum0064 {
    public int minPathSum(int[][] grid) {
        int numOfRows = grid.length;
        int numOfCols = grid[0].length;

        int[][] twoDimMat = new int[numOfRows][numOfCols];
        for (int r = 0; r < numOfRows; r ++){
            for (int c = 0; c < numOfCols; c++){
                twoDimMat[r][c] = -1;
            }
        }

        twoDimMat[numOfRows-1][numOfCols-1] = grid[numOfRows-1][numOfCols-1];

        findMinPathSum(0, 0, twoDimMat, grid);

        return twoDimMat[0][0];
    }

    public int findMinPathSum(int r, int c, int[][] twoDimMat, int[][] grid){
        if (twoDimMat[r][c] >= 0) {
            return twoDimMat[r][c];
        }
        else if (r == twoDimMat.length - 1) {
            twoDimMat[r][c] = grid[r][c] + findMinPathSum(r, c+1, twoDimMat, grid);
        }
        else if (c == twoDimMat[0].length - 1){
            twoDimMat[r][c] = grid[r][c] + findMinPathSum(r+1, c, twoDimMat, grid);
        }
        else {
            twoDimMat[r][c] = grid[r][c] + Math.min(findMinPathSum(r+1, c, twoDimMat, grid), findMinPathSum(r, c+1, twoDimMat, grid));
        }

        return twoDimMat[r][c];
    }
}
