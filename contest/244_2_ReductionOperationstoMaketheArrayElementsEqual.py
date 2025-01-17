"""
Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal.

 

Example 1:

Input: nums = [5,1,3]
Output: 3
Explanation: It takes 3 operations to make all elements in nums equal:
1. largest = 5 at index 0. nextLargest = 3. Reduce nums[0] to 3. nums = [3,1,3].
2. largest = 3 at index 0. nextLargest = 1. Reduce nums[0] to 1. nums = [1,1,3].
3. largest = 3 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1].
Example 2:

Input: nums = [1,1,1]
Output: 0
Explanation: All elements in nums are already equal.
Example 3:

Input: nums = [1,1,2,2,3]
Output: 4
Explanation: It takes 4 operations to make all elements in nums equal:
1. largest = 3 at index 4. nextLargest = 2. Reduce nums[4] to 2. nums = [1,1,2,2,2].
2. largest = 2 at index 2. nextLargest = 1. Reduce nums[2] to 1. nums = [1,1,1,2,2].
3. largest = 2 at index 3. nextLargest = 1. Reduce nums[3] to 1. nums = [1,1,1,1,2].
4. largest = 2 at index 4. nextLargest = 1. Reduce nums[4] to 1. nums = [1,1,1,1,1].
 

Constraints:

1 <= nums.length <= 5 * 104
1 <= nums[i] <= 5 * 104
"""


from typing import List
# import heapq
from collections import Counter
# class Solution:
#     def reductionOperations(self, nums: List[int]) -> int:

#         counts = Counter(nums)
#         pq = [(-v, c) for v, c in counts.items()]
#         if len(pq) == 1:
#             return 0
#         heapq.heapify(pq)
#         min_val = min(counts.values())
#         res = 0
#         while pq[0][0] != -min_val:
#             v, c = 

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:        
        counts = Counter(nums)
        val_counts = [(v, c) for v, c in counts.items()]
        if len(val_counts) == 0:
            return 0
        val_counts.sort(reverse = True)
        # print(val_counts)
        res = 0
        tmp = 0
        for i in range(len(val_counts) - 1):
            tmp += val_counts[i][1]
            res += tmp
        return res


S = Solution()
nums = [5,1,3]
print(S.reductionOperations(nums))
nums = [1,1,1]
print(S.reductionOperations(nums))
nums = [1,1,2,2,3]
print(S.reductionOperations(nums))
nums = [7,9,10,8,6,4,1,5,2,3]
print(S.reductionOperations(nums))
# 输出：
# 511
# 预期：
# 45
