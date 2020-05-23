"""
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.
"""
class Solution:
    def smallestCommonElement(self, mat):
        common_set = set(mat[0])
        for i in range(1,len(mat)):
            common_set &= set(mat[i])
        if len(common_set) == 0:
            return -1
        else:
            return min(common_set)

s = Solution()
mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(s.smallestCommonElement(mat))
