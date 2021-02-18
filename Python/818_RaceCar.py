"""
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.
Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.
 

Note:

1 <= target <= 10000.
"""
class Solution:
    def racecar(self, target: int) -> int:
        """
        TLE
        """
        steps = 0
        bfs = [(0,1)]
        visited = set()
        while bfs:
            bfs2 = []
            # print(bfs)
            for pos,speed in bfs:
                if (pos < 0 and speed < 0):
                    continue
                visited.add((pos,speed))
                if pos == target:
                    return steps
                if (pos+speed, speed*2) not in visited:
                    bfs2.append((pos+speed, speed*2))
                if speed > 0 and (pos, -1) not in visited:
                    bfs2.append((pos, -1))
                elif speed < 0 and (pos, 1) not in visited:
                    bfs2.append((pos, 1))
            steps += 1
            bfs = bfs2
        return None


class Solution:
    def racecar(self, target: int) -> int:
        """
        TLE 
        49 / 53
        test case : target  = 5478
        """
        steps = 0
        bfs = [(0,1)]
        visited = set()
        while bfs:
            bfs2 = []
            # print(bfs)
            for pos,speed in bfs:
                if abs(pos) > 2*target and abs(speed) > 2*target:
                    continue
                visited.add((pos,speed))
                if pos == target:
                    return steps
                if (pos+speed, speed*2) not in visited:
                    bfs2.append((pos+speed, speed*2))
                if speed > 0 and (pos, -1) not in visited:
                    bfs2.append((pos, -1))
                elif speed < 0 and (pos, 1) not in visited:
                    bfs2.append((pos, 1))
            steps += 1
            bfs = bfs2
        return None


class Solution:
    def racecar(self, target: int) -> int:
        """
        TLE 
        49 / 53
        test case : target  = 5478
        """
        steps = 0
        bfs = [(0,1)]
        visited = set()
        while bfs:
            bfs2 = []
            # print(bfs)
            for pos, speed in bfs:
                if (pos * speed > 0) and abs(pos) > 2*target and abs(speed) > 2*target:
                    continue
                visited.add((pos,speed))
                if pos == target:
                    return steps
                if (pos+speed, speed*2) not in visited:
                    bfs2.append((pos+speed, speed*2))
                if speed > 0 and (pos, -1) not in visited:
                    bfs2.append((pos, -1))
                elif speed < 0 and (pos, 1) not in visited:
                    bfs2.append((pos, 1))
            steps += 1
            bfs = bfs2
        return None

from functools import lru_cache
class Solution:
    def racecar(self, target: int) -> int:
        """
        may be we can use greed method to get the optimal solution
        A until we get or pass target, then reverse the direction
        """
        @lru_cache(None)
        def dp(pos, speed, target):
            steps = 0
            if pos == target:
                return 0
            while pos + speed < target:
                steps += 1
                pos += speed
                speed *= 2
            # pos + speed >= target, we choose to either AR or RR
            # RR, decrease speed to 1, then get to pos
            # AR from pos + speed to target with speed -1, equal to dp(post + speed - target , 1)
            return 2 + steps + min(dp(pos, 1), dp(0, 1, post + speed - target))

        return dp(0, 1, target)


from functools import lru_cache
class Solution:
    def racecar(self, target: int) -> int:
        """
        may be we can use greed method to get the optimal solution
        A until we get or pass target, then reverse the direction
        not correct, we may return in the middle, then goes to the target with less steps
        """
        @lru_cache(None)
        def dp(speed, pos):
            # print(speed, pos)
            steps = 0
            if pos == 0:
                return 0
            while pos - speed > 0:  # we can not get to pos directly with current speed
                steps += 1
                pos -= speed
                speed *= 2
            if speed == pos:
                return steps + 1
            # pos + speed >= target, we choose to either ARR or RR
            # RR, decrease speed to 1, then get to pos
            # AR from pos + speed to target with speed -1, equal to dp(post + speed - target , 1)
            return 2 + steps + min(dp(1, pos), dp(1, speed - pos))

        return dp(1, target)


class Solution:
    def racecar(self, target: int) -> int:
        """
        https://leetcode.com/problems/race-car/discuss/143993/Python-AC-BFS-and-Heapq-Solutions
        """
        steps = 0
        bfs = [(0,1)]
        boundary = 20000
        visited = set(bfs)
        while bfs:
            bfs2 = []
            for pos, speed in bfs:
                if pos == target:
                    return steps
                if abs(pos) > boundary:
                    continue
                if (pos+speed, speed*2) not in visited:
                    bfs2.append((pos+speed, speed*2))
                    visited.add((pos+speed, speed*2))
                if speed > 0 and (pos, -1) not in visited:
                    bfs2.append((pos, -1))
                    visited.add((pos, -1))
                elif speed < 0 and (pos, 1) not in visited:
                    bfs2.append((pos, 1))
                    visited.add((pos, 1))
            steps += 1
            bfs = bfs2
        return None

import heapq
class Solution:
    def racecar(self, target):
        target *= -1
        q, used = [(0, 0, -1)], {(0, -1)}  # if cnt and pos are same, make larger speed pop 1st, improve efficiency a little bit
        while q:
            cnt, pos, speed = heapq.heappop(q)
            if pos == target:
                return cnt
            elif pos > 20000 or -20000 > pos:
                continue
            if (pos + speed, speed * 2) not in used:
                heapq.heappush(q, (cnt + 1, pos + speed, speed * 2))
                used.add((pos + speed, speed * 2))
            if speed < 0 and (pos, 1) not in used:
                heapq.heappush(q, (cnt + 1, pos, 1))
                used.add((pos, 1))
            elif speed > 0 and (pos, -1) not in used:
                heapq.heappush(q, (cnt + 1, pos, -1))
                used.add((pos, -1))


from functools import lru_cache
class Solution:
    def racecar(self, target: int) -> int:
        """
        may be we can use greed method to get the optimal solution
        A until we get or pass target, then reverse the direction
        not correct, we may return in the middle, then goes to the target with less steps
        """
        @lru_cache(None)
        def dp(speed, pos):
            # print(speed, pos)
            steps = 0
            if pos == 0:
                return 0
            while pos - speed > 0:  # we can not get to pos directly with current speed
                steps += 1
                pos -= speed
                speed *= 2
            if speed == pos:
                return steps + 1
            # pos + speed >= target, we choose to either ARR or RR
            # RR, decrease speed to 1, then get to pos
            # AR from pos + speed to target with speed -1, equal to dp(post + speed - target , 1)
            res = 2 + steps + dp(1, speed - pos) # A, R then dp(1, speed - pos)
            for i in range(steps):  # reverse,  do i 'A', then go to pos
                res = min(res, 1 + i + dp(i, pos))

            return 2 + steps + min(dp(1, pos), dp(1, speed - pos))

        return dp(1, target)


# https://leetcode.com/problems/race-car/discuss/123834/JavaC%2B%2BPython-DP-solution
from functools import lru_cache
class Solution:
    def racecar(self, target: int) -> int:
        """
        Thought: greedy method can not get to the optimal solution 
        we may accelerate until speed + pos > target with n steps , and we can accelerate one more, then go back
        or we can go back and take m steps,  m in [0, n), then reach for pos. m could be more than 0
        use the previouse method, it hard to record the original pos.
        so use dp[t] to represent the min steps to get t from 0
        n = t.bit_length. if t == 2**n - 1, then we need n step to get t, just n*A
        """
        @lru_cache(None)
        def dp(t):
            if t == 0:
                return 0
            n = t.bit_length()
            if (1 << n) - 1 == t:
                return n
            res = dp((1 << n) - 1 - t) + n + 1  # n*A + 1R
            for m in range(n - 1):
                res = min(res, dp(t - (1 << n - 1) + (1 << m)) + n + m + 1)   # (n-1)*A + 1R + m*A + 1R
            return res
        return dp(target)


S = Solution()
target = 3
print(S.racecar(target))
target = 6
print(S.racecar(target))
target  = 5478
print(S.racecar(target))
# Output
# 53
# Expected
# 50