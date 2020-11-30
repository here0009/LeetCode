"""
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

 

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]
Example 3:

Input: nums = [[10,10],[11,11]]
Output: [10,11]
Example 4:

Input: nums = [[10],[11]]
Output: [10,11]
Example 5:

Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]
 

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
"""


from typing import List
from bisect import insort
from collections import deque
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        dq = deque(sorted([(nums[i][0], i, 0) for i in range(k)]))
        res = [dq[0][0], dq[-1][0]]
        diff_min = res[1] - res[0]
        while True:
            # print([i[0] for i in dq], res)
            num, i, j = dq.popleft()
            j += 1
            if j == len(nums[i]):
                break
            insort(dq, (nums[i][j], i, j))
            if dq[-1][0] - dq[0][0] < diff_min:
                diff_min = dq[-1][0] - dq[0][0]
                res = [dq[0][0], dq[-1][0]]
        return res


import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        pq = sorted([(nums[i][0], i, 0) for i in range(k)])
        min_v, max_v = pq[0][0], pq[-1][0]
        diff_min = max_v - min_v
        res = [min_v, max_v]
        # print(pq)
        while True:
            # print(pq)
            num, i, j = heapq.heappop(pq)
            j += 1
            if j == len(nums[i]):
                break
            if nums[i][j] > max_v:
                max_v = nums[i][j]
            heapq.heappush(pq, (nums[i][j], i, j))
            min_v = pq[0][0]
            # print(pq, max_v, min_v)
            if max_v - min_v < diff_min:
                diff_min = max_v - min_v
                res = [min_v, max_v]
        return res

from collections import Counter
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        mergedNums = sorted([(nums[i][j],i) for i in range(k) for j in range(len(nums[i]))])
        # print(mergedNums)
        left = 0
        res = [mergedNums[0][0], mergedNums[-1][0]]
        diff = res[1] - res[0]
        counts = Counter()
        for right in range(len(mergedNums)):
            v, i = mergedNums[right]
            counts[i] += 1
            while len(counts) == k and counts[mergedNums[left][1]] > 1:
                counts[mergedNums[left][1]] -= 1
                left += 1
            if len(counts) == k and mergedNums[right][0] - mergedNums[left][0] < diff:
                diff = mergedNums[right][0] - mergedNums[left][0]
                res = [mergedNums[left][0], mergedNums[right][0]]
        return res


S = Solution()
nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
print(S.smallestRange(nums))
nums = [[1,2,3],[1,2,3],[1,2,3]]
print(S.smallestRange(nums))
nums = [[10,10],[11,11]]
print(S.smallestRange(nums))
nums = [[10],[11]]
print(S.smallestRange(nums))
nums = [[1],[2],[3],[4],[5],[6],[7]]
print(S.smallestRange(nums))
nums = [[11,38,83,84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]
print(S.smallestRange(nums))