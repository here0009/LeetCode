"""
小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

示例 1：

输入：nums = [2,5,3,5], target = 6

输出：1

解释：预算内仅能购买 nums[0] 与 nums[2]。

示例 2：

输入：nums = [2,2,1,9], target = 10

输出：4

解释：符合预算的采购方案如下：
nums[0] + nums[1] = 4
nums[0] + nums[2] = 3
nums[1] + nums[2] = 3
nums[2] + nums[3] = 10

提示：

2 <= nums.length <= 10^5
1 <= nums[i], target <= 10^5
"""


from typing import List
from bisect import bisect_right
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        M = 10**9 + 7
        res = 0
        for i, v in enumerate(nums):
            t = target - v
            idx = bisect_right(nums[i + 1:], t)
            if idx <= 0:
                break
            res += idx
            res = res % M
        return res % M


from typing import List
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        M = 10**9 + 7
        res = 0
        left, right = 0, len(nums) - 1
        while left < right:
            while right > left and nums[right] + nums[left] > target:
                right -= 1
            res += right - left
            res = res % M
            left += 1
        return res

S = Solution()
nums = [2,5,3,5]
target = 6
print(S.purchasePlans(nums, target))
nums = [2,2,1,9]
target = 10
print(S.purchasePlans(nums, target))