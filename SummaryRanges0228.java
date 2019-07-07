class SummaryRanges0228 {
    public List<String> summaryRanges(int[] nums) {
        ArrayList<String> ans = new ArrayList<String>();

        for (int i = 0; i < nums.length;) {
            // System.out.println("i = " + i);
            int j = i+1;
            while ((j < nums.length) && (nums[j-1] == nums[j] - 1)) {
                j = j+1;
            }
            // System.out.println("j = " + j);
            if ((i+1)==j){
                ans.add(nums[i] + "");
            }
            else{
                ans.add(nums[i] + "->" + nums[j-1]);
            }
            i = j;
        }

        return ans;
    }
}
