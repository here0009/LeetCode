"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
import math
class Solution_1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        Thoughts:Mathmatical way to do it.
        you need to choose m-1 down arrows and n-1 right arrows from the start to the finish point.
        you got m+n-2 cups, and place n-1 balls in it. the combination number is (m+n-2)!/((n-1)!*(m-1)!)
        """
        return int(math.factorial(m+n-2)/math.factorial(n-1)/math.factorial(m-1))

s = Solution()

m = 3
n = 2
print(s.uniquePaths(m,n))

m = 7
n = 3
print(s.uniquePaths(m,n))

m = 2
n = 2
print(s.uniquePaths(m,n))

m = 1
n = 1
print(s.uniquePaths(m,n))