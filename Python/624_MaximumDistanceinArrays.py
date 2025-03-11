"""
You are given m arrays, where each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|. Your task is to find the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0
Example 3:

Input: arrays = [[1],[2]]
Output: 1
Example 4:

Input: arrays = [[1,4],[0,5]]
Output: 4
 

Constraints:

m == arrays.length
2 <= m <= 104
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.

"""


class Solution:
    def maxDistance(self, arrays) -> int:
        t_min, t_max = float('inf'), -float('inf')
        res = -float('inf')
        for lst in arrays:
            minv, maxv = lst[0], lst[-1]
            res = max(res, maxv - t_min, t_max - minv)
            t_max = max(maxv, t_max)
            t_min = min(minv, t_min)
        return res


S = Solution()
arrays = [[1,2,3],[4,5],[1,2,3]]
print(S.maxDistance(arrays))
arrays = [[1],[1]]
print(S.maxDistance(arrays))
arrays = [[1],[2]]
print(S.maxDistance(arrays))
arrays = [[1,4],[0,5]]
print(S.maxDistance(arrays))