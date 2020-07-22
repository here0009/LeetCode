"""
Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
"""


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [[1, 1] for _ in range(length)]  # dp[i] = [the longest increasing subsequence end with i, the counts of ...]
        # print(dp)
        for i,v in enumerate(nums):
            j = i - 1
            while j>=0 and j+2 >= dp[i][0]:
                if v > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
                j -= 1
                # print(dp)
        max_val = max(v for v,c in dp)
        return sum(c for v, c in dp if v == max_val)


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        if not nums:
            return 0
        length = len(nums)
        subseqs = [1]*length
        counts = [1]*length
        for i, v in enumerate(nums):
            for j in range(i):
                if nums[j] < v:
                    if subseqs[j] + 1 > subseqs[i]:
                        subseqs[i] = subseqs[j] + 1
                        counts[i] = counts[j]
                    elif subseqs[j] + 1 == subseqs[i]:
                        counts[i] += counts[j]
        max_val = max(subseqs)
        # print(subseqs)
        # print(counts)
        return sum(c for v,c in zip(subseqs, counts) if v == max_val)

from collections import defaultdict
from collections import Counter
from bisect import bisect_left
class Solution:
    def findNumberOfLIS(self, nums) -> int:
        if not nums:
            return 0
        table = [float('-inf')]
        hash_table = defaultdict(Counter)
        hash_table[0][float('-inf')] = 1
        for num in nums:
            index = bisect_left(table, num)
            if index == len(table):
                table.append(num)
            else:
                table[index] = num
            hash_table[index][num] += sum(hash_table[index-1][val] for val in hash_table[index-1] if val < num)
        # print(hash_table)
        return sum(hash_table[len(table)-1].values())

# class Solution:
#     def findNumberOfLIS(self, nums):
#         dp = defaultdict(Counter)
#         dp[-1][-1e9] = 1
#         table = []
#         for i in nums:
#             index = bisect_left(table, i)
#             if index == len(table):
#                 table.append(i)
#             else:
#                 table[index] = i 
#             dp[index][i] += sum(dp[index-1][j] for j in dp[index-1] if j < i)
#         return sum(dp[max(0, len(table)-1)].values()) 



S = Solution()
nums = [1,3,5,4,7]
print(S.findNumberOfLIS(nums))
nums = [2,2,2,2,2]
print(S.findNumberOfLIS(nums))
nums = [2,1]
print(S.findNumberOfLIS(nums))
# Output
# 1
# Expected
# 2
nums = [1,2]
print(S.findNumberOfLIS(nums))