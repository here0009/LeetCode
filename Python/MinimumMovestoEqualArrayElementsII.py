"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""
class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        middle_num = nums[len(nums)//2]
        return sum([abs(num - middle_num) for num in nums])


s = Solution()
nums = [1, 2, 3]
print(s.minMoves2(nums))
nums = [1, 2, 1]
print(s.minMoves2(nums))
nums = [1,0,0,8,6]
print(s.minMoves2(nums))