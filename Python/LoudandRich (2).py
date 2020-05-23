"""
In a group of N people (labelled 0, 1, 2, ..., N-1), each person has different amounts of money, and different levels of quietness.

For convenience, we'll call the person with label x, simply "person x".

We'll say that richer[i] = [x, y] if person x definitely has more money than person y.  Note that richer may only be a subset of valid observations.

Also, we'll say quiet[x] = q if person x has quietness q.

Now, return answer, where answer[x] = y if y is the least quiet person (that is, the person y with the smallest value of quiet[y]), among all people who definitely have equal to or more money than person x.

 

Example 1:

Input: richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]
Output: [5,5,2,5,4,5,6,7]
Explanation: 
answer[0] = 5.
Person 5 has more money than 3, which has more money than 1, which has more money than 0.
The only person who is quieter (has lower quiet[x]) is person 7, but
it isn't clear if they have more money than person 0.

answer[7] = 7.
Among all people that definitely have equal to or more money than person 7
(which could be persons 3, 4, 5, 6, or 7), the person who is the quietest (has lower quiet[x])
is person 7.

The other answers can be filled out with similar reasoning.
Note:

1 <= quiet.length = N <= 500
0 <= quiet[i] < N, all quiet[i] are different.
0 <= richer.length <= N * (N-1) / 2
0 <= richer[i][j] < N
richer[i][0] != richer[i][1]
richer[i]'s are all different.
The observations in richer are all logically consistent.
"""
from functools import lru_cache
from collections import defaultdict
class Solution:
    def loudAndRich(self, richer, quiet):
        
        @lru_cache(None)
        def dfs(i):
            """
            find the people that richer than n
            """
            self.richer_dict[i].add(i)
            for j in range(N+1):
                if matrix[i][j] == 1:
                    self.richer_dict[i].add(j)
                    self.richer_dict[i] |= dfs(j)
            return self.richer_dict[i] 

        N = len(quiet)
        matrix = [[0]*(N+1) for _ in range(N+1)]
        #matrix[i][j] = 1 means j is richer than i
        for j,i in richer:
            matrix[i][j] = 1
        # visited = [0]*(N+1)
        self.richer_dict = defaultdict(set)
        for i in range(N):
            dfs(i)
        # print(self.richer_dict)
        res = []
        # quiet_dict = dict(sorted([(v,i) for i,v in enumerate(quiet)]))
        for i in range(N):
            min_quite = float('inf')
            for j in self.richer_dict[i]:
                if quiet[j] < min_quite:
                    ans = j
                    min_quite = quiet[j]
            res.append(ans)
        return res


class Solution:
    def loudAndRich(self, richer, quiet):

        N = len(quiet)
        graph = [[]*N for _ in range(N)]
        for i,j in richer:
            graph[j].append(i)
        res = [i for i in range(N)]
        res = [None]*N
        def dfs(i):
            if res[i] is None: #if res[i] is not None, it is already calculated, just return res[i]
                res[i] = i
                for j in graph[i]:
                    cand = dfs(j)
                    if quiet[cand] < quiet[res[i]]:
                        res[i] = cand
            return res[i]

        return list(map(dfs, range(N)))

from collections import defaultdict
class Solution:
    def loudAndRich(self, richer, quiet):
        m = defaultdict(list)
        for i, j in richer: m[j].append(i)
        res = [-1] * len(quiet)

        def dfs(i):
            if res[i] >= 0: return res[i]
            res[i] = i
            for j in m[i]:
                if quiet[res[i]] > quiet[dfs(j)]: res[i] = res[j]
            return res[i]

        for i in range(len(quiet)): dfs(i)
        return res

richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
S = Solution()
print(S.loudAndRich(richer,quiet))