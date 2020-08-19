"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.
Example 1:

Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
Example 2:

Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
"""


from collections import defaultdict
from collections import Counter
class Solution:
    """
    it can pass, but too slow
    """
    def findItinerary(self, tickets):
        def dfs(node, res, visited):
            if not self.res:
                if len(res) == length:
                    self.res = res
                    return
                for next_node in edges[node]:
                    if visited[(node, next_node)] < edges_dict[node][next_node]:
                        visited[(node, next_node)] += 1
                        dfs(next_node, res + [next_node], visited)
                        visited[(node, next_node)] -= 1

        edges_dict = defaultdict(Counter)
        edges = defaultdict(list)
        for s, e in tickets:
            edges_dict[s][e] += 1
            edges[s].append(e)
        length = len(tickets) + 1
        for s in edges:
            edges[s].sort()
        # print(edges_dict)
        self.res = []
        visited = Counter()
        dfs('JFK', ['JFK'], visited)
        return self.res

from collections import defaultdict
class Solution:
    def dfs(self, node):
        while self.edges[node]:
            self.dfs(self.edges[node].pop())
        self.route.append(node)

    def findItinerary(self, tickets):
        self.route = []
        self.edges = defaultdict(list)
        for src, dst in tickets:
            self.edges[src].append(dst)
        for src in self.edges:
            self.edges[src].sort(reverse=True)
        self.dfs('JFK')
        return self.route[::-1]

# https://leetcode.com/problems/reconstruct-itinerary/discuss/375397/Simply-simple-Python-Solution-Using-stack-for-dfs-with-comments
class Solution:
    def findItinerary(self, tickets):
        graph = {}
        # Create a graph for each airport and keep list of airport reachable from it
        for src, dst in tickets:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]

        for src in graph.keys():
            graph[src].sort(reverse=True)
            # Sort children list in descending order so that we can pop last element 
            # instead of pop out first element which is costly operation
        stack = []
        res = []
        stack.append("JFK")
        # Start with JFK as starting airport and keep adding the next child to traverse 
        # for the last airport at the top of the stack. If we reach to an airport from where 
        # we can't go further then add it to the result. This airport should be the last to go 
        # since we can't go anywhere from here. That's why we return the reverse of the result
        # After this backtrack to the top airport in the stack and continue to traaverse it's children
        print(graph)
        while len(stack) > 0:
            # print('stack',stack)
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0:
                # print('graph,elem',elem,graph[elem])
                # Check if elem in graph as there may be a case when there is no out edge from an airport 
                # In that case it won't be present as a key in graph
                stack.append(graph[elem].pop())
            else:
                res.append(stack.pop())
                # If there is no further children to traverse then add that airport to res
                # This airport should be the last to go since we can't anywhere from this
                # That's why we return the reverse of the result
        return res[::-1]

# https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a].append(b)
        route = []
        print(targets)
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]

S = Solution()
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# print(S.findItinerary(tickets))
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# print(S.findItinerary(tickets))
tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
print(S.findItinerary(tickets))
# Output
# []
# Expected
# ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]