class RotateImage0048 {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < n; i++){
            for (int j = i; j < n; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for (int i = 0; i < n; i++){
            for (int j = 0; j < n/2; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][n-j-1];
                matrix[i][n-j-1] = temp;
            }
        }
    }

  //   public void rotate(int[][] matrix) {
  //   int n = matrix.length;
  //   for (int i = 0; i < n/2; i ++) {
  //     for (int j = i; j < n-i-1; j++) {
  //       int temp = matrix[n - 1 - j][i];
  //       matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1];
  //       matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i];
  //       matrix[j][n - 1 - i] = matrix[i][j];
  //       matrix[i][j] = temp;
  //     }
  //   }
  //
  //     display(matrix);
  // }
}
