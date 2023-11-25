class Solution:
    def trampolineArena(self, T, D):
        n = len(T)
        dp = [0] * n
        dp[0] = D[0]
        for i in range(1, n):
            for j in range(i, -1, -1):
                if T[j] + D[j] <= T[i]:
                    dp[i] = max(dp[i - 1], D[i] + dp[j])
                    break
        return max(dp)
    
    def trampolineArenaFast(self, T, D):
        n = len(T)
        trampolines = [(T[i] + D[i], D[i]) for i in range(n)]  # Create a list of tuples (position, airtime distance)
        trampolines.sort()  # Sort the trampolines by their positions

        dp = [0] * n  # Initialize an array to store the maximum airtime distances
        dp[0] = D[0]
        for i in range(1, n):
            # Use binary search to find the index of the trampoline with the maximum position before the current trampoline
            index = self.binarySearch(trampolines[0:i], T[i])

            if index != -1:
                dp[i] = max(dp[i - 1], trampolines[i][1] + dp[index])  # Update the maximum airtime distance
        print(dp)
        return max(dp)  # Return the maximum airtime distance

    def binarySearch(self, trampolines, position):
        left, right = 0, len(trampolines) - 1

        while left <= right:
            mid = (left + right) // 2
            if trampolines[mid][0] <= position:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1  # Return the index of the trampoline with the maximum position before the current position


    def trampoline_k(self, T, D, k):
        n = len(T)
        dp = [[0] * k for _ in range(n)]
        for i in range(n):
            dp[i][0] = D[i]
        for x in range(k):
            dp[0][x] = D[0]
        

        for x in range(1, k):
            for i in range(1, n):
                for j in range(i):
                    if T[j] + D[j] <= T[i]:
                        dp[i][x] = max(dp[i][x], D[i] + dp[j][x - 1])
                        
        print(dp)
        return max(dp[i][k-1] for i in range(n))


T = [1, 3, 5, 7, 11, 15]
D = [2, 3, 4, 5, 3, 6]
sol = Solution()
result = sol.trampolineArena(T, D)
print(result)  # Output: 16

# Example usage
T = [1, 3, 5, 7, 11, 15]
D = [2, 3, 4, 5, 3, 6]
sol = Solution()
result = sol.trampolineArenaFast(T, D)
print(result)  # Output: 16

T = [1, 3, 5, 7, 11, 15]
D = [2, 3, 4, 5, 3, 6]
sol_1 = Solution()
result = sol_1.trampoline_k(T, D, 3)
print(result)
