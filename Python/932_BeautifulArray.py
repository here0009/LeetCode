"""
For some fixed N, an array A is beautiful if it is a permutation of the integers 1, 2, ..., N, such that:

For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] + A[j].

Given N, return any beautiful array A.  (It is guaranteed that one exists.)

 

Example 1:

Input: 4
Output: [2,1,4,3]
Example 2:

Input: 5
Output: [3,1,2,5,4]
 

Note:

1 <= N <= 1000
"""

from collections import deque
class Solution:
    def beautifulArray(self, N: int):
        """
        too complicated to implement
        """
        def backTrack(n):
            print(n, res, visited)
            if n == N+1:
                self.flag = True
            if self.flag:
                return
            for i in range(1, N+1):
                if i not in visited:
                    for v in res:
                        tmp = v+i
                        if tmp % 2 == 0 and tmp // 2 in visited:
                            break
                    else:
                        visited.add(i)
                        res[n-1] = i
                        backTrack(n+1)
                        visited.remove(i)

        visited = set()
        res = [0]*N
        self.flag = False
        backTrack(1)
        return res

class Solution:
    def beautifulArray(self, N: int):
        """
        wrong answer
        """
        lst = list(range(1, N+1))[::-1]
        res = []
        while lst:
            length = len(lst)
            if length == 1:
                res.append(lst.pop())
            elif length == 2:
                res.extend(lst[:2][::-1])
            if length >= 3:
                a,b,c = lst[:3]
                res.extend([c,a,b]) #for [1,2,3], we extend [3,1,2] so no violation to the rule
            lst = lst[min(3, length):]
            # print(lst, res)
        return res

from collections import deque
class Solution:
    def beautifulArray(self, N: int):
        def backTrack(n):
            print(n, res, visited)
            if n == N+1:
                self.flag = True
            if self.flag:
                return
            for i in range(1, N+1):
                if i not in visited:
                    tmp_dq = deque(res[::1])
                    tmp_set = set(res)
                    flag = False
                    while tmp_dq:
                        v = tmp_dq.popleft()
                        tmp_set.remove(v)
                        if (i+v) %2 == 0 and (i+v)//2 in tmp_set:
                            flag = True
                            break
                    if not flag:
                        visited.add(i)
                        res[n-1] = i
                        backTrack(n+1)
                        visited.remove(i)

        visited = set()
        res = [0]*N
        self.flag = False
        backTrack(1)
        return res

class Solution:
    def beautifulArray(self, N: int):
        res = [1]
        while len(res) < N:
            res = [i*2-1 for i in res] + [i*2 for i in res]
        return [i for i in res if i <= N]

S = Solution()
N = 4
print(S.beautifulArray(N))
N = 5
print(S.beautifulArray(N))
N = 100
print(S.beautifulArray(N))
# Output
# [98,100,99,95,97,96,92,94,93,89,91,90,86,88,87,83,85,84,80,82,81,77,79,78,74,76,75,71,73,72,68,70,69,65,67,66,62,64,63,59,61,60,56,58,57,53,55,54,50,52,51,47,49,48,44,46,45,41,43,42,38,40,39,35,37,36,32,34,33,29,31,30,26,28,27,23,25,24,20,22,21,17,19,18,14,16,15,11,13,12,8,10,9,5,7,6,2,4,3,1]
# Expected
# [1,65,33,97,17,81,49,9,73,41,25,89,57,5,69,37,21,85,53,13,77,45,29,93,61,3,67,35,99,19,83,51,11,75,43,27,91,59,7,71,39,23,87,55,15,79,47,31,95,63,2,66,34,98,18,82,50,10,74,42,26,90,58,6,70,38,22,86,54,14,78,46,30,94,62,4,68,36,100,20,84,52,12,76,44,28,92,60,8,72,40,24,88,56,16,80,48,32,96,64]
