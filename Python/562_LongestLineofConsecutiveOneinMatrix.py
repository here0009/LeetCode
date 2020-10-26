"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-line-of-consecutive-one-in-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def longestLine(self, M) -> int:
        if not M:
            return 0
        res = 0
        R, C = len(M), len(M[0])
        r, c, d, ad = Counter(), Counter(), Counter(), Counter()
        for i in range(R):
            for j in range(C):
                num = M[i][j]
                r[i] = num*r[i] + num
                c[j] = num*c[j] + num
                d[j-i] = d[j-i]*num + num
                ad[i+j] = ad[i+j]*num + num
                res = max(res, r[i], c[j], d[j-i], ad[i+j])
        return res


S = Solution()
M = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
print(S.longestLine(M))
