"""
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.
 

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
"""


from functools import lru_cache
class Solution_1:
    """
    wrong for test case:
    nums1 = [5,-4,-3]
    nums2 = [-4,-3,0,-4,2]
    """
    def maxDotProduct(self, nums1, nums2) -> int:
        row, col = len(nums1), len(nums2)
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = nums1[i]*nums2[j]

        for l in matrix:
            print(l)

        self.res = float('-inf')
        @lru_cache(None)
        def dfs(r, c):
            product = matrix[r][c]
            if c == col-1:
                self.res = max(self.res, product)
                print(r,c,product,self.res)
                return product
            dfs(r, c+1)
            if r+1 < row:
                tmp = max([dfs(i,c+1) for i in range(r+1, row)])
                if tmp > 0:
                    product += tmp
                    print(r,c,product,self.res)
            self.res = max(self.res, product)

            return product

        for i in range(row):
            dfs(i, 0)

        return self.res


class Solution_3:
    """
    Wrong answer
    """
    def maxDotProduct(self, nums1, nums2) -> int:

        row, col = len(nums1), len(nums2)
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = nums1[i] * nums2[j]
        for l in matrix:
            print(l)

        print("++++++++++++++++")
        pre = matrix[0][0]
        for j in range(1, col):
            if matrix[0][j] < pre:
                matrix[0][j] = pre
            else:
                pre = matrix[0][j]
        pre = matrix[0][0]
        for i in range(1, row):
            if matrix[i][0] < pre:
                matrix[i][0] = pre
            else:
                pre = matrix[i][0]
        for i in range(1, row):
            for j in range(1, col):
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]+matrix[i][j])

        for l in matrix:
            print(l)

        return matrix[-1][-1]



from functools import lru_cache
class Solution_2:
    def maxDotProduct(self, nums1, nums2) -> int:
        row, col = len(nums1), len(nums2)
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = nums1[i]*nums2[j]

        self.res = float('-inf')
        @lru_cache(None)
        def dfs(r, c):
            product = matrix[r][c]
            tmp = float('-inf')
            for i in range(r+1, row):
                for j in range(c+1, col):
                    tmp = max(dfs(i,j), tmp)
            if tmp > 0:
                product += tmp
            self.res = max(self.res, product)
            return product

        for i in range(row):
            dfs(i,0)
        for j in range(col):
            dfs(0,j)

        return self.res


class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        row, col = len(nums1), len(nums2)
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = nums1[i] * nums2[j]
        pre = matrix[0][0]
        for j in range(1, col):
            if matrix[0][j] < pre:
                matrix[0][j] = pre
            else:
                pre = matrix[0][j]
        pre = matrix[0][0]
        for i in range(1, row):
            if matrix[i][0] < pre:
                matrix[i][0] = pre
            else:
                pre = matrix[i][0]
        for i in range(1, row):
            for j in range(1, col):
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1], max(0,matrix[i-1][j-1])+matrix[i][j])
        return matrix[-1][-1]


class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        row, col = len(nums1), len(nums2)
        matrix = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                matrix[i][j] = nums1[i] * nums2[j]
                if i > 0 and j > 0:
                    matrix[i][j] += max(0, matrix[i - 1][j - 1])
                if i > 0:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j])
                if j > 0:
                    matrix[i][j] = max(matrix[i][j - 1], matrix[i][j])
        return matrix[-1][-1]


from functools import lru_cache
class Solution:
    def maxDotProduct(self, nums1, nums2) -> int:
        @lru_cache(None)
        def helper(i, j):
            if i == 0 or j == 0: 
                return float('-inf')
            return max(helper(i - 1, j - 1), helper(i, j - 1), helper(i - 1, j),
                       max(helper(i - 1, j - 1), 0) + nums1[i - 1] * nums2[j - 1])
        return helper(len(nums1), len(nums2))

S = Solution()

nums1 = [2,1,-2,5]
nums2 = [3,0,-6]
print(S.maxDotProduct(nums1, nums2))
nums1 = [3,-2]
nums2 = [2,-6,7]
print(S.maxDotProduct(nums1, nums2))
nums1 = [-1,-1]
nums2 = [1,1]
print(S.maxDotProduct(nums1, nums2))

nums1 = [5,-4,-3]
nums2 = [-4,-3,0,-4,2]
print(S.maxDotProduct(nums1, nums2))
# Output:
# 25
# Expected:
# 28

nums1 = [-5,3,-5,-3,1]
nums2 = [-2,4,2,5,-5]
print(S.maxDotProduct(nums1, nums2))
# Output:
# 47
# Expected:
# 50

nums1 = [-3,-8,3,-10,1,3,9]
nums2 = [9,2,3,7,-9,1,-8,5,-1,-1]
print(S.maxDotProduct(nums1, nums2))
# Output:
# 194
# Expected:
# 200
