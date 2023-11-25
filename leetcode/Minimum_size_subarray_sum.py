'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
 '''


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum, left, right = 0, 0, 0
        n = len(nums)
        min_len = float('inf')
        while (right<n):
            sum += nums[right]

            while sum >= target:
                min_len = min(min_len, right-left+1)
                sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0