class FindFirstAndLastPositionOfElementInSortedArray0034 {

    public int findBoundary(int[] nums, int target, boolean leftBoundary) {
        int left = 0;
        int right = nums.length;

        while (left < right){
            int mid = (left + right) / 2;
             if (nums[mid] > target || (leftBoundary && nums[mid] == target)){
                 right = mid;
             }
            else{
                left = mid + 1;
            }
        }

        return left;
    }
    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1, -1};

        if(nums == null || nums.length == 0){
            return ans;
        }
        int leftBoundary = findBoundary(nums, target, true);

        if (leftBoundary == nums.length || nums[leftBoundary] != target){
            return ans;
        }

        ans[0] = leftBoundary;
        ans[1] = findBoundary(nums, target, false) - 1;
        return ans;
    }
}
