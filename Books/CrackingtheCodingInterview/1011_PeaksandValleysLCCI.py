"""
在一个整数数组中，“峰”是大于或等于相邻整数的元素，相应地，“谷”是小于或等于相邻整数的元素。例如，在数组{5, 8, 4, 2, 3, 4, 6}中，{8, 6}是峰， {5, 2}是谷。现在给定一个整数数组，将该数组按峰与谷的交替顺序排序。

示例:

输入: [5, 3, 1, 2, 3]
输出: [5, 1, 3, 2, 3]
提示：

nums.length <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/peaks-and-valleys-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        idx = 0
        while left <= right:
            if idx % 2 == 0:
                nums[idx] = sorted_nums[right]
                right -= 1
            else:
                nums[idx] = sorted_nums[left]
                left += 1
            idx += 1
        # print(nums)


from typing import List
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        对于每个位置，对于不符合要求的通过交换与其后一位的数值来满足题意。
        if i is valley , nums[i] > nums[i + 1], we can just swap nums[i] and nums[i + 1]. because i - 1 is peak and nums[i - 1] >= nums[i] have already satisfied by swapping nums[i - 1] and nums[i] or do nothing.
        so nums[i - 1] also >= nums[i + 1]
        """
        for i in range(len(nums) - 1):
            if i % 2 == 0 and nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
            elif i % 2 == 1 and nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        # print(nums)

S = Solution()
nums = [5, 3, 1, 2, 3]
print(S.wiggleSort(nums))