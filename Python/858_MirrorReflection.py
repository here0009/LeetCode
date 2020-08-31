"""
There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.



Note:

1 <= p <= 1000
0 <= q <= p
"""


"""
https://leetcode.com/problems/mirror-reflection/discuss/141773/C%2B%2BJavaPython-1-line-without-using-any-package-or
"""
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        """
        m : the number of room extensions
        n : the number of light reflection
        and when the light meet the corner, we have:
        m*p = n*q
        if m is even, n is odd, return 0
        if m is odd, n is even, return 2
        if m is odd, n is odd, return 1
        m, n can not be even at the same time, otherwise we always divid 2 to both of them
        """
        m, n = 1, 1
        while (m*p != n*q):
            n += 1 #because q <= p, add n will find the smallest answer
            m = n*q//p
        if m % 2 == 0 and n % 2 == 1:
            return 0
        if m % 2 == 1 and n % 2 == 0:
            return 2
        if m % 2 == 1 and n % 2 == 1:
            return 1
        return -1

S = Solution()
p = 2
q = 1
print(S.mirrorReflection(p, q))