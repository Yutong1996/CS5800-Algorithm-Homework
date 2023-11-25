'''
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number 
of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        hashmap = dict()
        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1+n2] = hashmap.get(n1+n2, 0) + 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                k = 0-(n3+n4)
                if k in hashmap:
                    count += hashmap[k]
        return count