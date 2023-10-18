'''
Give a Θ(n log n) time divide and conquer algorithm that given an array A of n integers, finds two indices i < j 
such that A[j] - A[i] is maximized. Analyze and show that your algorithm runs in the required Θ(n log n) time.
'''
def findMin(arr, low, high):
  min = arr[low]
  for i in range(low + 1, high + 1):
    if arr[i] < min:
       min = arr[i]
  return min

def findMax(arr, low, high):
  max = arr[low]
  for i in range(low + 1, high + 1):
    if arr[i] > max:
      max = arr[i]
  return max

def find_max_difference(arr, l, r):
  if l >= r:
    return l, r, 0
  max_diff = float('-inf')
  mid = l + (r - l) // 2
  i1, j1, left_max_diff = find_max_difference(arr, l, mid)
  i2, j2, right_max_diff = find_max_difference(arr, mid+1, r)
  min_left = findMin(arr, l, mid)
  max_right = findMax(arr, mid + 1, r)
  max_diff = max(max(left_max_diff, right_max_diff), max_right - min_left)
  if left_max_diff == max_diff:
    return i1, j1, max_diff
  elif right_max_diff == max_diff:
    return i2, j2, max_diff
  else:
    i = arr.index(min_left)
    j = arr.index(max_right)
    return i, j, max_diff

# Example usage
arr = [4, 3, 10, 2, 9, 1, 6]
i, j, max_diff = find_max_difference(arr, 0, len(arr) - 1)
print(f"Indices i = {i}, j = {j}, Max Difference = {max_diff}")
# Indices i = 1, j = 2, Max Difference = 7
