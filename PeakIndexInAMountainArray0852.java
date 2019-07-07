class PeakIndexInAMountainArray0852 {
    public int peakIndexInMountainArray(int[] A) {

        int i = 0;
        int ans = -1;
        int maxVal = Integer.MIN_VALUE;

        while (i < A.length){
            if (A[i] > maxVal){
                maxVal = A[i];
                ans = i;
            }
            i = i + 1;

        }
        return ans;
    }
}
