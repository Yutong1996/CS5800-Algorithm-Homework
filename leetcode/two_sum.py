'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add 
up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, value in enumerate(nums):
            if target - value in nums:
                if nums.index(target - value) != index:
                    return [nums.index(target - value), index]
        return []
    
    def twoSumUsingMap(self, nums: list[int], target: int) -> list[int]:
        record = dict()
        for index, value in enumerate(nums):
            if target - value in record:
                return [record[target-value], index]
            else:
                record[value] = index
        return []