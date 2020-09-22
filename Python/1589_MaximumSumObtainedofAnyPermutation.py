"""
We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.

Return the maximum total sum of all requests among all permutations of nums.

Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
Output: 19
Explanation: One permutation of nums is [2,1,3,4,5] with the following result: 
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
Total sum: 8 + 3 = 11.
A permutation with a higher total sum is [3,5,4,2,1] with the following result:
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
Total sum: 11 + 8 = 19, which is the best that you can do.
Example 2:

Input: nums = [1,2,3,4,5,6], requests = [[0,1]]
Output: 11
Explanation: A permutation with the max total sum is [6,5,4,3,2,1] with request sums [11].
Example 3:

Input: nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
Output: 47
Explanation: A permutation with the max total sum is [4,10,5,3,2,1] with request sums [19,18,10].
 

Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i] <= 105
1 <= requests.length <= 105
requests[i].length == 2
0 <= starti <= endi < n
"""


class Solution:
    def maxSumRangeQuery(self, nums, requests) -> int:
        """
        TLE
        """
        M = 10**9 +7
        counts = [0]*len(nums)
        for i, j in requests:
            for k in range(i, j+1):
                counts[k] += 1
        nums = sorted(nums, reverse=True)
        counts = sorted(counts, reverse=True)
        return sum(n*c for n, c in zip(nums, counts)) % M

from collections import Counter
class Solution:
    def maxSumRangeQuery(self, nums, requests) -> int:
        """
        still TLE
        """
        M = 10**9 +7
        counts = Counter()
        for i, j in requests:
            for k in range(i, j+1):
                counts[k] += 1
        length = len(counts)
        nums = sorted(nums, reverse=True)
        nums = nums[:length]
        counts_v = sorted(counts.values(), reverse=True)
        return sum(n*c for n, c in zip(nums, counts_v)) % M


# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/discuss/854206/JavaC%2B%2BPython-Sweep-Line
class Solution:
    def maxSumRangeQuery(self, nums, requests) -> int:
        """
        sweep line
        """
        M = 10**9 +7
        length = len(nums)
        counts = [0]*(length+1)
        for i, j in requests:
            counts[i] += 1
            counts[j+1] -= 1
        for i in range(1, length+1):
            counts[i] += counts[i-1]
        counts = sorted(counts[:-1], reverse=True)
        nums = sorted(nums, reverse=True)
        return sum(n*c for n,c in zip(nums, counts)) % M

S = Solution()
nums = [1,2,3,4,5]
requests = [[1,3],[0,1]]
print(S.maxSumRangeQuery(nums, requests))
nums = [1,2,3,4,5,6]
requests = [[0,1]]
print(S.maxSumRangeQuery(nums, requests))
nums = [1,2,3,4,5,10]
requests = [[0,2],[1,3],[1,1]]
print(S.maxSumRangeQuery(nums, requests))

