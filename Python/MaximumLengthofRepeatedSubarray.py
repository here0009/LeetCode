"""
Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 

Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""
class Solution_1:
    def findLength(self, A, B) -> int:
        len_a = len(A)
        len_b = len(B)
        matrix = [[0]*(len_a+1) for _ in range(len_b+1)]
        res = 0
        for i in range(1,len_a+1):
            for j in range(1,len_b+1):
                if A[i-1] == B[j-1]:
                    matrix[i][j] = matrix[i-1][j-1] + 1
                    res = max(res, matrix[i][j])
        # for row in matrix:
        #     print(row)
        return res

class Solution:
    def findLength(self, A, B):
        A, res, sub = "X%sX" % "X".join(map(str, A)), 0, "X"
        # print(A)
        # print('+++++++++')
        for num in B:
            sub += str(num) + "X" #only find subsequences that longer than res
            # print(sub)
            if sub in A:
                res += 1
            else: 
                # print('pre',sub)
                sub = sub[sub[1:].index("X") + 1:]
                # print('after',sub)
        return res

s = Solution()
A = [1,2,3,2,1]
B = [3,2,1,4,7]
print(s.findLength(A,B))



