"""
There is a tree (i.e., a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has a value associated with it, and the root of the tree is node 0.

To represent this tree, you are given an integer array nums and a 2D array edges. Each nums[i] represents the ith node's value, and each edges[j] = [uj, vj] represents an edge between nodes uj and vj in the tree.

Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.

An ancestor of a node i is any other node on the shortest path from node i to the root. A node is not considered an ancestor of itself.

Return an array ans of size n, where ans[i] is the closest ancestor to node i such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such ancestor.

 

Example 1:



Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
Output: [-1,0,0,1]
Explanation: In the above figure, each node's value is in parentheses.
- Node 0 has no coprime ancestors.
- Node 1 has only one ancestor, node 0. Their values are coprime (gcd(2,3) == 1).
- Node 2 has two ancestors, nodes 1 and 0. Node 1's value is not coprime (gcd(3,3) == 3), but node 0's
  value is (gcd(2,3) == 1), so node 0 is the closest valid ancestor.
- Node 3 has two ancestors, nodes 1 and 0. It is coprime with node 1 (gcd(3,2) == 1), so node 1 is its
  closest valid ancestor.
Example 2:



Input: nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
Output: [-1,0,-1,0,0,0,-1]
 

Constraints:

nums.length == n
1 <= nums[i] <= 50
1 <= n <= 105
edges.length == n - 1
edges[j].length == 2
0 <= uj, vj < n
uj != vj
"""


from typing import List
from math import gcd
from collections import defaultdict
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        """
        TLE
        """
        n = len(nums)
        parent = [None] * n
        parent[0] = -1
        edges_list = defaultdict(list)
        for i, j in edges:
            edges_list[i].append(j)
            edges_list[j].append(i)

        def dfs(i):
            for j in edges_list[i]:
                if parent[j] is None:
                    parent[j] = i
                    dfs(j)

        dfs(0)
        # print(edges_list)
        # print(parent)
        res = []
        for i in range(n):
            pi = parent[i]
            while pi != -1 and gcd(nums[i], nums[pi]) != 1:
                pi = parent[pi]
            res.append(pi)
        return res
 


from typing import List
from math import gcd, sqrt
from collections import defaultdict
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        """
        Thoughts:
        nums[i] <= 50, we can record the prime factors of nums[i] in list 
        wrong answer
        """
        limits = 51
        isPrime = [1] * limits
        for i in range(2, int(sqrt(50)) + 1):
            if isPrime[i]:
                for j in range(i * i, limits, i):
                    isPrime[j] = 0
        primes = [i for i in range(2, limits) if isPrime[i]]

        print(primes)
        n = len(nums)
        parent = [None] * n
        parent[0] = -1
        edges_list = defaultdict(list)
        for i, j in edges:
            edges_list[i].append(j)
            edges_list[j].append(i)
        idx_depth = dict()
        idx_depth[-1] = -1

        def dfs(i, d, prime_idx):
            print(i, nums[i], d, prime_idx)
            ancestors = set(prime_idx)
            idx_depth[i] = d
            prime_idx2 = prime_idx[:]
            for j in range(len(primes)):
                p = primes[j]
                if nums[i] % p != 0:
                    prime_idx2[j] = i
                else:
                    if prime_idx[j] in ancestors:
                        ancestors.remove(prime_idx[j])

            tmp, tmp_d = -1, -1
            for a in ancestors:
                if idx_depth[a] > tmp_d:
                    tmp = a
            parent[i] = tmp

            for j in edges_list[i]:
                if parent[j] is None:
                    dfs(j, d + 1, prime_idx2)


        dfs(0, 0, [-1] * len(primes))  # idx, depth,  [idx for each primer]
        return parent


# https://leetcode.com/problems/tree-of-coprimes/discuss/1074565/Python3-dfs
from typing import List
from math import gcd
from collections import defaultdict
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        """
        because nums[i] <= 50, the length of path is limited, we can check each num within 50 iterations
        """
        def dfs(node, parent, depth):
            max_depth = -1
            for val in path:
                if gcd(nums[node], val) == 1:
                    if path[val] and path[val][-1][1] > max_depth:
                        res[node], max_depth = path[val][-1]
            path[nums[node]].append((node, depth))
            for nxt_node in graph[node]:
                if nxt_node != parent:
                    dfs(nxt_node, node, depth + 1)
            path[nums[node]].pop()

        n = len(nums)
        res = [-1] * n
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        path = defaultdict(list)
        dfs(0, -1, 0)
        return res


S = Solution()
nums = [2,3,3,2]
edges = [[0,1],[1,2],[1,3]]
print(S.getCoprimes(nums, edges))

nums = [5,6,10,2,3,6,15]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
print(S.getCoprimes(nums, edges))