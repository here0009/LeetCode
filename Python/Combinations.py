"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution_1:
    """
    this solution is accepted, but too slow
    """
    def combine(self, n: int, k: int):
        if k <= 0:
            return []
        res = [[i+1] for i in range(n)]
        for j in range(k-1):
            tmp = []
            while res:
                l = res.pop()
                for i in range(n):
                    if i+1 > l[-1]:
                        tmp.append(l+[i+1])
            res = tmp
        return res

from itertools import combinations
class Solution_2:
    def combine(self, n: int, k: int):
        res = []
        for i in combinations(range(1,n+1),k):
            res.append(list(i))
        return res

class Solution_3:
    def combine(self, n: int, k: int):
        if k == 0:
            return [[]]
        else:
            res = [pre+[i] for i in range(k,n+1) for pre in self.combine(i-1,k-1)]
            print(res)
        return res

class Solution:
    def combine(self, n: int, k: int):
        def backtrack(res,curr,start):
            print(curr)
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(start+1,n+1):
                curr.append(i)
                backtrack(res,curr,i)
                curr.pop()

        res = []
        for i in range(1,n+1):
            backtrack(res,[i],i)
        return res

s = Solution()
# n = 4
# k = 2
# print(s.combine(n,k))

n = 4
k = 3
print(s.combine(n,k))

# n = 4
# k = 1
# print(s.combine(n,k))

# n = 4
# k = 4
# print(s.combine(n,k))

# n = 5
# k = 0
# print(s.combine(n,k))