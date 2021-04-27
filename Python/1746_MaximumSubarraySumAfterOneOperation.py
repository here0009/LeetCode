"""
You are given an integer array nums. You must perform exactly one operation where you can replace one element nums[i] with nums[i] * nums[i]. 

Return the maximum possible subarray sum after exactly one operation. The subarray must be non-empty.

 

Example 1:

Input: nums = [2,-1,-4,-3]
Output: 17
Explanation: You can perform the operation on index 2 (0-indexed) to make nums = [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17.
Example 2:

Input: nums = [1,-1,1,1,-1,-1,1]
Output: 4
Explanation: You can perform the operation on index 1 (0-indexed) to make nums = [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 = 4.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray-sum-after-one-operation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
import heapq
class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:

        curr = 0
        res = -float('inf')
        pq = [curr]
        pq_e = [curr]
        for num in nums:
            curr += num
            res = max(res, curr - pq[0])
            heapq.heappush(pq, curr)
        print(res, pq)
        return res


S = Solution()
nums = [2,-1,-4,-3]
print(S.maxSumAfterOperation(nums))
nums = [1,-1,1,1,-1,-1,1]
print(S.maxSumAfterOperation(nums))
