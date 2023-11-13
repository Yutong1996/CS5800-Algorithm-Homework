'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
'''



class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        return self.traverse(nums, 0, n - 1, target)

    def traverse(self, nums, left, right, target):
        if left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return self.traverse(nums, mid + 1, right, target)
            else:
                return self.traverse(nums, left, mid - 1, target)
        else:
            return -1  # If the target is not found in the array