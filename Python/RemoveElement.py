"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""
class Solution:
    """
    wrong answer
    """
    def removeElement(self, nums, val: int) -> int:
        val_counts = 0
        start = 0
        len_nums = len(nums)
        for i in range(len(nums)):
            index = i
            while (nums[index] == val and index < len_nums-1):
                index += 1
                val_counts += 1
            if i + val_counts < len(nums):
                nums[i] = nums[i+val_counts]
        new_len = len(nums) - val_counts
        # for i in range(val_counts):
        #     nums.pop()
        print(nums)
        return new_len

class Solution_1:
    """
    Two pointers
    i record the final result 
    j record the proceding list, if num[j] == val, skip it assign to i
    """
    def removeElement(self, nums, val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


class Solution_2:
    """
    swap elements
    """
    def removeElement(self, nums, val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                n -= 1
            else:
                i+=1
        return n
        

s = Solution_2()
# s = Solution_2()
nums = [3,2,2,3]
val = 3
print(s.removeElement(nums,val))

nums = [0,1,2,2,3,0,4,2]
val = 2
print(s.removeElement(nums,val))

nums = [3,3,3]
val = 3
print(s.removeElement(nums,val))