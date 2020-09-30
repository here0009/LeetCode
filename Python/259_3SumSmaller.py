"""
Given an array of n integers nums and an integer target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Follow up: Could you solve it in O(n2) runtime?

 

Example 1:

Input: nums = [-2,0,1,3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
[-2,0,1]
[-2,0,3]
Example 2:

Input: nums = [], target = 0
Output: 0
Example 3:

Input: nums = [0], target = 0
Output: 0
 

Constraints:

n == nums.length
0 <= n <= 300
-100 <= nums[i] <= 100
-100 <= target <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-smaller
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:
        nums.sort()
        length = len(nums)
        res = 0
        for i in range(length-2):
            for j in range(i+1, length-1):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] < target:
                        res += 1
                    else:
                        break
        return res


class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:
        two_sums = dict()
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                two_sums[(i,j)] = nums[i] + nums[j]

        res = 0
        for i in range(length-2):
            for k, v in two_sums.items():
                if k[0] > i and nums[i] + v < target:
                    res += 1
        return res


class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:
        """
        two pointer, optimize at the function of twoSumSmaller, O(N)
        """
        def twoSumSmaller(left, right, target):
            res = 0
            while left < right:
                if nums[left] + nums[right] < target:
                    res += right-left
                    left += 1
                else:
                    right -= 1
            return res

        nums.sort()
        length = len(nums)
        res = 0
        for i in range(length-2):
            res += twoSumSmaller(i+1, length-1, target-nums[i])
        return res


S = Solution()
nums = [-2,0,1,3]
target = 2
print(S.threeSumSmaller(nums, target))
nums = []
target = 0
print(S.threeSumSmaller(nums, target))
nums = [0]
target = 0
print(S.threeSumSmaller(nums, target))
nums = [3,1,0,-2]
target = 4
print(S.threeSumSmaller(nums, target))
