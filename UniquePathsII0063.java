class UniquePathsII0063 {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        int[][] twoDimMat = new int[m][n];
        for (int r = 0; r < m; r ++){
            for (int c = 0; c < n; c++){
                twoDimMat[r][c] = -1;
            }
        }

        twoDimMat[m-1][n-1] = (obstacleGrid[m-1][n-1] == 0) ? 1 : 0;

        saveCountOfUniquePaths(0, 0, twoDimMat, obstacleGrid);

        return twoDimMat[0][0];
    }

    public int saveCountOfUniquePaths(int m, int n, int[][] twoDimMat, int[][] obstacleGrid){
        if (twoDimMat[m][n] >= 0){
        }
        else if (obstacleGrid[m][n] == 1){
            twoDimMat[m][n] = 0;
        }
        else if (m == twoDimMat.length - 1) {
            twoDimMat[m][n] = saveCountOfUniquePaths(m, n+1, twoDimMat, obstacleGrid);
        }
        else if (n == twoDimMat[0].length - 1){
            twoDimMat[m][n] = saveCountOfUniquePaths(m+1, n, twoDimMat, obstacleGrid);
        }
        else {
            twoDimMat[m][n] = saveCountOfUniquePaths(m+1, n, twoDimMat, obstacleGrid) + saveCountOfUniquePaths(m, n+1, twoDimMat, obstacleGrid);
        }


        return twoDimMat[m][n];
    }
}
