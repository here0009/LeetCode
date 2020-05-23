"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""
class Solution_1:
    """
    Thoughts: time exceed, try to sort pre_sums
    """
    def subarraySum(self, nums, k: int) -> int:
        pre_sums = []
        tmp = 0
        res = 0
        for n in nums:
            tmp += n
            pre_sums.append(tmp)
            if tmp == k:
                res += 1

        # print(pre_sums)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                # print(i,j)
                # print('----')
                # print(pre_sums[i],pre_sums[j])
                if pre_sums[j] - pre_sums[i] == k:
                    res += 1
        return res

from collections import Counter
class Solution:
    """
    Thoughts: got the wrong answer, because the order of pre_sums do matters, k can only obtained by the latter minus the previous pre_sums. if you use a dict to store pre_sums, there will be no orders.
    """
    def subarraySum(self, nums, k: int) -> int:
        pre_sums = []
        tmp = 0
        res = 0
        for n in nums:
            tmp += n
            pre_sums.append(tmp)
            if tmp == k:
                res += 1

        pre_sums_dict = Counter(pre_sums)
        print(pre_sums_dict)
        for n in pre_sums_dict:
            target = k + n
            # if target == n:

            if target in pre_sums_dict:
                if target == n:
                    res += pre_sums_dict[target]-1
                else:
                    res += pre_sums_dict[target]
        return res


class Solution:
    """
    we can use a dict updated by the sequence, so only latter ones minus previous ones
    """
    def subarraySum(self, nums, k: int) -> int:
        pre_sums_dict = {0:1}
        pre_sum = 0
        res = 0
        for n in nums:
            pre_sum += n
            target = pre_sum - k
            if target in pre_sums_dict:
                res += pre_sums_dict[target]
            pre_sums_dict[pre_sum] = pre_sums_dict.get(pre_sum,0) + 1
        return res

s = Solution()
nums = [1,1,1]
k = 2
print(s.subarraySum(nums,k))

nums = [1]
k = 2
print(s.subarraySum(nums,k))

nums = [2]
k = 2
print(s.subarraySum(nums,k))


nums = [1]
k = 0
print(s.subarraySum(nums,k))

nums = [-1,-1,1]
k = 1
print(s.subarraySum(nums,k))