"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""
from functools import lru_cache
class Solution:
    def jump(self, nums) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def minJump(index):
            """
            min jump to the last index 
            """
            if index == target:
                return 0
            steps = float('inf')
            for i in range(1, nums[index]+1):
                if index+i <= target:
                    steps = min(steps, 1+minJump(index+i))
                else:
                    break
            # print(index, steps)
            return steps


        target = len(nums)-1
        return minJump(0)

class Solution:
    def jump(self, nums) -> int:
        """
        the 1st jump can reach from 0 to nums[0], so the min jump to nums[0] is 1.
        the second jump can reach max(i+nums[i] for i in range(1,nums[0]))
        find until reaches len(nums)-1
        """
        left, right, steps = 0, 0, 0
        while right < len(nums)-1:
            nxt_right = max([i+nums[i] for i in range(left, right+1)])
            left, right = right, nxt_right
            steps += 1
        return steps

S = Solution()
nums = [2,3,1,1,4]
print(S.jump(nums))

nums = [2,1]

print(S.jump(nums))

nums = [0]
print(S.jump(nums))