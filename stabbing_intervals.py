'''
Let X be a set of n intervals on the realline. 
The input, for each 1 ≤ i ≤ n, specifies the start value si and the finish value fi of
interval i. We say that a set P of points stabs X if every interval in X contains at least one
point in P . Describe and analyze an efficient algorithm to compute the smallest set of points
that stabs X. As usual, If you use a greedy algorithm, you must prove that it is correct.
'''

def smallest_set_points(intervals):

  if len(intervals) == 0:
    return 0
  intervals.sort(key = lambda x:(x[0], x[1]))
  result = 1

  for i in range(1, len(intervals)):
    if intervals[i][0] > intervals[i-1][1]:
      result += 1
    else:
      intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
  return result

intervals_1 = [[0,2], [3,4], [1,3], [5,7], [6,9]]
result = smallest_set_points(intervals_1)
print(result)