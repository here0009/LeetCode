"""
数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。

示例 1：

输入：[1,2,5,9,5,9,5,5,5]
输出：5
 

示例 2：

输入：[3,2]
输出：-1
 

示例 3：

输入：[2,2,1,1,1,2,2]
输出：2
 

说明：
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-majority-element-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        idx, cnt, res = 1, 1, nums[0]
        while idx < len(nums):
            if nums[idx] == res:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res = nums[idx]
                    cnt = 1
            idx += 1
        # print(res)
        total = sum([res == num for num in nums])
        return res if total > len(nums) / 2 else -1

S = Solution()
nums = [1,2,5,9,5,9,5,5,5]
print(S.majorityElement(nums))
nums = [3,2]
print(S.majorityElement(nums))
nums = [2,2,1,1,1,2,2]
print(S.majorityElement(nums))