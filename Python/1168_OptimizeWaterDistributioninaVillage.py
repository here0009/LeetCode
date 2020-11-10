"""
There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i], or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes, where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe. Connections are bidirectional.

Find the minimum total cost to supply water to all houses.

 

Example 1:



Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: 
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
 

Constraints:

1 <= n <= 10000
wells.length == n
0 <= wells[i] <= 10^5
1 <= pipes.length <= 10000
1 <= pipes[i][0], pipes[i][1] <= n
0 <= pipes[i][2] <= 10^5
pipes[i][0] != pipes[i][1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimize-water-distribution-in-a-village
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 作者：JiayangWu
# 链接：https://leetcode-cn.com/problems/optimize-water-distribution-in-a-village/solution/python-jie-fa-zui-xiao-sheng-cheng-shu-by-jiayangw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class UnionFindSet:
    def __init__(self, n):
 
        self.roots = [i for i in range(n + 1)]
        self.rank = [0 for i in range(n + 1)]
        self.count = n
 
    def find(self, member):
        tmp = []
        while member != self.roots[member]:
            tmp.append(member)
            member = self.roots[member]
        for root in tmp:
            self.roots[root] = member
        return member
 
    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] -= 1
            self.count -= 1
            
class Solution:
    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        for i, well in enumerate(wells):
            pipes.append([0, i + 1, well])#转井为管
        
        queue = []
        ufs = UnionFindSet(n)
        for start, end, cost in pipes:
            queue.append([cost, start, end]) 
            
        heapify(queue)
        res = 0
        while ufs.count > 0:           
            cost, start, end = heappop(queue)
            if ufs.find(start) == ufs.find(end):
                continue
            res += cost
            ufs.union(end, start)
        return res


from typing import List
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        """
        不需要直接与水井相连，与和水井相连的村子相连也可以
        把水井视为house 0，连接所有house
        """
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            root[ri] = rj
            return True

        cost = []
        for i,v in enumerate(wells):
            cost.append((v, 0, i+1))
        for i, j, d in pipes:
            cost.append((d, i, j))
        root = list(range(n+1))
        cost.sort()
        counts = 0
        res = 0
        for d, i, j in cost:
            if union(i, j):
                counts += 1
                res += d
                if counts == n:
                    return res
        return None


S = Solution()
n = 3
wells = [1,2,2]
pipes = [[1,2,1],[2,3,1]]
print(S.minCostToSupplyWater(n, wells, pipes))