"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""
class Solution:
    def integerReplacement(self, n: int) -> int:
        bfs = {n}
        visited = {n}
        steps = 0
        while True:
            if 1 in bfs:
                return steps
            bfs2 = set()
            steps += 1
            for i in bfs:
                if i % 2 == 0:
                    j = i//2
                    if j not in visited:
                        visited.add(j)
                        bfs2.add(j)
                else:
                    p = i+1
                    q = i-1
                    if p not in visited:
                        visited.add(p)
                        bfs2.add(p)
                    if q not in visited:
                        visited.add(q)
                        bfs2.add(q)
            bfs = bfs2

s = Solution()
print(s.integerReplacement(8))
print(s.integerReplacement(7))