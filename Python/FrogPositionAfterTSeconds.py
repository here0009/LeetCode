"""
Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from the vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with the same probability, otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex. 

The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting directly the vertices fromi and toi.

Return the probability that after t seconds the frog is on the vertex target.

 

Example 1:



Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
Example 2:



Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
Example 3:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output: 0.16666666666666666
 

Constraints:

1 <= n <= 100
edges.length == n-1
edges[i].length == 2
1 <= edges[i][0], edges[i][1] <= n
1 <= t <= 50
1 <= target <= n
Answers within 10^-5 of the actual value will be accepted as correct
"""
from collections import defaultdict
class Solution:
    def frogPosition(self, n: int, edges, t: int, target: int) -> float:
        visited = [0]*(n+1)
        e_dict = defaultdict(list)
        for p,q in edges:
            e_dict[p].append(q)
            e_dict[q].append(p)
        # print(e_dict)
        prob_dict = {1:1}
        visited[1] = 1
        while t > 0:
            prob_dict2 = dict()
            for k,v in prob_dict.items():
                children = set()
                for c in e_dict[k]:
                    if visited[c] == 0:
                        children.add(c)
                        visited[c] = 1
                len_children = len(children)
                if len_children == 0:
                    prob_dict2[k] = v
                else:
                    for c in children:
                        prob_dict2[c] = v/len_children

            if prob_dict == prob_dict2:
                break
            prob_dict = prob_dict2
            # print(prob_dict)
            t -= 1
        if target in prob_dict:
            return prob_dict[target]
        else:
            return 0

S = Solution()
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 2
target = 4
print(S.frogPosition(n,edges,t,target))
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 1
target = 7
print(S.frogPosition(n,edges,t,target))
n = 7
edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
t = 20
target = 6
print(S.frogPosition(n,edges,t,target))

n = 3
edges = [[2,1],[3,2]]
t = 1
target = 2
print(S.frogPosition(n,edges,t,target))
