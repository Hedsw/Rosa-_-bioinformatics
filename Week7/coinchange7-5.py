
class Solution(object):
    def coinChange(coins, amount):
        dp = [0] + [float('inf')] * amount
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]
        

coins = [1,3,5,8,15,17,23]
amount = 19431

print(Solution.coinChange(coins, amount))