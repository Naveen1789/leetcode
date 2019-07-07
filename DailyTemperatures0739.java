class DailyTemperatures0739 {
    public int[] dailyTemperatures(int[] T) {

        int[] ans = new int[T.length];

        ans[T.length - 1] = 0;

        Stack<Integer> st = new Stack<Integer>();
        st.push(T.length - 1);

        for(int i = T.length - 2; i >= 0; i--){
            while(!st.empty() && T[st.peek()] <= T[i]){
                st.pop();
            }

            ans[i] = (st.empty()) ? 0 : st.peek() - i;
            st.push(i);
        }
        return ans;
    }
}
