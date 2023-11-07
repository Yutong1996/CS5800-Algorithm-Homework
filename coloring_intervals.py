'''
Let X be a set of n intervals on the real line. 
The input, for each 1 ≤ i ≤ n, specifies the start value si and the finish value fi of
interval i. A proper coloring of X assigns a color to each interval, so that any two overlapping
intervals are assigned different colors. Describe and analyze an efficient algorithm to compute
the minimum number of colors needed to properly color X. As before, if you use a greedy
algorithm, you must prove that it is correct.
'''

def min_num_color(intervals):

  if len(intervals) == 0:
    return 0
  intervals.sort(key = lambda x:(x[0], x[1]))
  result = 1
  num_color = 1

  for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i-1][1]:
      result += 1
      intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
    else:
      result = 1
    num_color = max(result, num_color)
  return num_color

intervals_1 = [[0,2], [3,4], [1,3], [5,7], [6,9], [6,7]]
result = min_num_color(intervals_1)
print(result)