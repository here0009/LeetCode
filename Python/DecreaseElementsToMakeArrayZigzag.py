"""
Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
Example 2:

Input: nums = [9,6,1,6,2]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        odd,even = 0,0
        len_nums = len(nums)
        for i in range(1,len(nums),2):
            #i is odd
            _tmp = nums[i]
            if i-1 >= 0:
                k = _tmp - nums[i-1]
                if k >= 0:
                    _tmp -= k+1
                    odd += k+1
            if i+1 < len_nums:
                k = _tmp - nums[i+1]
                if k >= 0:
                    odd += k+1

        for i in range(0,len(nums),2):
            #i is even
            _tmp = nums[i]
            if i-1 >= 0:
                k = _tmp - nums[i-1]
                if k >= 0:
                    _tmp -= k+1
                    even += k+1
            if i+1 < len_nums:
                k = _tmp - nums[i+1]
                if k >= 0:
                    even += k+1

        # print(odd,even)
        return min(odd, even)

s = Solution()
nums = [1,2,3]
print(s.movesToMakeZigzag(nums))

nums = [9,6,1,6,2]
print(s.movesToMakeZigzag(nums))
