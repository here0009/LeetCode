"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
"""
class NumArray:

    def __init__(self, nums):
        self.nums = [0] + nums
        for i in range(1,len(nums)+1):
            self.nums[i] += self.nums[i-1]
        # print(self.nums)

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j+1]-self.nums[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))