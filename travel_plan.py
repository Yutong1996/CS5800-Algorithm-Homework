class Solution:
    def optimalTravelPlan(self, T, k, S, C):
        dp = [[0 for _ in range(k)] for _ in range(T)]
        travel_plan = [[0 for _ in range(k)] for _ in range(T)]

        for i in range(k):
            dp[0][i] = S[0][i]

        for t in range(T):
            for i in range(k):
                dp[t][i] = max(dp[t][i], S[t][i] + dp[t - 1][i])
                travel_plan[t][i] = i
                for j in range(k):
                    if j is not i:
                        if dp[t - 1][j] - C[t][j][i] > dp[t][i]:
                            dp[t][i] = dp[t - 1][j] - C[t][j][i]
                            travel_plan[t][i] = j

        max_enjoy = max(dp[T-1])
    
        end_city = dp[T-1].index(max_enjoy)

        # Backtrack to find the optimal travel plan
        plan = []
        cur_city = end_city

        for t in range(T - 1, -1, -1):
            next_city = travel_plan[t][cur_city]
            if t == 0:
                # for the first day, we can simply stay in the city
                plan.insert(0, (t + 1, cur_city, 
                                f"Stay in city {cur_city + 1} and explore."))
            else:
                if cur_city == next_city:
                    # if today's city is the same as yesterday's, then we stayed in the city
                    plan.insert(0, (t + 1, cur_city, 
                                    f"Stay in city {cur_city + 1} and explore."))
                else:
                    # If today's city is different from yesterday's, then we moved to a new city
                    plan.insert(0, (t + 1, cur_city, 
                                    f"Move from city {next_city + 1} to city {cur_city + 1}."))
            cur_city = next_city
        return max_enjoy, plan

T = 5
k = 2
S = [[5, 1], [1, 2], [1, 6], [1, 2], [7, 2]]
C = [
    [[0, 1], [2, 0]],
    [[0, 1], [2, 0]],
    [[0, 2], [2, 0]],
    [[0, 3], [1, 0]],
    [[0, 1], [1, 0]]
]
sol = Solution()
max_enjoyment, plan = sol.optimalTravelPlan(T, k, S, C)

print("Maximum Enjoyment:", max_enjoyment)
print("Travel Plan:")
for day, city, action in plan:
    print(f"Day {day}: {action}")