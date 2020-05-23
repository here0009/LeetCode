"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
class Solution_1:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        pre = nums[0]
        index = 1
        unique = 1
        counts = 1
        while index < len(nums):
            if nums[index] == pre:
                counts += 1
                if counts <= 2:
                    nums[unique] = nums[index]
                    unique += 1   
            else:
                nums[unique] = nums[index]
                pre = nums[index]
                unique += 1
                counts = 1
            index += 1
        return unique

class Solution:
    def removeDuplicates(self, nums) -> int:
        unique = 0
        for index in range(len(nums)):
            if unique < 2 or nums[index] != nums[unique-2]:
                nums[unique] = nums[index]
                unique += 1
        return unique


s = Solution()
nums = [1,1,1,2,2,3]
print(s.removeDuplicates(nums))

nums = [0,0,1,1,1,1,2,3,3]
print(s.removeDuplicates(nums))