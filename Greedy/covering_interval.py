"""
Let X be a set of n intervals on the real line. The input, for each 1 ≤ i ≤ n, specifies the 
start value si and the finish value fi of interval i. We say that a subset of intervals Y ⊆ X 
covers X if the union of all intervals in Y is equal to the union of all intervals in X . The 
size of a cover is just the number of intervals. Describe and analyze an efficient algorithm 
to compute the smallest cover of X. If you use a greedy algorithm, you must prove that it is 
correct.
"""


def num_interval(intervals):
  intervals = list(intervals)
  if len(intervals) == 0:
    return 0
  intervals.sort(key=lambda x: (x[0], -x[1]))
  result = 1
  cur = intervals[0][1]
  next_cover = float('-inf')
  max_f = max(intervals[i][1] for i in range(len(intervals)))
  for i in range(len(intervals)):
    if next_cover > cur:
      if intervals[i][0] == cur:
        result += 1
        cur = max(next_cover, intervals[i][1])
      elif intervals[i][0] > cur:
        result += 1
        if intervals[i][0] > next_cover:
          result += 1
          cur = intervals[i][1]
        cur = next_cover

      if cur >= max_f:
        break
    next_cover = max(next_cover, intervals[i][1])
  return result

# Test case:
intervals_1 = {(0, 2), (1, 2), (2, 3), (1, 4)}
result = num_interval(intervals_1)
print(result)

intervals = [(1, 4), (2, 3), (3, 6), (7, 8), (8, 10)]
smallest_cover = num_interval(intervals) 
print(smallest_cover)

intervals = [(1, 5), (2, 6), (3, 7), (8, 10), (9, 12)]
smallest_cover = num_interval(intervals)
print(smallest_cover)

intervals = [(1, 3), (2, 5), (4, 6), (7, 9), (8, 11), (10, 12)]
smallest_cover = num_interval(intervals)
print(smallest_cover)