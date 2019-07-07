class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> hMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++){
            if(hMap.containsKey(nums[i])){
                if (i - hMap.get(nums[i]) <= k){
                    return true;
                }
            }
            hMap.put(nums[i], i);
        }

        return false;

    }
}
