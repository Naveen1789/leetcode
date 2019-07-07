class FairCandySwap0888 {
    public int[] fairCandySwap(int[] A, int[] B) {
        int sumOfA = 0;
        int sumOfB = 0;

        for (int i = 0; i < A.length; i++){
            sumOfA = sumOfA + A[i];
        }

        for (int i = 0; i < B.length; i++){
            sumOfB = sumOfB + B[i];
        }

        int mid = (sumOfA + sumOfB) / 2;

        HashSet<Integer> set=new HashSet<Integer>();
        for (int i = 0; i < A.length; i++){
            set.add(A[i] - (sumOfA - mid));
        }

        for (int i = 0; i < B.length; i++){
            if (set.contains(B[i])){
                int[] ans = {(mid - sumOfB + B[i]), B[i]};
                return ans;
            }
        }
        return null;

    }
}
