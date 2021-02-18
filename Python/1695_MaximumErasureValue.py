"""
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
"""


from typing import List
from collections import Counter, deque
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        tmp = 0
        counts = Counter()
        dq = deque([])
        for i, num in enumerate(nums):
            while dq and counts[num] > 0:
                j = dq.popleft()
                tmp -= nums[j]
                counts[nums[j]] -= 1
            counts[num] += 1
            dq.append(i)
            tmp += num
            res = max(res, tmp)
        return res

S = Solution()
nums = [4,2,4,5,6]
print(S.maximumUniqueSubarray(nums))
nums = [5,2,1,2,5,2,1,2,5]
print(S.maximumUniqueSubarray(nums))
nums = [187,470,25,436,538,809,441,167,477,110,275,133,666,345,411,459,490,266,987,965,429,166,809,340,467,318,125,165,809,610,31,585,970,306,42,189,169,743,78,810,70,382,367,490,787,670,476,278,775,673,299,19,893,817,971,458,409,886,434]
print(S.maximumUniqueSubarray(nums))
# 输出：
# 24864
# 预期：
# 16911