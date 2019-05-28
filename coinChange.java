class Solution {
    public int coinChange(int[] coins, int amount) {
        if(amount < 1) return 0;
        int[] dp = new int[amount+1];
        for(int j=1; j <= amount; j++)
            dp[j] = Integer.MAX_VALUE;
        for(int i = 1; i <= amount; i++){
            for (int coin:coins) {
                if(i - coin >= 0){
                    dp[i] = Math.min(dp[i], (dp[i-coin] == Integer.MAX_VALUE) ? Integer.MAX_VALUE : dp[i-coin] + 1);
                }
            }
        }
      
        return (dp[dp.length - 1] == Integer.MAX_VALUE)? -1 : (int) dp[dp.length-1];
    }
}