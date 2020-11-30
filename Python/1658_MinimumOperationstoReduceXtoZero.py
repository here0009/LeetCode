"""
You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
1 <= x <= 109
"""


from functools import lru_cache
class Solution:
    def minOperations(self, nums, x: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(i,j,val):
            """
            min operations to get val from nums[i:j+1]
            """
            # print(nums[i:j+1], val)
            if i > j or val < 0:  # i == j+1 means remove nums[i], empty sequece
                return float('inf')
            if val == 0:
                return 0
            total = preSum[j+1] - preSum[i]
            if total == val:
                return j-i+1
            if total < val:
                return float('inf')
            return 1 + min(dp(i+1, j, val-nums[i]), dp(i, j-1, val-nums[j]))


        # print(nums, len(nums))
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        res = dp(0, len(nums)-1, x)
        return res if res != float('inf') else -1


from functools import lru_cache
class Solution:
    def minOperations(self, nums, x: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return float('inf')
            tmp = preSum[j] - preSum[i]
            if tmp < target:
                return float('inf')
            if tmp == target:
                return length - (j-i)
            return min(dp(i+1, j), dp(i, j-1))
            
        length = len(nums)
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)
        total = preSum[-1]
        target = total - x
        # self.res = float('inf')
        res = dp(0, length)
        return res if res != float('inf') else -1



from functools import lru_cache
class Solution:
    def minOperations(self, nums, x: int) -> int:
        length = len(nums)
        total = sum(nums)
        target = total - x
        preSum = [0]
        index_dict = {0:-1}
        res = -1
        # print(target)
        for i, v in enumerate(nums):
            tmp = preSum[-1] + v
            preSum.append(tmp)
            if tmp not in index_dict:
                index_dict[tmp] = i
            if tmp - target in index_dict:
                res = max(res, i - index_dict[tmp - target])

        return length- res if res != -1 else -1



S = Solution()
nums = [1,1,4,2,3]
x = 5
print(S.minOperations(nums, x))
nums = [5,6,7,8,9]
x = 4
print(S.minOperations(nums, x))
nums = [3,2,20,1,1,3]
x = 10
print(S.minOperations(nums, x))

nums = [8828,9581,49,9818,9974,9869,9991,10000,10000,10000,9999,9993,9904,8819,1231,6309]
x = 134365
print(S.minOperations(nums, x))

# 输出：
# -1
# 预期：
# 16

nums  = [1,1]
x = 3
print(S.minOperations(nums, x))