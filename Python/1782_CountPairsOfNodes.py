"""
You are given an undirected graph represented by an integer n, which is the number of nodes, and edges, where edges[i] = [ui, vi] which indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

The answer to the jth query is the number of pairs of nodes (a, b) that satisfy the following conditions:

a < b
cnt is strictly greater than queries[j], where cnt is the number of edges incident to a or b.
Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

Note that there can be repeated edges.

 

Example 1:


Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]
Explanation: The number of edges incident to at least one of each pair is shown above.
Example 2:

Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
Output: [10,10,9,8,6]
 

Constraints:

2 <= n <= 2 * 104
1 <= edges.length <= 105
1 <= ui, vi <= n
ui != vi
1 <= queries.length <= 20
0 <= queries[j] < edges.length
"""


from typing import List
from collections import Counter
from bisect import bisect_right
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """
        TLE
        """
        counts = Counter()
        e_counts = Counter()
        for p, q in edges:
            if p > q:
                p, q = q, p
            counts[p] += 1
            counts[q] += 1
            e_counts[(p, q)] += 1
        dot_pair_counts = []
        # print(counts)
        # print(e_counts)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                # print(i, j, counts[i] + counts[j] - e_counts[(i, j)])
                dot_pair_counts.append(counts[i] + counts[j] - e_counts[(i, j)])
        res = []
        dot_pair_counts.sort()
        # print(dot_pair_counts)
        length = len(dot_pair_counts)
        for q in queries:
            res.append(length - bisect_right(dot_pair_counts, q))
        return res


from collections import Counter
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        """
        we can not calculate all the dot paris since it will take O(n**2) time
        we can iterate over the edges, since query is 20, there are only 1E5 edges.
        """

        n_counts = [0] * (n + 1)
        e_counts = Counter()
        for p, q in edges:
            n_counts[p] += 1
            n_counts[q] += 1
            e_counts[(min(p, q), max(p, q))] += 1

        vals = sorted(n_counts)
        res = []
        # print(n_counts)
        # print(e_counts)
        for query in queries:
            i, j = 1, n
            cnt = 0
            while i < j:
                if vals[i] + vals[j] > query:
                    cnt += j - i  # paris of (i, j) ... (j - 1, j)
                    j -= 1
                else:
                    i += 1
            for p, q in e_counts.keys():
                if n_counts[p] + n_counts[q] - e_counts[(p, q)] <= query < n_counts[p] + n_counts[q]:
                    cnt -= 1
            res.append(cnt)
        return res



S = Solution()
n = 4
edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
queries = [2,3]
print(S.countPairs(n, edges, queries))

n = 5
edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]]
queries = [1,2,3,4,5]
print(S.countPairs(n, edges, queries))