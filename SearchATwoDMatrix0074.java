class SearchATwoDMatrix0074 {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix.length == 0){
            return false;
        }

        int rowNum = findRow(matrix, 0, matrix.length - 1, target);
        return elementInRow(matrix[rowNum], 0, matrix[rowNum].length - 1, target);
    }

    public int findRow(int[][] matrix, int low, int high, int target){
        if (low >= high){
            return low;
        }

        int mid = (low + high) / 2;
        if (target >= matrix[mid][0] && target <= matrix[mid][matrix[mid].length - 1]){
            return mid;
        }
        else if (target > matrix[mid][matrix[mid].length - 1]) {
            return findRow(matrix, mid + 1, high, target);
        }
        else {
            return findRow(matrix, low, mid - 1, target);
        }
    }

    public boolean elementInRow(int[] row, int low, int high, int target){
        if (low > high){
            return false;
        }
        int mid = (low + high) / 2;
        if (target == row[mid]){
            return true;
        }
        else if(target < row[mid]) {
            return elementInRow(row, low, mid - 1, target);
        }
        else {
            return elementInRow(row, mid + 1, high, target);
        }

    }
}
