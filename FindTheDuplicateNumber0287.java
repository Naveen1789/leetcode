class FindTheDuplicateNumber0287 {
    public int findDuplicate(int[] nums) {
        int ans = 0;
        int curPtr = 0;
        while (ans == 0){
            if (nums[curPtr] <= 0){
                ans = curPtr;
            }
            else{
                int temp = nums[curPtr];
                nums[curPtr] = nums[curPtr] * -1;
                curPtr = temp;

            }
        }

        // for (int i=0; i < nums.length; i++){
        //     if (nums[i] < 0) {
        //         nums[i] = nums[i] * -1;
        //     }
        // }

        return ans;
    }
}
