class ContainerWithMostWater0011 {
    public int maxArea(int[] height) {
        int maxArea = 0;
        int l = 0;
        int r = height.length - 1;

        while (l < r){
            maxArea = Math.max(maxArea, Math.min(height[l], height[r]) * (r-l));
            if (height[l] > height[r]){
                r--;
            }
            else {
                l++;
            }
        }

        return maxArea;

    }
}
