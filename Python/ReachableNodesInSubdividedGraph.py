"""
类似于树的遍历, 但是是图,可能更加复杂
尝试采用递归的方法, 从0开始先到一个节点, 再从这个节点开始, 直到末尾或者到M
"""
class Solution:
    def reachableNodes(self, edges, M, N):
        """
        :type edges: List[List[int]]
        :type M: int
        :type N: int
        :rtype: int
        """

    def LnodesFromK(self, edge, K, L):
        """
        return the nodes from K, largest distance is L
        """
        

s = Solution()
edges = [[0,1,10],[0,2,1],[1,2,2]]
M = 6
N = 3
print(s.reachableNodes(edges, M, N))