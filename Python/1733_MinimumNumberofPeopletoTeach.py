"""
On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
 

Constraints:

2 <= n <= 500
languages.length == m
1 <= m <= 500
1 <= languages[i].length <= n
1 <= languages[i][j] <= n
1 <= u​​​​​​i < v​​​​​​i <= languages.length
1 <= friendships.length <= 500
All tuples (u​​​​​i, v​​​​​​i) are unique
languages[i] contains only unique values
"""


from typing import List
from collections import defaultdict
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        """
        wrong answer, even non of the friends of p speak k, it is still possible that we teach p speak k, and get a min value
        """
        def dfs(p):
            if p == m + 1:
                return 0
            candi = set()
            for q in f_edges[p]:
                if q > p and not l_edges[p] & l_edges[q]:
                    candi |= l_edges[q]
            if not candi:
                return dfs(p + 1)
            res = float('inf')
            for lang in candi:
                # l_edges[p].add(lang)
                res = min(res, 1 + dfs(p + 1))
                # l_edges[p].remove(lang)
            # print(p, candi, res, l_edges)
            return res

        f_edges = defaultdict(set)
        m = len(languages)
        for p, q in friendships:
            f_edges[p].add(q)
            f_edges[q].add(p)
        l_edges = defaultdict(set)

        for i, lst in enumerate(languages, 1):
            l_edges[i] = set(lst)
        print('f_edges', f_edges)
        print('l_edges', l_edges)
        return dfs(1)


from typing import List
from collections import defaultdict
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        def teach(lang):
            res = 0
            for p in range(1, m + 1):
                if lang not in l_edges[p] and p in non_comm:
                    res += 1
            return res

        f_edges = defaultdict(set)
        m = len(languages)
        for p, q in friendships:
            f_edges[p].add(q)
            f_edges[q].add(p)
        l_edges = defaultdict(set)

        for i, lst in enumerate(languages, 1):
            l_edges[i] = set(lst)

        non_comm = set()
        for p, q in friendships:
            if not l_edges[p] & l_edges[q]:
                non_comm.add(p)
                non_comm.add(q)
        res = m
        for lang in range(1, n + 1):
            res = min(res, teach(lang))
        return res

S = Solution()
n = 2
languages = [[1],[2],[1,2]]
friendships = [[1,2],[1,3],[2,3]]
print(S.minimumTeachings(n, languages, friendships))

n = 3
languages = [[2],[1,3],[1,2],[3]]
friendships = [[1,4],[1,2],[3,4],[2,3]]
print(S.minimumTeachings(n, languages, friendships))

n = 17
languages = [[4,7,2,14,6],[15,13,6,3,2,7,10,8,12,4,9],[16],[10],[10,3],[4,12,8,1,16,5,15,17,13],[4,13,15,8,17,3,6,14,5,10],[11,4,13,8,3,14,5,7,15,6,9,17,2,16,12],[4,14,6],[16,17,9,3,11,14,10,12,1,8,13,4,5,6],[14],[7,14],[17,15,10,3,2,12,16,14,1,7,9,6,4]]
friendships = [[4,11],[3,5],[7,10],[10,12],[5,7],[4,5],[3,8],[1,5],[1,6],[7,8],[4,12],[2,4],[8,9],[3,10],[4,7],[5,12],[4,9],[1,4],[2,8],[1,2],[3,4],[5,10],[2,7],[1,7],[1,8],[8,10],[1,9],[1,10],[6,7],[3,7],[8,12],[7,9],[9,11],[2,5],[2,3]]
print(S.minimumTeachings(n, languages, friendships))
