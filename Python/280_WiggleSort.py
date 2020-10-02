"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/wiggle-sort
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def dfs(index, flag):
            """
            if flag is 1, swap nums[index-1:index+1] to inorder
            else, swap to reverse order
            if index == length:
                return True
            """
            if index == length or length == 0:
                return True
            if (flag == 1 and nums[index-1] < nums[index]) or (flag == 0 and nums[index-1] > nums[index]):
                nums[index-1], nums[index] = nums[index], nums[index-1]
            dfs(index+1, 1-flag)

        length = len(nums)
        if not dfs(1, 1):
            dfs(1, 0)
        print(nums)

class Solution:
    def wiggleSort(self, nums) -> None:
        nums.sort()
        index = 0
        length = len(nums)
        while index+1 < length:
            nums[index], nums[index+1] = nums[index+1], nums[index]
            index += 2
        # print(nums)

S = Solution()
nums = [3,5,2,1,6,4]
print(S.wiggleSort(nums))
