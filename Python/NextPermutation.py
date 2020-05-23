"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution_1:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_flag = False
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
                swap_flag = True
                break
        if not swap_flag:
            nums = sorted(nums)
        print(nums)


"""
thoughts: find the 1st not rev order from the end(marked as index-1), sort from index, then swap index-1 with min(nums[index:])
"""
class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums)
        index = len(nums)-1
        while index > 0:
            if nums[index] > nums[index-1]:
                break
            index -= 1
        # print(index)
        if index == 0:
            nums.sort()
        else:
            # nums[index:].sort()
            for i in range(index, len(nums)-1):
                for j in range(i+1, len(nums)):
                    if nums[i] > nums[j]:
                        nums[i],nums[j] = nums[j], nums[i]
            # nums[index:] = sorted(nums[index:])
            # print(nums)
            tmp = index
            while tmp < len(nums)-1 and nums[index-1] >= nums[tmp] :
                tmp += 1
            nums[index-1], nums[tmp] = nums[tmp], nums[index-1]
            # print(index,tmp)
        # print(nums)


s = Solution()
nums = [1,2,3]
print(s.nextPermutation(nums))
nums = [3,2,1]
print(s.nextPermutation(nums))
nums = [1,1,5]
print(s.nextPermutation(nums))
nums = [1,2]
print(s.nextPermutation(nums))

nums = [1,3,2]
print(s.nextPermutation(nums))

nums = [2,3,1]
print(s.nextPermutation(nums))

nums = [1,5,1]
print(s.nextPermutation(nums))