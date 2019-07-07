class BestTimeToBuyAndSellStockWithCooldown0309 {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1){
            return 0;
        }

        // if you bought on day 1
        int boughtDMinus1 = -prices[0];

        // You can't sell on day 1
        // You had nothing prior to first day to sell
        int soldDMinus1 = 0;
        int soldDMinus2 = 0;

        for(int i = 1; i < prices.length; i++){
            // the last action at the end of day i was buy
            // a) you bought a stock on day i
            int temp1 = soldDMinus2 - prices[i];
            // b) the last action at the end of day i-1 was buy and you did nothing on day i
            int temp2 = boughtDMinus1;
            int boughtD = Math.max(temp1, temp2);

            // the last action at the end of day i was sell
            // a) you sold a stock on day i
            int temp3 = boughtDMinus1 + prices[i];
            // b) the last action at the end of day i-1 was sell and you did nothing on day i
            int temp4 = soldDMinus1;
            int soldD = Math.max(temp3, temp4);

            boughtDMinus1 = boughtD;
            soldDMinus2 = soldDMinus1;
            soldDMinus1 = soldD;
        }

        return soldDMinus1;
    }
}
