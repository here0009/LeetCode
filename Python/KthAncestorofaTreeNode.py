"""
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.

 

Example:



Input:
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

Output:
[null,1,0,-1]

Explanation:
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor
 

Constraints:

1 <= k <= n <= 5*10^4
parent[0] == -1 indicating that 0 is the root node.
0 <= parent[i] < n for all 0 < i < n
0 <= node < n
There will be at most 5*10^4 queries.
"""


class TreeAncestor_1:
    """
    TLE
    """
    def __init__(self, n: int, parent):
        self.p_dict = dict()
        for i,v in enumerate(parent):
            p_dict[i] = v
        

    def getKthAncestor(self, node: int, k: int) -> int:
        if k == 0 or node == -1:
            return node
        return self.getKthAncestor(p_dict[node], k-1)


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
from functools import lru_cache
class TreeAncestor_2:
    def __init__(self, n: int, parent):
        self.p_dict = dict()
        self.cache = dict()
        for i,v in enumerate(parent):
            self.p_dict[i] = v
        
    @lru_cache(None)
    def getKthAncestor(self, node: int, k: int) -> int:
        if k == 0 or node == -1:
            return node
        for i in range(k-1, -1, 0):
            res = self.getKthAncestor(self.p_dict[node], k-1)
        return res


from math import log
class TreeAncestor:
    def __init__(self, n, parent):
        self.pars = [parent]
        self.n = n
        depth = int(log(n,2)) + 1
        for _ in range(depth):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)
        for row in self.pars:
            print(row)

    def getKthAncestor(self, node, k):
        i = 0
        while k:
            if node == -1:
                break
            if (k & 1):
                node = self.pars[i][node]
            i += 1
            k >>= 1
        return node

# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/discuss/686318/Solution-Using-Binary-Lifting
from math import log
class TreeAncestor:
    def __init__(self, n, parent):
        self.pars = [parent]
        self.n = n
        depth = int(log(n,2)) + 1
        for _ in range(depth):
            row = []
            for i in range(n):
                p = self.pars[-1][i]
                if p != -1:
                    p = self.pars[-1][p]
                row.append(p)
            self.pars.append(row)
        for row in self.pars:
            print(row)

    def getKthAncestor(self, node, k):
        i = 0
        while k:
            if node == -1:
                break
            if k % 2 == 1:
                node = self.pars[i][node]
            i += 1
            k = k //2
        return node

# https://leetcode.com/problems/kth-ancestor-of-a-tree-node/discuss/686482/Python3-binary-lifting-(dp)
from math import log2
class TreeAncestor:
    def __init__(self, n: int, parent):
        m = 1 + int(log2(n)) #at most 16 for this problem 
        self.dp = [[-1] * m for _ in range(n)] #ith node's 2^j parent
        for i in range(n):
            self.dp[i][0] = parent[i] #2^0 parent
            for j in range(1, m):
                if self.dp[i][j-1] != -1: 
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]
        for row in self.dp:
            print(row)
    
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: #sanity check of k is skipped
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node 

treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(treeAncestor.getKthAncestor(3, 1)) # returns 1 which is the parent of 3
print(treeAncestor.getKthAncestor(5, 2))  # returns 0 which is the grandparent of 5
print(treeAncestor.getKthAncestor(6, 3))  # returns -1 because there is no such ancestor
 
