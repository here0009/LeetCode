"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
"""
Thoughts:backtrack
"""
class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        def dfs(tmp):
            if len(tmp) == k:
                # print(tmp)
                if sum(tmp) == n:
                    res.append(tmp)
                return
            if sum(tmp) > n:
                return
            for i in range(tmp[-1]+1, 10):
                dfs(tmp + [i])

        for i in range(1,10):
            dfs([i])
        return res

s = Solution()
# k = 3
# n = 7
# print(s.combinationSum3(k,n))

# k = 3
# n = 9
# print(s.combinationSum3(k,n))

# k = 1
# n = 1
# print(s.combinationSum3(k,n))

k = 3
n = 15
print(s.combinationSum3(k,n))

"""
Output
[[1,6,8],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
Expected
[[1,5,9],[1,6,8],[2,4,9],[2,5,8],[2,6,7],[3,4,8],[3,5,7],[4,5,6]]
"""