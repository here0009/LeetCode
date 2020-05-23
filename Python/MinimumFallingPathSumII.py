"""
Given a square grid of integers arr, a falling path with non-zero shifts is a choice of exactly one element from each row of arr, such that no two elements chosen in adjacent rows are in the same column.

Return the minimum sum of a falling path with non-zero shifts.

 

Example 1:

Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation: 
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
 

Constraints:

1 <= arr.length == arr[i].length <= 200
-99 <= arr[i][j] <= 99
"""
class Solution:
    def minFallingPathSum(self, arr) -> int:
        """
        TLE
        """
        def dfs(r_index,pre_col,score):
            # print(r_index, pre_col,score)
            #start for row i, col j in matrix
            if r_index == r: #the end
                self.score = min(self.score, score)
                return
            for value,col in min_2_matrix[r_index]:
                if col != pre_col:
                    dfs(r_index+1, col, score+value)


        min_2_matrix = [] #record the min 2 of each row
        for row in arr:
            min_2_matrix.append(sorted((v,i) for i,v in enumerate(row))[:2])
        r,c = len(arr), len(arr[0])
        self.score = float('inf')
        dfs(0,-1,0)
        return self.score

class Solution:
    def minFallingPathSum(self, arr) -> int:
        """
        do not use dfs, but use dp to store the min values
        """

        min_2_matrix = [] #record the min 2 of each row
        for row in arr:
            min_2_matrix.append(sorted([v,i] for i,v in enumerate(row))[:2])

        v1,i1 = min_2_matrix[0][0]
        v2,i2 = min_2_matrix[0][1]
        for r in range(1,len(min_2_matrix)):
            tmp_v1,tmp_i1 = min_2_matrix[r][0]
            tmp_v2,tmp_i2 = min_2_matrix[r][1]
            if tmp_i1 != i1:
                tmp_v1 += v1
            else:
                tmp_v1 += v2
            if tmp_i2 != i1:
                tmp_v2 += v1
            else:
                tmp_v2 += v2
            tmp = sorted([(tmp_v1, tmp_i1),(tmp_v2, tmp_i2)])
            v1,i1 = tmp[0]
            v2,i2 = tmp[1]
        return min(v1,v2)




S = Solution()
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(S.minFallingPathSum(arr))


arr = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
# Output
# -155
# Expected
# -192
print(S.minFallingPathSum(arr))