class CoinChange0322 {

    // public int coinChange(int[] coins, int amount) {
    //     int[] dp = new int[amount+1];
    //
    //     Arrays.fill(dp, amount+1);
    //     dp[0] = 0;
    //
    //     for(int i = 1; i <= amount; i++){
    //         for (int j = 0; j < coins.length; j++){
    //             if (coins[j] <= i){
    //                 dp[i] = Math.min(dp[i], dp[i-coins[j]] + 1);
    //             }
    //         }
    //     }
    //
    //     return (dp[amount] > amount) ? -1 : dp[amount];
    // }
    
    public int coinChange(int[] coins, int amount) {
        if (amount <= 0){
            return 0;
        }

        return coinChangeHelper(coins, amount, new int[amount]);

    }

    public int coinChangeHelper(int[] coins, int remAmount, int[] dp){

        if (remAmount <= 0){
            return remAmount;
        }
        if (dp[remAmount-1] != 0){
            return dp[remAmount-1];
        }

        int min = Integer.MAX_VALUE;
        for (int c : coins){
            int res = coinChangeHelper(coins, remAmount - c, dp);
            if (res >= 0 && res < min){
                min = 1 + res;
            }
        }
        dp[remAmount-1] = (min == Integer.MAX_VALUE) ? -1 : min;

        return dp[remAmount-1];
    }
}
