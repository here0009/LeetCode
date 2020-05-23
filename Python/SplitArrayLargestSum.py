"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
from functools import lru_cache
class Solution:
    def splitArray(self, nums, m: int) -> int:
        @lru_cache(None)
        def dp(index, k):
            """
            return the min value that split nums[index:] to k parts
            """
            if k == 1:
                return acc_nums[-1]-acc_nums[index]
            elif length - index == k:
                return max(nums[index:])
            res = float('inf')
            i = 0
            while length-(index+i) > k-1:
                i += 1 
                res = min(res, max(acc_nums[index+i]-acc_nums[index], dp(index+i, k-1)))
            return res

        acc_nums, curr_sum = [0], 0
        length = len(nums)
        for num in nums:
            curr_sum += num
            acc_nums.append(curr_sum)

        return dp(0,m)

"""
Binary search is faster
search the minimum value that can split nums to m parts
"""
class Solution:
    def splitArray(self, nums, m: int) -> int:
        def isValid(val):
            curr, counts = 0,1
            for n in nums:
                if curr+n <= val:
                    curr += n
                else:
                    curr = n
                    counts += 1
            # print('v,c',val, counts)
            return counts <= m


        low,hi = max(nums), sum(nums)
        while low < hi:
            # print(low,hi)
            mid = (low + hi)//2
            if isValid(mid):
                hi = mid
            else:
                low = mid+1
        return low


S = Solution()
nums = [7,2,5,10,8]
m = 2
print(S.splitArray(nums,m))