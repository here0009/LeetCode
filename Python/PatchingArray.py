"""
Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
"""


class Solution:
    def minPatches(self, nums, n: int) -> int:
        while len(nums) > 1:
            n -= nums.pop()
        print(nums, n)


class Solution:
    def minPatches(self, nums, n: int) -> int:
        covered, res, index = 0, 0, 0
        length = len(nums)
        while covered < n:
            if index < length:
                num = nums[index]
            else:
                num = float('inf')
            if num > covered + 1:
                covered += covered + 1
                res += 1
            else:
                covered += num
                index += 1
        return res
            

S = Solution()
nums = [1,3]
n = 6
print(S.minPatches(nums, n))
nums = [1,5,10]
n = 20
print(S.minPatches(nums, n))
nums = [1,2,2]
n = 5
print(S.minPatches(nums, n))