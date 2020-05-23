"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 

Note:

N is a positive integer and will not exceed 15.
"""
"""
Thoughts: backtrack
"""
from copy import deepcopy
class Solution:
    def countArrangement(self, N: int) -> int:

        def backtrack(pos,vals):
            if pos == N+1:
                self.res += 1
                return

            for val in vals:
                if pos % val == 0 or val % pos == 0:
                    new_vals = deepcopy(vals)
                    new_vals.remove(val)
                    backtrack(pos+1,new_vals)


        nums = set(range(1,N+1))
        self.res = 0
        backtrack(1,nums)
        return self.res

class Solution:
    def countArrangement(self, N: int) -> int:
        """
        wrong answer, may be because the size of the set is changed during the iteration
        """
        def backtrack(pos):
            if pos == N+1:
                self.res += 1
                return

            for num in nums:
                if pos % num == 0 or num % pos == 0:
                    nums.remove(num)
                    backtrack(pos+1)
                    nums.add(num)

        nums = set(range(1,N+1))
        self.res = 0
        backtrack(1)
        return self.res


class Solution:
    def countArrangement(self, N: int) -> int:
        def backtrack(pos):
            if pos == N+1:
                self.res += 1
                return

            for i in range(1,N+1):
                if not visited[i] and (i % pos == 0 or pos % i == 0):
                    visited[i] = 1
                    backtrack(pos+1)
                    visited[i] = 0

        visited = [0]*(N+1)
        self.res = 0
        backtrack(1)
        return self.res

# class Solution:
#     def countArrangement(self, N: int) -> int:
#         self.cnt = 0
#         used = [0] * (N+1)
        
#         def dfs(s):
#             if s == N+1:
#                 self.cnt+=1
#                 return
            
#             for i in range(1, N+1):
#                 if not used[i] and min(i%s,s%i)==0: 
#                     used[i] = 1
#                     dfs(s+1)
#                     used[i] = 0
            
#         dfs(1)
#         return self.cnt
from functools import lru_cache
class Solution:
    def countArrangement(self, N: int) -> int:
        @lru_cache(None)
        def dfs(i,X):
            if i == 1:
                return 1
            return sum(dfs(i-1,X[:j]+X[j+1:]) for j,x in enumerate(X) if x%i == 0 or i%x == 0)
        return dfs(N,tuple(range(1,N+1)))


S = Solution()
N = 2
print(S.countArrangement(N))
N = 3
print(S.countArrangement(N))
# for i in range(1,15):
#     print(S.countArrangement(i))

N = 10
print(S.countArrangement(N))
"""
Output
4788
Expected
700
"""