"""
给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。

示例 1：

输入：nums = [2,3,3,2,3,3]

输出：2

解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。

示例 2：

输入：nums = [2,3,5,7]

输出：4

解释：只有一种可行的切割：[2], [3], [5], [7]

限制：

1 <= nums.length <= 10^5
2 <= nums[i] <= 10^6
"""
from collections import defaultdict
from functools import lru_cache
class Solution:
    def splitArray(self, nums) -> int:
        next_index = defaultdict(list) #next_index[i] stores the index of nums that got the same gcd of nums[i]
        def gcd(p,q):
            if p < q:
                return gcd(q,p)
            while p % q != 0:
                p, q = p//q, p%q
            return q

        @lru_cache(None)
        def dfs(index):
            """
            return the min group from nums[index:]
            """
            # print(index)
            if index >= length:
                return 0
            if not next_index[index]:
                return  1+dfs(index+1)
            return min(1+dfs(j+1) for j in next_index[index])

        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if gcd(nums[i],nums[j]) != 1:
                    next_index[i].append(j)

        return dfs(0)
        # print(next_index)

class Solution:
    def splitArray(self, nums) -> int:
        def gcd(p,q):
            if p < q:
                return gcd(q,p)
            while p % q != 0:
                p, q = p//q, p%q
            return q

        stack = []
        for num in nums:
            while stack and gcd(stack[-1],num) != 1:
                stack.pop()
            stack.append(num)

        next_index = defaultdict(list)

        @lru_cache(None)
        def dfs(index):
            """
            return the min group from nums[index:]
            """
            # print(index)
            if index >= length:
                return 0
            if not next_index[index]:
                return  1+dfs(index+1)
            return min(1+dfs(j+1) for j in next_index[index])

        length = len(stack)
        for i in range(length-1):
            for j in range(i+1, length):
                if gcd(stack[i],stack[j]) != 1:
                    next_index[i].append(j)

        return dfs(0)

def gcd(p,q):
    if p < q:
        return gcd(q,p)
    while p % q != 0:
        p, q = p//q, p%q
    return q
# print(gcd(3,6))
# print(gcd(2,4))
# print(gcd(2,3))
# print(gcd(3,2))
# print(gcd(2,2))
S = Solution()
nums = [2,3,3,2,3,3]
print(S.splitArray(nums))

nums = [2,3,5,7]
print(S.splitArray(nums))