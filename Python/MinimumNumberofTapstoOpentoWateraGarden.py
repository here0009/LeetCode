"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
Example 3:

Input: n = 7, ranges = [1,2,1,0,2,1,0,1]
Output: 3
Example 4:

Input: n = 8, ranges = [4,0,0,0,0,0,0,0,4]
Output: 2
Example 5:

Input: n = 8, ranges = [4,0,0,0,4,0,0,0,4]
Output: 1

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100
"""


class Solution_1:
    """
    wrong answer for test case:
    n = 9
    ranges = [0,5,0,3,3,3,1,4,0,4]
    """
    def minTaps(self, n: int, ranges) -> int:
        stack = []
        for i,v in enumerate(ranges):
            left, right = max(0, i-v), min(n,i+v)
            while stack and (left <= stack[-1][0] and right >= stack[-1][1]):
                stack.pop()
            if not stack or (left < stack[-1][0] or right > stack[-1][1]):
                stack.append([left, right])

        print(stack)
        if stack[0][0] != 0 or stack[-1][1] != n:
            return -1
        for i in range(1, len(stack)):
            if stack[i][0] - stack[i-1][1] > 0:  # not ajacent
                return -1
        return len(stack)


class Solution:
    def minTaps(self, n: int, ranges) -> int:
        vals = []
        for i,v in enumerate(ranges):
            left, right = max(0, i-v), min(n,i+v)
            vals.append((left,right))
        vals = sorted(vals, key=lambda x: (x[0], -x[1]))  # left: samll to large, right: large to small
        stack = [vals[0]]
        for i in range(1,len(vals)):
            left, right = vals[i]
            if right <= stack[-1][1]:
                continue
            if left > stack[-1][1]:
                return -1
            while stack and left < stack[-1][0]:
                stack.pop()
            stack.append((stack[-1][1]+1, right))  # only append the extra part
        return len(stack)


class Solution:
    def minTaps(self, n: int, ranges) -> int:
        jumps = [0]*(n+1)  # store the longest distance we can get from i
        for i,v in enumerate(ranges):
            left, right = max(0, i-v), min(n,i+v)
            jumps[left] = max(jumps[left], right)
        start, end, steps = 0, 0, 0
        while end < n:
            start, end = end, max(jumps[start:end+1])
            if end <= start:
                return -1
            steps += 1
        return steps

S = Solution()
n = 5
ranges = [3,4,1,1,0,0]
print(S.minTaps(n, ranges))
n = 3
ranges = [0,0,0,0]
print(S.minTaps(n, ranges))
n = 7
ranges = [1,2,1,0,2,1,0,1]
print(S.minTaps(n, ranges))
n = 8
ranges = [4,0,0,0,0,0,0,0,4]
print(S.minTaps(n, ranges))
n = 8
ranges = [4,0,0,0,4,0,0,0,4]
print(S.minTaps(n, ranges))
n = 9
ranges = [0,5,0,3,3,3,1,4,0,4]
print(S.minTaps(n, ranges))