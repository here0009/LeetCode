"""
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 

Constraints:

1 <= m <= n <= 3*10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m-1
0 <= beforeItems[i].length <= n-1
0 <= beforeItems[i][j] <= n-1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
"""


# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/discuss/402401/Python-Use-topologically-sorted-items-and-groups-to-get-the-desired-order.
from collections import defaultdict
class Solution:
    def sortItems(self, n: int, m: int, group, beforeItems):
        def topOrder(graph, indegree):
            res = []
            stack = [node for node in range(len(graph)) if indegree[node] == 0]
            while stack:
                v = stack.pop()
                res.append(v)
                for u in graph[v]:
                    indegree[u] -= 1
                    if indegree[u] == 0:
                        stack.append(u)
            return res if len(res) == len(graph) else []

        for u in range(len(group)):
            if group[u] == -1:
                group[u] = m
                m += 1

        graph_itmes = [[] for _ in range(n)]
        indegree_items = [0]*n
        graph_groups = [[] for _ in range(m)]
        indegree_groups = [0]*m
        for u in range(n):
            for v in beforeItems[u]:
                graph_itmes[v].append(u)
                indegree_items[u] += 1
                if group[u] != group[v]:
                    graph_groups[group[v]].append(group[u])
                    indegree_groups[group[u]] += 1

        item_order = topOrder(graph_itmes, indegree_items)
        group_order = topOrder(graph_groups, indegree_groups)
        if not item_order or not group_order:
            return []
        order_within_group = defaultdict(list)
        for v in item_order:
            order_within_group[group[v]].append(v)

        res = []
        for group in group_order:
            res += order_within_group[group]
        return res


S = Solution()
n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
print(S.sortItems(n, m, group, beforeItems))

n = 8
m = 2
group = [-1,-1,1,0,0,1,0,-1]
beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
print(S.sortItems(n, m, group, beforeItems))