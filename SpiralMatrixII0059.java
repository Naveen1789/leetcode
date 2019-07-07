class SpiralMatrixII0059 {
    public int[][] generateMatrix(int n) {
        int[][] spiralMat = new int[n][n];

        fillInMatrix(spiralMat, 0, 0, n-1, n-1, 1);

        return spiralMat;
    }

    public void fillInMatrix(int[][] twoDimArr, int stRow, int stCol, int endRow, int endCol, int numToBeFilled){

        if (stRow > endRow || stCol > endCol){
            return;
        }
        else if (stRow == endRow){
            int c = stCol;
            while (c <= endCol) {
                twoDimArr[stRow][c++] = numToBeFilled++;
            }

        }
        else if (stCol == endCol){
            int r = stRow;
            while (r <= endRow) {
                twoDimArr[r++][stCol] = numToBeFilled++;
            }
        }
        else{
            int r = stRow;
            int c = stCol;
            while (c <= endCol){
                twoDimArr[r][c++] = numToBeFilled++;
            }

            r = stRow + 1;
            c = endCol;
            while (r <= endRow) {
                twoDimArr[r++][c] = numToBeFilled++;
            }

            r = endRow;
            c = endCol - 1;
            while (c >= stCol){
                twoDimArr[r][c--] = numToBeFilled++;
            }

            r = endRow - 1;
            c = stCol;
            while (r > stRow) {
                twoDimArr[r--][c] = numToBeFilled++;
            }

            stRow = stRow + 1;
            stCol = stCol + 1;
            endRow = endRow - 1;
            endCol = endCol - 1;
            fillInMatrix(twoDimArr, stRow, stCol, endRow, endCol, numToBeFilled);
        }
    }
}
