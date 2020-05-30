"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Solution:
    def canPartition(self, nums) -> bool:
        def dfs(index, currSum):
            if currSum == target:
                return True

            for i in range(index, length):
                if nums[index] == target:
                    return True
                if nums[index] > target:
                    return False
                if not visit[i] and currSum + nums[i] <= target:
                    visit[i] = 1
                    if dfs(i+1, currSum+nums[i]):
                        return True
                    visit[i] = 0
            return False

        nums = sorted(nums, reverse=True)
        length = len(nums)
        visit = [0]*length
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total //2
        # print(nums)
        # print(target)
        return dfs(0, 0)


class Solution_1:
    """
    wrong anw
    """
    def canPartition(self, nums) -> bool:
        def dfs(index):
            if index == length:
                return self.sum == target
            self.sum += nums[index]
            if self.sum <= target and dfs(index+1):
                return True
            self.sum -= nums[index]
            return False

        nums = sorted(nums, reverse=True)
        # print('nums:', nums)
        self.sum = 0
        target = sum(nums)/2
        length = len(nums)

        return dfs(0)

        
class Solution:
    def canFindSum(self, nums, target, ind, n, d):
        if target in d: 
            return d[target]
        if target == 0: 
            d[target] = True
        else:
            d[target] = False
            if target > 0:
                for i in range(ind, n):
                    if self.canFindSum(nums, target - nums[i], i+1, n, d):
                        d[target] = True
                        break
        return d[target]
    
    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s/2, 0, len(nums), {})


class Solution:
    def canPartition(self,nums):
        s, n, memo = sum(nums), len(nums), {0: True}
        if s & 1: return False  #odd
        nums.sort(reverse=True)
        def dfs(i, x):
            print(i,x,memo)
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        return dfs(0, s >> 1)

S = Solution()
# nums = [1, 5, 11, 5]
# print(S.canPartition(nums))
# nums = [1, 2, 3, 5]
# print(S.canPartition(nums))
nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100]

print(S.canPartition(nums))