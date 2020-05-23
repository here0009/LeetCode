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
        """
        steps = 0
        bfs = [(0,1)]
        visited = set()
        while bfs:
            bfs2 = []
            # print(bfs)
            for pos,speed in bfs:
                if (pos < 0 and speed < 0) or (pos > 2*target and speed > 2*target):
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


S = Solution()
target = 3
print(S.racecar(target))
target = 6
print(S.racecar(target))