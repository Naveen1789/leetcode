class SearchInRotatedSortedArray0033 {
    public int findPivot(int[] nums) {
        int left = 0;
        int right = nums.length - 1;

        if (nums[left] < nums[right]){
            return 0;
        }

        while (left <= right){
            int pivot = (left + right) / 2;
            // System.out.println("left = " + left + ", right = " + right + ", pivot = " + pivot);
            if (nums[pivot] > nums[pivot+1]){
                return pivot + 1;
            }
            else {
                if (nums[pivot] >= nums[left]) {
                    left = pivot + 1;
                }
                else {
                    right = pivot - 1;
                }
            }
        }

        return 0;
    }

    public int binSearch(int[] nums, int target, int left, int right){
        // System.out.println("left = " + left + ", right = " + right);
        while (left <= right) {
            int mid = (left + right) / 2;
            if (target == nums[mid]){
                return mid;
            }
            else if (target > nums[mid]){
                left = mid + 1;
            }
            else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public int search(int[] nums, int target) {

        if (nums.length == 0){
            return -1;
        }
        if (nums.length == 1){
            if (nums[0] == target){
                return 0;
            }
            else {
                return -1;
            }
        }
        int pivot = findPivot(nums);
        // System.out.println("pivot = " + pivot);

        if (pivot == 0) {
            return binSearch(nums, target, 0, nums.length - 1);
        }

        if (target < nums[0]){
            return binSearch(nums, target, pivot, nums.length - 1);
        }
        else {
            return binSearch(nums, target, 0, pivot-1);
        }
    }
}
