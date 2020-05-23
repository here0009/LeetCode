"""
Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i], ..., A[N-1] in clockwise order.

Suppose you triangulate the polygon into N-2 triangles.  For each triangle, the value of that triangle is the product of the labels of the vertices, and the total score of the triangulation is the sum of these values over all N-2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

 

Example 1:

Input: [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:



Input: [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
Example 3:

Input: [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
 

Note:

3 <= A.length <= 50
1 <= A[i] <= 100
"""
"""
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/286754/C%2B%2BPython-O(n3)-DP-explanation-%2B-diagrams
"""   
from functools import lru_cache
class Solution_1:
    def minScoreTriangulation(self, A) -> int:
     
        @lru_cache(None)
        def dp(i,j):
            # print(i,j)
            if j-i < 2: #so i and j are in one edge
                return 0
            return min(dp(i,k)+dp(k,j)+A[i]*A[j]*A[k] for k in range(i+1,j))
        # print(A)
        return dp(0,len(A)-1)

"""
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/discuss/294265/Python-In-depth-Explanation-DP-For-Beginners
"""
class Solution:
    def minScoreTriangulation(self, A) -> int:
        n = len(A)
        dp = [[0]*n for _ in range(n)]
        #dp[i][j] represents the min cost to merge i~j to a triangle, in the bottom up solution, we need to merge from small to larger, the smallest one j-i = 2, and the largest is the result j-i = n-1
        for size in range(2,n):
            for left in range(0,n-size):
                right = left+size
                dp[left][right] = min(dp[left][k]+dp[k][right]+A[left]*A[right]*A[k] for k in range(left+1,right))
        # print(dp)
        return dp[0][-1]



S = Solution()
A = [1,2,3]
print(S.minScoreTriangulation(A))
A = [3,7,4,5]
print(S.minScoreTriangulation(A))
A = [1,3,1,4,1,5]
print(S.minScoreTriangulation(A))

