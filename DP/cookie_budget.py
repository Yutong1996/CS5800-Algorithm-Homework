class Solution:
    def cookiesBudget(self, cookie: list[int], B: int):
        n = len(cookie)
        dp = [float("-inf")] * (B + 1) 
        dp[0] = 0 

        for i in range(1, B + 1):  
            for j in range(n): 
                if dp[i - cookie[j]] is not float("-inf"): 
                    dp[i] = max(dp[i - cookie[j]] + 1, dp[i])  

        if dp[B] == float("-inf"):  
            return "Impossible"
        print(dp)
        return dp[B] 


# Example usage
cookie = [2, 5]
sol = Solution()
result = sol.cookiesBudget(cookie, 9)
print(result)  # Output: 3
