'''
The price of a stock on each day is given to you in an array.
Assume you have enough money to buy a stock on all of the days. However, you cannot buy
if you already have a stock in hand (every buy must be followed by a sell before another
buy). To be more precise, on each day you have one of three options. You can either buy
exactly one share of the stock, sell exactly one share of the stock, or do nothing. However,
you can't buy any additional shares if you already possess one share, and you cannot sell
any shares if you don't possess one share. In other words, you can only have exactly 0 or 1
share at any given moment. A transaction is 1 buy followed by 1 sell. You can perform at
most K transactions.
As the manager of some traders in your company you want to come up with an algorithm
to find out the maximum profit your traders can possibly get by buying/selling the stock on
these days.
For example, if the given array is [100, 200, 250, 330, 40, 30, 700, 400], and K = 2 the
maximum profit can be earned by buying on day 1, selling on day 4, again buy on day 6 and
selling on day 7. As another example, if the given prices in the array keep decreasing, then
no profit can be earned. You only need to output the profit (a number).
Note: You need to use dynamic programming for this problem. Describe the subproblems
in English, specify the recursion (including the base case) needed for solving these subproblems, 
then write the pseudo-code (either topdown or bottom up). You also need to specify the
running time of your algorithm.
'''

class Solution:
    def max_profit(self, K, price):
        n = len(price)
        dp = [[0] * n for _ in range(K+1)]

        for i in range(1, K+1):
            for j in range(1, n):
                max_val = 0
                for m in range(j):
                    max_val = max(max_val, dp[i-1][m] - price[m]+price[j])
                dp[i][j] = max(dp[i][j-1], max_val)
        print(dp)
        return max(dp[K])

price = [100, 200, 250, 330, 40, 30, 700, 400]
sol = Solution()
result = sol.max_profit(2, price)
print(result)
