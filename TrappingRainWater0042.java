class TrappingRainWater0042 {
    public int trap(int[] height) {

        if(height == null || height.length == 0){
            return 0;
        }

        int[] leftHighVals = new int[height.length];
        int[] rightHighVals = new int[height.length];

        int leftMax = height[0];
        for(int i = 0; i < height.length; i++){
            leftMax = Math.max(leftMax, height[i]);
            leftHighVals[i] = leftMax;
        }


        int rightMax = height[height.length-1];
        for(int i = height.length - 1; i >= 0; i--){
            rightMax = Math.max(rightMax, height[i]);
            rightHighVals[i] = rightMax;
        }

        int amountOfRainWaterTrapped = 0;
        for (int i = 0; i < height.length; i++){
            amountOfRainWaterTrapped = amountOfRainWaterTrapped + Math.min(leftHighVals[i], rightHighVals[i]) - height[i];
        }

        return amountOfRainWaterTrapped;
    }

    // Using stacks
    // public int trap(int[] height) {
    //
    //     int amountOfRainWaterTrapped = 0;
    //
    //     Stack<Integer> st = new Stack<Integer>();
    //
    //     int i = 0;
    //     while (i < height.length) {
    //         while (!st.empty() && height[i] > height[st.peek()]) {
    //             int middleBarIndex = st.pop();
    //             if (st.empty()){
    //                 break;
    //             }
    //             int distance = i - st.peek() - 1;
    //             int h = Math.min(height[i], height[st.peek()]) - height[middleBarIndex];
    //             amountOfRainWaterTrapped = amountOfRainWaterTrapped + (distance * h);
    //         }
    //         st.push(i);
    //         i++;
    //     }
    //
    //     return amountOfRainWaterTrapped;
    // }
}
