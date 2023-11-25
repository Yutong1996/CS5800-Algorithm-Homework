'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number 
sorted in non-decreasing order.
'''


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        mylist = list(map(lambda x: x*x, nums))
        mylist.sort()
        return mylist