"""
给定一个整数数组，找出总和最大的连续数列，并返回总和。

示例：

输入： [-2,1,-3,4,-1,2,1,-5,4]
输出： 6
解释： 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶：

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-sequence-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        preSum = [0]
        tmp = 0
        res = -float('inf')
        for num in nums:
            tmp += num
            preSum.append(tmp)
            # res = max(res, tmp)
        stack = []
        idx = 0
        # print(preSum)
        while idx < len(preSum):
            if stack:
                res = max(res, preSum[idx] - stack[0])
            while stack and preSum[idx] <= stack[-1]:
                stack.pop()
            # print(stack)
            stack.append(preSum[idx])
            idx += 1
        return res

S = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(S.maxSubArray(nums))
nums = [1]
print(S.maxSubArray(nums))
nums = [0]
print(S.maxSubArray(nums))
nums = [-2,-1]
print(S.maxSubArray(nums))