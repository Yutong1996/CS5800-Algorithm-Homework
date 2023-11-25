def majorityElement(nums):
    def majority_element_divide_conquer(left, right):
        # Base case: If the array has only one element, it is the majority element.
        if left == right:
            return nums[left]

        # Divide the array into two halves.
        mid = (left + right) // 2

        # Recursively find the majority elements in the left and right subarrays.
        left_majority = majority_element_divide_conquer(left, mid)
        right_majority = majority_element_divide_conquer(mid + 1, right)

        # If the left and right subarrays have the same majority element, return it.
        if left_majority == right_majority:
            return left_majority

        # Count the occurrences of the left and right majority elements in the entire array.
        left_count = sum(1 for i in range(left, right + 1) if nums[i] == left_majority)
        right_count = sum(1 for i in range(left, right + 1) if nums[i] == right_majority)

        # Return the majority element with the higher count.
        return left_majority if left_count > right_count else right_majority

    return majority_element_divide_conquer(0, len(nums) - 1)

# Example 1
nums1 = [3, 2, 3]
print(majorityElement(nums1))  # Output: 3

# Example 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums2))  # Output: 2

# Example 3
nums2 = [1, 3, 1, 1, 1, 2, 2]
print(majorityElement(nums2))  # Output: 2