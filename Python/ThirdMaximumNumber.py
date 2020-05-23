"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""
class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        res = sorted(nums[:3], reverse = True)
        for num in nums[3:]:
            if num > res[-1]:
                res[-1] = num
                res = sorted(res, reverse = True)
        return res[-1]

s = Solution()
nums = [3,2,1]
print(s.thirdMax(nums))
nums = [1,2]
print(s.thirdMax(nums))
nums = [2,2,3,1]
print(s.thirdMax(nums))

