"""
There is a box protected by a password. The password is a sequence of n digits where each digit can be one of the first k digits 0, 1, ..., k-1.

While entering a password, the last n digits entered will automatically be matched against the correct password.

For example, assuming the correct password is "345", if you type "012345", the box will open because the correct password matches the suffix of the entered password.

Return any password of minimum length that is guaranteed to open the box at some point of entering it.

 

Example 1:

Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.
Example 2:

Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.
 

Note:

n will be in the range [1, 4].
k will be in the range [1, 10].
k^n will be at most 4096.
"""


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        Thoughts:
        start with '0'*(n-1), curr = pre[1:] + 'i', if curr not visited before, we add curr to the list. iterate until there's no place to go
        post order traverse: do not understand this part, it is called Hierholzer's Algorithm 
        """
        def dfs(start):
            print(start, res, visited)
            for i in range(k):
                curr = start + str(i)
                if curr not in visited:
                    visited.add(curr)
                    dfs(curr[1:])
                    res.append(str(i))



        start = '0' * (n - 1)
        res = []
        visited = set()
        dfs(start)
        return ''.join(res) + '0' * (n - 1)


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        """
        Thoughts:
        start with '0'*(n-1), curr = pre[1:] + 'i', if curr not visited before, we add curr to the list. iterate until there's no place to go
        this solution use backtrack is more understandable
        """
        def dfs(curr):
            if len(visited) == target_len:
                return curr
            for i in range(k):
                nxt = curr[-(n - 1):] + str(i) if n != 1 else str(i)
                if nxt not in visited:
                    visited.add(nxt)
                    res = dfs(curr + str(i))
                    if res:
                        return res
                    visited.remove(nxt)

        start = '0' * n
        visited = set([start])
        target_len = k**n
        return dfs(start)

# https://leetcode.com/problems/cracking-the-safe/discuss/502204/Python-Euler-Path-(99.47-Faster-~15-Lines)
from itertools import product
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        digits, G, res = range(k), {}, []
        nodes = list(product(digits, repeat=n - 1))
        for node in nodes:
            G[node] = list(range(k))

        node = tuple([0] * (n - 1))
        res.extend(node)
        while node in G and G[node]:
            edge = G[node].pop()
            res.extend([edge])
            node = tuple(node + (edge,))[1:]
        return "".join(str(ch) for ch in res)


S = Solution()
print(S.crackSafe(1, 2))
print(S.crackSafe(2, 2))

