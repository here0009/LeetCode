"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000
"""
class Solution:
    def sumZero(self, n: int):
        res = []
        # print([-i for i in range(1,n+1)])
        if n % 2 == 1:
            res.append(0)
            n -= 1
        n = n//2
        return res + [i for i in range(1,n+1)] + [-i for i in range(1,n+1)]
        
s = Solution()
# n = 5
# print(s.sumZero(n))

# n = 3
# print(s.sumZero(n))

# n = 1
# print(s.sumZero(n))

for n in range(1,10):
    print(s.sumZero(n))