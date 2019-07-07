class SubarraySumEqualsK0560 {
    public int subarraySum(int[] nums, int k) {

        int ans = 0;

        int[][] mat = new int[nums.length][nums.length];
        for (int i = 0; i < nums.length; i++){
            mat[i][i] = nums[i];
            if(mat[i][i] == k){
                ans++;
            }
        }

        for(int len = 1; len < nums.length; len++){
            for(int row = 0; (row + len) < nums.length; row++){
                int col = row + len;
                mat[row][col] = mat[row][col-1] + mat[row+1][col] - mat[row+1][col-1];
                if (mat[row][col] == k){
                    ans++;
                }
            }
        }

        return ans;
    }

    // cumulative sum
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int[] sum = new int[nums.length + 1];
        sum[0] = 0;
        for (int i = 1; i <= nums.length; i++)
            sum[i] = sum[i - 1] + nums[i - 1];
        for (int start = 0; start < nums.length; start++) {
            for (int end = start + 1; end <= nums.length; end++) {
                if (sum[end] - sum[start] == k)
                    count++;
            }
        }
        return count;
    }

    // cumulative sum - without space
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.length; start++) {
            int sum=0;
            for (int end = start; end < nums.length; end++) {
                sum+=nums[end];
                if (sum == k)
                    count++;
            }
        }
        return count;
    }

    // cumulative sum - using hashmap
    public int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0;
        HashMap < Integer, Integer > map = new HashMap < > ();
        map.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            if (map.containsKey(sum - k))
                count += map.get(sum - k);
            map.put(sum, map.getOrDefault(sum, 0) + 1);
        }
        return count;
    }
}
