"""
Given a non-decreasing array of positive integers nums and an integer K, find out if this array can be divided into one or more disjoint increasing subsequences of length at least K.

 

Example 1:

Input: nums = [1,2,2,3,3,4,4], K = 3
Output: true
Explanation: 
The array can be divided into the two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
Example 2:

Input: nums = [5,6,6,7,8], K = 3
Output: false
Explanation: 
There is no way to divide the array using the conditions required.
 

Note:

1 <= nums.length <= 10^5
1 <= K <= nums.length
1 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-array-into-increasing-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def canDivideIntoSubsequences(self, nums, K: int) -> bool:
        counts = Counter(nums)
        v_counts = Counter(counts.values())
        total = 0
        max_key = 0
        for key, val in v_counts.items():
            max_key = max(max_key, key)
            total += key*val
        max_key_total = max_key*v_counts[max_key]
        return (total - max_key_total) - (K*max_key - max_key_total) >= 0
          


from collections import Counter
class Solution:
    def canDivideIntoSubsequences(self, nums, K: int) -> bool:
        """
        the most common elments should be allocatate to different group
        """
        counts = Counter(nums)
        max_v = max(counts.values())
        return max_v*K <= len(nums)

S = Solution()
nums = [1,2,2,3,3,4,4]
K = 3
print(S.canDivideIntoSubsequences(nums, K))
nums = [5,6,6,7,8]
K = 3
print(S.canDivideIntoSubsequences(nums, K))
