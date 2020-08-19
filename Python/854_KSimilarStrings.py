"""
Strings A and B are K-similar (for some non-negative integer K) if we can swap the positions of two letters in A exactly K times so that the resulting string equals B.

Given two anagrams A and B, return the smallest K for which A and B are K-similar.

Example 1:

Input: A = "ab", B = "ba"
Output: 1
Example 2:

Input: A = "abc", B = "bca"
Output: 2
Example 3:

Input: A = "abac", B = "baca"
Output: 2
Example 4:

Input: A = "aabc", B = "abca"
Output: 2
Note:

1 <= A.length == B.length <= 20
A and B contain only lowercase letters from the set {'a', 'b', 'c', 'd', 'e', 'f'}
"""


class Solution:
    """
    Time Limit Exceeded
    """
    def kSimilarity(self, A: str, B: str) -> int:
        def swapPos(string):
            for i in range(length-1):
                for j in range(i+1, length):
                    s2 = string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
                    if s2 not in visited:
                        visited.add(s2)
                        yield s2

        visited = {A}
        bfs = {A}
        res = 0
        length = len(A)
        if A == B:
            return 0
        while bfs:
            # print(bfs)
            bfs2 = set()
            for string in bfs:
                for new_string in swapPos(string):
                    if new_string == B:
                        return res
                    bfs2.add(new_string)
            res += 1
            bfs = bfs2


from collections import deque
class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        def swapPos(string):
            i = 0
            while string[i] == B[i]:
                i += 1
            for j in range(i+1, length):
                if string[j] == B[i] and string[j] != B[j]:
                    yield string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]

        dq = deque([(A, 0)])
        visited = set(A)
        length = len(A)
        while dq:
            string, dist = dq.popleft()
            if string == B:
                return dist
            for s2 in swapPos(string):
                if s2 not in visited:
                    dq.append((s2, dist+1))
                    visited.add(s2)


S = Solution()
A = "ab"
B = "ba"
print(S.kSimilarity(A, B))
A = "abc"
B = "bca"
print(S.kSimilarity(A, B))
A = "abac"
B = "baca"
print(S.kSimilarity(A, B))
A = "aabc"
B = "abca"
print(S.kSimilarity(A, B))
A = "abccaacceecdeea"
B = "bcaacceeccdeaae"
print(S.kSimilarity(A, B))