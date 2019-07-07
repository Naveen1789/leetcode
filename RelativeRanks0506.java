class RelativeRanks0506 {

    public String getTitle(int rank) {
        switch(rank) {
            case 0: return "Gold Medal";
            case 1: return "Silver Medal";
            case 2: return "Bronze Medal";
            default: return Integer.toString(rank + 1);
        }
    }
    public String[] findRelativeRanks(int[] nums) {

        HashMap<Integer, Integer> hMap = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            hMap.put(nums[i], i);
        }

        Arrays.sort(nums);
        int i = 0;
        int j = nums.length - 1;

        while (i < j) {
            int temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;

            i = i + 1;
            j = j - 1;
        }

        String[] strNums = new String[nums.length];
        for (int k = 0; k < nums.length; k++) {
            strNums[hMap.get(nums[k])] = getTitle(k);
        }

        return strNums;
    }
}
