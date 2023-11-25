def longest_alternating_subsequence_length(arr):
    n = len(arr)
    
    # Initialize arrays to store lengths
    increase = [1] * n
    decrease = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                increase[i] = max(increase[i], decrease[j] + 1)
            elif arr[i] < arr[j]:
                decrease[i] = max(decrease[i], increase[j] + 1)

    # Find the maximum length among positive and negative subsequences
    max_length = max(max(increase), max(decrease))

    return max_length

# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 2, 5, 8]
result = longest_alternating_subsequence_length(arr)
print(result)  # Output: 9