"""
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        """
        wrong answer
        """
        bfs = set([0])
        # visited = set([0])
        steps = 0
        while bfs:
            # print(steps, bfs)
            if target in bfs:
                return steps
            steps += 1
            bfs2 = set()
            for num in bfs:
                for tmp in [num+steps, num-steps]:
                    # if tmp not in visited:
                        # visited.add(tmp)
                    bfs2.add(tmp)
            bfs = bfs2

# https://leetcode.com/problems/reach-a-number/discuss/257741/python-solution-beat-100-with
import math
class Solution:
    def reachNumber(self, target: int) -> int:
        """
        we can reach in dist = (1 + n) * n // 2 in n steps
        if dist == target, it is n
        if diff = dist - target, if diff is even, because the num is continous, we can alwasys change the sign of diff/2, to make the sum equal to target
        if it is odd, we try (n+1, n+2) then
        """
        target = abs(target)
        n = int(math.ceil((math.sqrt(1 + 8 * target) - 1) / 2))
        total = n * (n + 1) // 2
        while (total - target) % 2 != 0:
            n += 1
            total += n
        return n


S = Solution()
print(S.reachNumber(3))
print(S.reachNumber(2))
print(S.reachNumber(-1000000000))