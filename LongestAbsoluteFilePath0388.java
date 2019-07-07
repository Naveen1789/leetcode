class LongestAbsoluteFilePath0388 {
    public int lengthLongestPath(String input) {
        String[] strArr = input.split("\n");

        int ans = 0;

        Stack<Integer> st = new Stack<Integer>();
        st.push(0);

        for (String fileOrDir : strArr){
            int level = fileOrDir.lastIndexOf('\t') + 1;
            int len = fileOrDir.length() - level;

            while (st.size() > level+1){
                st.pop();
            }
            boolean isFile = fileOrDir.contains(".");
            if (isFile){
                ans = Math.max(ans, st.peek() + len);
            }
            else {
                st.push(st.peek() + 1 + len);
            }
        }

        return ans;
    }
}
