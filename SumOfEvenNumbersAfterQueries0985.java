class Solution {
    public int[] sumEvenAfterQueries(int[] A, int[][] queries) {

        int[] ans = new int[queries.length];

        int sumOfAllEvenElements = 0;
        for (int i = 0; i < A.length; i++){
            if (A[i] % 2 == 0){
                sumOfAllEvenElements = sumOfAllEvenElements + A[i];
            }
        }

        for (int i = 0; i < queries.length; i++){
            int newElem = queries[i][0];
            int index = queries[i][1];
            if (A[index] % 2 == 0) {
                sumOfAllEvenElements = sumOfAllEvenElements - A[index];
            }
            A[index] = newElem + A[index];
            if (A[index] % 2 == 0){
                sumOfAllEvenElements = sumOfAllEvenElements + A[index];
            }

            ans[i] = sumOfAllEvenElements;
        }

        return ans;
    }
}
