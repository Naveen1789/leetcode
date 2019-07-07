class UniquePaths0062 {
  public int uniquePaths(int m, int n) {
      int[][] twoDimMat = new int[m][n];
      saveCountOfUniquePaths(0, 0, twoDimMat);

      return twoDimMat[0][0];
  }

  public int saveCountOfUniquePaths(int m, int n, int[][] twoDimMat){
      if (twoDimMat[m][n] != 0){
          return twoDimMat[m][n];
      }

      if (m == twoDimMat.length - 1 || n == twoDimMat[0].length - 1){
          twoDimMat[m][n] = 1;
          return 1;
      }

      twoDimMat[m][n] = saveCountOfUniquePaths(m+1, n, twoDimMat) + saveCountOfUniquePaths(m, n+1, twoDimMat);
      return twoDimMat[m][n];
  }
}
