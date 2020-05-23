"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""
from bisect import bisect_left
class Solution_1:
    def triangleNumber(self, nums) -> int:
        res = 0
        nums = sorted(nums)
        len_n = len(nums)
        # print(nums)
        for f in range(len_n-2):
            for s in range(f+1, len_n-1):
                t = bisect_left(nums,nums[f]+nums[s])
                # print(nums[f],nums[s],nums[t-1],t-s-1)
                # if t-s-1 <= 0: #nums[s+1] >= nums[f] + nums[s]
                res += max(0,t-s-1)
        return res

class Solution:
    def triangleNumber(self, nums) -> int:
        res = 0
        nums = sorted(nums)
        len_n = len(nums)
        for t in range(2, len_n):
            f,s = 0, t-1
            while f < s:
                if nums[f] + nums[s] > nums[t]:
                    res += s-f
                    s -= 1
                else:
                    f += 1
        return res

S = Solution()
nums = [2,2,3,4]
print(S.triangleNumber(nums))
nums = [0,0,0]
print(S.triangleNumber(nums))


nums =[24,3,82,22,35,84,19]
print(S.triangleNumber(nums))
# Output
# 5
# Expected
# 10