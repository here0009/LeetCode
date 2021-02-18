"""
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

 
Example 1:

Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"
 

Note:

1 <= A.length <= 12
1 <= A[i].length <= 20
"""


from collections import defaultdict
class Solution:
    def shortestSuperstring(self, A) -> str:
        prefix = defaultdict(set)
        suffix = defaultdict(set)
        for i, word in enumerate(A):
            for j in range(len(word) - 1):
                prefix[word[:j]].add(i)
            for j in range(1, len(word)):
                suffix[word[j:]].add(i)
        edges_to = defaultdict(set)


from functools import lru_cache
from collections import defaultdict
from typing import List
class Solution:
    def shortestSuperstring(self, A) -> str:
        """
        Thoughts: 
        to find the correct solution, we must try every enumeration of A, which is len(A)!
        we can use dp to record the optimal solution of the subproblems we find during the iteration. the the idx of sub_superstring and the combination of strings can impact the following calculation.
        use dp(status, idx) to record the optimal solution of that status
        """
        def path(lst: List[int]) -> str:
            """
            str representaion of the list
            """
            res = A[lst[0]]
            for i in range(1, len(lst)):
                res += A[lst[i]][dist[lst[i - 1]][lst[i]]:]
            return res

        @lru_cache(None)
        def dp(status, idx):
            if status == target:
                return 0, [idx]
            score, lst = -1, []
            for i in range(len_A):
                if (1 << i) & status == 0:  # A[i] not visited
                    s2 = (1 << i) | status
                    tmp_score, tmp_lst = dp(s2, i)
                    if tmp_score + dist[idx][i] > score:
                        score = tmp_score + dist[idx][i]
                        lst = tmp_lst
            return score, [idx] + lst

        len_A = len(A)
        dist = [[0] * len_A for _ in range(len_A)]
        for i in range(len_A):
            for j in range(len_A):
                for k in range(min(len(A[i]), len(A[j])), 0, -1):
                    if A[j].startswith(A[i][-k:]):
                        dist[i][j] = k
                        # print(A[i], A[j], dist[i][j])
                        break

        target = (1 << len_A) - 1
        score, res = -1, []
        for i, v in enumerate(A):
            tmp_score, tmp_lst = dp(1 << i, i)
            if tmp_score > score:
                score = tmp_score
                res = tmp_lst

        # print([A[i] for i in res])
        return path(res)

S = Solution()
# A = ["alex","loves","leetcode"]
# print(S.shortestSuperstring(A))
A = ["catg","ctaagt","gcta","ttca","atgcatc"]
print(S.shortestSuperstring(A))

# Output
# "gctaagtttcatgcatc"
# Expected
# "gctaagttcatgcatc"
gctaagttcatgcatc