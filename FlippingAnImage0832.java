class FlippingAnImage0832 {
    public int[][] flipAndInvertImage(int[][] A) {
        for(int[] row: A){
            invertRow(row);
        }

        for (int i = 0; i < A.length; i++){
            for (int j = 0; j < A[i].length; j++){
                A[i][j] = A[i][j] ^ 1;
            }
        }

        return A;
    }

    public void invertRow(int[] arr){
        int i = 0;
        int j = arr.length - 1;

        while (i < j){
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}
