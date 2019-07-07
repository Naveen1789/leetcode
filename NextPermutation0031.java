class NextPermutation0031 {
    public void nextPermutation(int[] nums) {
        int start = 0;
        int end = nums.length - 1;

        int i = end - 1;
        while(i >= 0 && nums[i] >= nums[i+1]){
            i--;
        }

        if (i >= 0){
            int j = nums.length - 1;
            while (j > i && nums[j] <= nums[i]){
                j--;
            }

            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;

            start = i+1;
        }


        reverseArray(nums, start, end);
    }

    public void reverseArray(int[] nums, int i, int j){
        while (i < j){
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
            j--;
        }
    }
}
