class GenerateParentheses0022 {
    public List<String> generateParenthesis(int n) {
        ArrayList<String> ans = new ArrayList<String>();
        backtrack(ans, "", 0, 0, n);
        return ans;
    }

    public void backtrack(ArrayList<String> ans, String cur, int open, int close, int max){
        if (cur.length() == max * 2){
            ans.add(cur);
            return;
        }

        if (open < max){
            backtrack(ans, cur + "(", open+1, close, max);
        }
        if (close < open){
            backtrack(ans, cur + ")", open, close+1, max);
        }
    }
}
