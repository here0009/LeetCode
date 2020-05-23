"""
Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

 

Example 1:


Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.
Example 2:

Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0
Example 3:

Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3
Example 4:

Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2
 

Constraints:

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5
"""
class Solution_1:
    def maxSideLength(self, mat, threshold: int) -> int:
        res = 0
        m, n = len(mat), len(mat[0])
        row_sum = [row[:] for row in mat]
        col_sum = [row[:] for row in mat]
        corners_sum = [[0]*n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(n):
                row_sum[i][j] += row_sum[i-1][j]
        for row in row_sum:
            print(row)
        print('==================')
        for i in range(m):
            for j in range(1,n):
                col_sum[i][j] += col_sum[i][j-1]
        for row in col_sum:
            print(row)
        print('==================')
        for row in mat:
            print(row)
        print('==================')
        check_flag = True
        for i in range(m):
            for j in range(n):
                if check_flag and corners_sum[i][j] <= threshold:
                    check_flag = False
                    res += 1
        check_flag = True
        for i in range(1,m):
            for j in range(1,n):
                corners_sum[i][j] = sum([mat[i][j], mat[i-1][j-1],mat[i-1][j],mat[i][j-1]])
                if check_flag and corners_sum[i][j] <= threshold:
                    check_flag = False
                    res += 1
        print(res)
        for row in corners_sum:
            print(row)
        while True:
            corners_sum2 = [row[:] for row in corners_sum]
            for i in range(m):
                for j in range(n):
                    pass
"""
Thoughts:use dp[i][j] to store the sum from 0,0 to matrix[i][j], so
the sum of square(length k) is dp[i][j] + dp[i-k][j-k] - dp[i-k][j] - dp[i][j-k]
"""
class Solution:
    def maxSideLength(self, mat, threshold: int) -> int:
        def check(length):
            # print(length,low,high,mid)
            for i in range(length,m+1):
                for j in range(length,n+1):
                    t = dp[i][j] - dp[i-length][j] - dp[i][j-length] + dp[i-length][j-length]
                    if t <= threshold:
                        return True
            return False


        m,n = len(mat), len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1,m+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + mat[i-1][j-1]
        # for row in dp:
        #     print(row)
        low, high = 0, min(m,n)
        while low <= high:
            mid = (low + high)//2
            if check(mid):
                low = mid+1
            else:
                high = mid-1
        return high


mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]
threshold = 4

s = Solution()
print(s.maxSideLength(mat, threshold))


mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]]
threshold = 1
print(s.maxSideLength(mat, threshold))

mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
threshold = 6
print(s.maxSideLength(mat, threshold))

mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]]
threshold = 40184
print(s.maxSideLength(mat, threshold))