"""
给定一个数组，包含从 1 到 N 所有的整数，但其中缺了两个数字。你能在 O(N) 时间内只用 O(1) 的空间找到它们吗？

以任意顺序返回这两个数字均可。

示例 1:

输入: [1]
输出: [2,3]
示例 2:

输入: [2,3]
输出: [1,4]
提示：

nums.length <= 30000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-two-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        nums.extend([0, 0])
        for i, v in enumerate(nums):
            if v != -float('inf') and v != 0:
                idx = abs(v) - 1
                if nums[idx] == 0:
                    nums[idx] = -float('inf')
                else:
                    nums[idx] = - nums[idx]
            # print(nums)
        res = []
        for i, v in enumerate(nums):
            if v >= 0:
                res.append(i + 1)
        return res

S = Solution()
nums = [1]
print(S.missingTwo(nums))
nums = [2,3]
print(S.missingTwo(nums))