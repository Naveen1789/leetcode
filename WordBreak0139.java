class WordBreak0139 {

    // DP
    // public boolean wordBreak(String s, List<String> wordDict) {
    //     HashSet<String> set = new HashSet(wordDict);
    //     boolean[] dp = new boolean[s.length()+1];
    //     dp[0] = true;
    //
    //     for (int i = 1; i <= s.length(); i++){
    //         for (int j = 0; j < i; j++){
    //             if (dp[j] && set.contains(s.substring(j,i))){
    //                 dp[i] = true;
    //                 break;
    //             }
    //         }
    //     }
    //
    //     return dp[s.length()];
    // }
    public boolean wordBreak(String s, List<String> wordDict) {
        return wordBreakSubRoutine(s, 0, new Boolean[s.length()], new HashSet(wordDict));

    }

    public boolean wordBreakSubRoutine(String s, int start, Boolean[] memo, Set<String> dict){
        if (start == s.length()){
            return true;
        }

        if (memo[start] != null){
            return memo[start];
        }

        for (int end = start+1; end <= s.length(); end++){
            if (dict.contains(s.substring(start, end)) && wordBreakSubRoutine(s, end, memo, dict)){
                memo[start] = true;
                return true;
            }
        }

        memo[start] = false;
        return false;
    }
}
