"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
 

The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.
"""
class LinkedNode:
    def __init__(self, string):
        self.string = string
        self.next = None
        self.pre = None



class Solution_1:
    def calcEquation(self, equations, values, queries):

        val_dict = dict()
        for i in range(len(equations)):
            e1, e2 = equations[i]
            val = values[i]
            if e1 not in val_dict and e2 not in val_dict:
                val_dict[e2] = 1
                val_dict[e1] = val
            elif e1 in val_dict and e2 in val_dict:
                pass
            else:
                if e1 not in val_dict:
                    val_dict[e1] = val * val_dict[e2]
                elif e2 not in val_dict:
                    val_dict[e2] = val_dict[e1]/val
        res  = []
        for q1,q2 in queries:
            if q1 in val_dict and q2 in val_dict:
                res.append(val_dict[q1]/val_dict[q2])
            else:
                res.append(-1.0)
        return res

from collections import defaultdict
class Solution_2:
    def calcEquation(self, equations, values, queries):
        q = defaultdict(dict)
        for (a,b),val in zip(equations,values):
            q[a][a] = 1
            q[b][b] = 1
            q[a][b] = val
            q[b][a] = 1/val

        for k in q:
            for i in q[k]:
                for j in q[k]:
                    q[i][j] = q[i][k] * q[k][j]

        res = [q[a].get(b,-1.0) for (a,b) in queries]
        # for a,b in queries:
        #     if a not in q or b not in q:
        #         res.append(-1.0)
        #     else:
        #         res.append(q[a][b])

        return res

from collections import defaultdict
class Solution_3:
    def calcEquation(self, equations, values, queries):
        def dfs(start, end, val, paths):
            if start == end and start in G:
                paths[0] = val
                return
            if start in vis:
                return
            vis.add(start)
            for n in G[start]:
                dfs(n, end, val*W[start,n],paths)


        G,W = defaultdict(set), defaultdict(float)
        for (a,b),val in zip(equations, values):
            G[a],G[b] = G[a]|{b}, G[b]|{a}
            W[a,b], W[b,a] = val, 1/val
   
        res = []
        for a,b in queries:
            paths, vis = [-1.0], set()
            dfs(a,b,1.0,paths)
            res.append(paths[0])
        return res


from collections import defaultdict
class Solution:
    def calcEquation(self, equations, values, queries):
        def dfs(start, end, val):
            if start == end:
                return val
            if start in vis:
                return -1
            vis.add(start)
            for n in G[start]:
                k = dfs(n, end, val*W[start,n])
                if k != -1:
                    return k
            return -1.0


        G,W = defaultdict(set), defaultdict(float)
        for (a,b),val in zip(equations, values):
            G[a],G[b] = G[a]|{b}, G[b]|{a}
            W[a,b], W[b,a] = val, 1/val
   
        res = []
        for a,b in queries:
            if a not in G or b not in G:
                res.append(-1.0)
            else:
                vis = set()
                k = dfs(a,b,1.0)
                res.append(k)
        return res




s = Solution()
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
print(s.calcEquation(equations, values, queries))

equations = [["a","b"],["e","f"],["b","e"]]
values = [3.4,1.4,2.3]
queries = [["b","a"],["a","f"],["f","f"],["e","e"],["c","c"],["a","c"],["f","e"]]
print(s.calcEquation(equations, values, queries))