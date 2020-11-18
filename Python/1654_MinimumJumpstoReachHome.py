"""
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.

 

Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
Example 2:

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1
Example 3:

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.
 

Constraints:

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
All the elements in forbidden are distinct.
Position x is not forbidden.
"""


from typing import List
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited = set()
        forbidden = set(forbidden)
        bfs = [(0, 0)]
        jumps = 0
        # print('Input', forbidden, a, b, x)
        while bfs:
            bfs2 = []
            # print(bfs)
            for i,v in bfs:
                if i == x:
                    return jumps
                if (i+a, 0) not in visited and i+a not in forbidden and i+a <= 3*b+x:
                    bfs2.append((i+a, 0))
                    visited.add((i+a, 0))
                if v == 0 and i-b > 0 and (i-b, 1) not in visited and i-b not in forbidden:
                    bfs2.append((i-b, 1))
                    visited.add((i-b, 1))

            bfs = bfs2
            jumps += 1
        return -1

# https://leetcode.com/problems/minimum-jumps-to-reach-home/discuss/?currentPage=1&orderBy=most_votes&query=      
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, t: int) -> int:
        if not t: 
            return 0
        
        threshold = max(forbidden + [t]) + a + b
        forbidden = set(forbidden)
        seen = set([0])
        q = [[0,0]]

        while q:
            pos, steps = q.pop(0)
            if pos+a not in forbidden and pos+a not in seen and pos+a <= threshold: 
                # Termination Condition
                if pos+a == t: 
                    return steps+1
                q.append([pos+a, steps+1])
                seen.add(pos+a)

            if pos-b > 0 and pos-b not in forbidden and pos-b not in seen: 
                # Termination Condition
                if pos-b == t: 
                    return steps+1
                seen.add(pos-b)
                if pos-b+a not in forbidden and pos-b+a not in seen and pos-b+a <= threshold:
                    # Termination Condition
                    if pos-b+a == t: 
                        return steps+2
                    q.append([pos-b+a, steps+2])
                    seen.add(pos-b+a)
        return -1
S = Solution()
forbidden = [14,4,18,1,15]
a = 3
b = 15
x = 9
print(S.minimumJumps(forbidden, a, b, x))
forbidden = [8,3,16,6,12,20]
a = 15
b = 13
x = 11
print(S.minimumJumps(forbidden, a, b, x))
forbidden = [1,6,2,14,5,17,4]
a = 16
b = 9
x = 7
print(S.minimumJumps(forbidden, a, b, x))

forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
a = 29
b = 98
x = 80
print(S.minimumJumps(forbidden, a, b, x))
# 输出：
# -1
# 预期：
# 121