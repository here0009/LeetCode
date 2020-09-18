"""
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:

Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
Example 2:

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
Note:

len(row) is even and in the range of [4, 60].
row is guaranteed to be a permutation of 0...len(row)-1.
"""




class Solution:
    def minSwapsCouples(self, row) -> int:
        def dfs(i):
            visited[i] = True
            self.tmp += 1
            for j in edges[i]:
                if not visited[j]:
                    dfs(j)

        N = len(row) // 2
        edges = [[] for _ in range(N)]
        couches = dict()
        for i in range(len(row)):
            couches[row[i]] = i // 2
        for i in range(N):
            c1, c2 = couches[2*i], couches[2*i+1]
            if c1 != c2:
                edges[c1].append(c2)
                edges[c2].append(c1)
        res = 0
        visited = N * [False]
        for i in range(N):
            if not visited[i]:
                self.tmp = 0
                dfs(i, nodes)
                res += self.tmp - 1
        return res

"""
use two hashmaps to record the theoretical paterner and current seat paterner of each person.
record the cost of union find operations to find the theorectial paterner
"""
class Solution:
    def minSwapsCouples(self, row) -> int:
        def dist(p, q):
            # count the distance between p and q
            visited[p] = 1
            res = 0
            if paterner[p] != q:
                visited[paterner[p]] = 1
                res = 1 + dist(seats[paterner[p]], q)
            visited[q] = 1
            return res

        N = len(row)//2
        paterner = dict()
        for i in range(1, N+1): # the paterner of each person
            paterner[i*2-2] = i*2-1
            paterner[i*2-1] = i*2-2
        seats = dict()
        for i in range(N): # the current seat-paterner of each person
            p, q = row[i*2], row[i*2+1]
            seats[p] = q
            seats[q] = p
        res = 0
        visited = [0]*(2*N)
        for i in range(2*N):
            if not visited[i]:
                res += dist(i, seats[i])
        return res

S = Solution()
row = [0, 2, 1, 3]
print(S.minSwapsCouples(row))

row = [3, 2, 0, 1]
print(S.minSwapsCouples(row))

