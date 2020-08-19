"""
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 

Example 1:

Input: A = ["tars","rats","arts","star"]
Output: 2
 

Constraints:

1 <= A.length <= 2000
1 <= A[i].length <= 1000
A.length * A[i].length <= 20000
All words in A consist of lowercase letters only.
All words in A have the same length and are anagrams of each other.
The judging time limit has been increased for this question.
"""


from collections import defaultdict
class Solution:
    """
    TLE
    """
    def numSimilarGroups(self, A) -> int:
        def similar(X, Y):
            res = 0
            for x,y in zip(X, Y):
                if x != y:
                    res += 1
                if res > 2:
                    return False
            return res == 2 or res == 0

        def dfs(node, flag):
            if color[node] == 0:
                color[node] = flag
                for next_node in edges[node]:
                    dfs(next_node, flag)

        edges = defaultdict(list)
        length = len(A)
        for i in range(length - 1):
            for j in range(i+1, length):
                if similar(A[i], A[j]):
                    edges[i].append(j)
                    edges[j].append(i)

        color = [0]*length
        counts = 0
        for i in range(length):
            if color[i] == 0:
                counts += 1
                dfs(i, counts)

        # print(color)
        return counts





# https://leetcode.com/problems/similar-string-groups/discuss/255844/python-O(mn-*-min(m-n))-solution-union-find
class Solution:
    def numSimilarGroups(self, A):
        def explore(s):
            visited.add(s)
            for v in edges[s]:
                if v not in visited: explore(v)
        res, edges, visited = 0, {}, set()
        if len(A) >= 2 * len(A[0]):
            strs = set(A)
            for s in A:
                if s not in edges: edges[s] = set()
                for i in range(len(s) - 1):
                    for j in range(i + 1, len(s)):
                        new = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                        if new in strs:
                            edges[s].add(new)
                            if new in edges: edges[new].add(s)
                            else: edges[new] = {s}
        else:
            for s in A:
                if s not in edges: edges[s] = set()
                for t in A:
                    if s != t:
                        same = 0
                        for i, c in enumerate(t):
                            if c == s[i]: same += 1
                        if same == len(s) - 2: 
                            edges[s].add(t)
                            if t in edges: edges[t].add(s)
                            else: edges[t] = {s}
        for s in A:
            if s not in visited:
                res += 1
                explore(s)
        return res

class Solution:
    def similar(self, x, y):
        cnt = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                cnt += 1
            if cnt > 2:
                return False
        return True 

    def numSimilarGroups(self, A) -> int:
        wordlen = len(A[0])
        A=set(A)
        divs = defaultdict(list)
        if wordlen > 6:
            for word in A:
                step = wordlen // 3
                for i in range(0, step * 3, step):
                    divs[word[i:i+step] + str(i)].append(word)
        else:
            divs['all'].extend(A)
        
        graph = defaultdict(set)
        for _list in divs.values():
            for i, a in enumerate(_list):
                for j, b in enumerate(_list[i+1:], i+1):
                    if self.similar(a, b):
                        graph[a].add(b)
                        graph[b].add(a)
        
        ans = 0 
        cc = set()
        for word in A:
            if word not in cc:
                queue = [word]
                while queue:
                    cur = queue.pop()
                    cc.add(cur)
                    for nx in graph[cur]:
                        if nx not in cc:
                            queue.append(nx)
                ans += 1
        return ans 

# https://leetcode.com/problems/similar-string-groups/solution/
from collections import defaultdict
class Solution:
    def numSimilarGroups(self, A) -> int:
        def similar(X, Y):
            res = 0
            for x, y in zip(X, Y):
                if x != y:
                    res += 1
                if res > 2:
                    return False
            return res == 2 or res == 0

        def dfs(node):
            visited.add(node)
            for next_node in edges[node]:
                if next_node not in visited:
                    dfs(next_node)

        def constructDictA():
            for i in range(length - 1):
                for j in range(i+1, length):
                    if similar(A[i], A[j]):
                        edges[A[i]].add(A[j])
                        edges[A[j]].add(A[i])

        def constructDictB():
            for s1 in A:
                for i in range(len_item - 1):
                    for j in range(i+1, len_item):
                        s2 = s1[:i] + s1[j] + s1[i+1:j] + s1[i] + s1[j+1:]
                        if s2 in set_A:
                            edges[s1].add(s2)
                            edges[s2].add(s1)

        set_A = set(A)
        A = list(set_A)
        length = len(A)
        len_item = len(A[0])
        edges = defaultdict(set)
        if length < len_item**2:
            constructDictA()
        else:
            constructDictB()
        # print(edges)
        visited = set()
        counts = 0
        for string in A:
            if string not in visited:
                counts += 1
                dfs(string)
        # print(color)
        return counts

S = Solution()
A = ["tars","rats","arts","star"]
print(S.numSimilarGroups(A))
A = ["abc","abc"]
print(S.numSimilarGroups(A))