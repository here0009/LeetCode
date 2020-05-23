"""
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.
"""
class Solution:
    def findPeakElement(self, nums) -> int:
        pre = float('-inf')
        for i,v in enumerate(nums):
            if v >= pre:
                pre = v
            else:
                return i-1
        return len(nums)-1


class Solution:
    def findPeakElement(self, nums) -> int:
        # nums = [float('-inf')] + nums +  [float('-inf')]
        def bisearch(left, right):
            if left == right:
                return left
            mid = (left + right)//2
            if nums[mid] < nums[mid+1]:
                return bisearch(mid+1, right)
            else:
                return bisearch(left, mid)
        k = bisearch(0,len(nums)-1)
        return k

s = Solution()
nums = [1,2,3,1]
print(s.findPeakElement(nums))

nums = [1,2,1,3,5,6,4]
print(s.findPeakElement(nums))

nums = [1]
print(s.findPeakElement(nums))

nums = [2,1,2]
print(s.findPeakElement(nums))
