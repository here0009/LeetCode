"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""
class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for astd in asteroids:
            if not res or res[-1] < 0 or astd > 0:
                res.append(astd)
            else:
                #res[-1] > 0 and astd < 0
                while res and res[-1] > 0 and astd != 0:
                    k = res[-1]
                    if abs(astd) < abs(k):
                        astd = 0
                    elif abs(astd) > abs(k):
                        res.pop()
                    else:
                        res.pop()
                        astd = 0
                if astd != 0:
                    res.append(astd)
        return res

class Solution:
    def asteroidCollision(self, asteroids):
        res = []
        for astd in asteroids:
            while res and res[-1] > 0 and astd < 0:
                k = res[-1]
                if abs(astd) < abs(k):
                    astd = 0
                elif abs(astd) > abs(k):
                    res.pop()
                else:
                    astd = 0
                    res.pop()
            if astd != 0:
                res.append(astd)
        return res

s = Solution()
asteroids = [5, 10, -5]
print(s.asteroidCollision(asteroids))

asteroids = [8, -8]
print(s.asteroidCollision(asteroids))

asteroids = [10, 2, -5]
print(s.asteroidCollision(asteroids))

asteroids = [-2, -1, 1, 2]
print(s.asteroidCollision(asteroids))

asteroids = [-2,-2,1,-2]
print(s.asteroidCollision(asteroids))