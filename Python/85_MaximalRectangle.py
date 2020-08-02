"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""


class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        if len(matrix) == 1:
            curr = 0
            res = 0
            for row in matrix:
                for num in row:
                    if num == '1':
                        curr += 1
                        res = max(res, curr)
                    else:
                        curr = 0
            return res
        row = [0]*n
        res = 0

        for i in range(len(matrix)):
            next_row = [0]*n
            stack = []
            for j in range(n):
                v = 0
                if matrix[i][j] == '1':
                    v = 1 + row[j]
                    next_row[j] = v
                stack.append((j, v))
                while stack and stack[-1][1] >= v:
                    index = stack.pop()[0]
                stack.append((index, v))
                # print(stack)
                for s_i,s_v in stack:
                    # print(ii)
                    res = max(res, s_v*(j - s_i + 1))
            row = next_row[:]
            # print(row)
        return res


class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        height = [0]*(n + 1)
        res = 0 
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            print(height)
            for i in range(n + 1):
                print('stack',stack)
                print('height',[height[i] for i in stack])
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1] #e.g. [2,3,4,5,0] if i == 0, h = 3, i-1 = 3, stack[-1] = 0, because stack is ascending, so height[i-1] >= h, or h will be poped before
                    print(h, i, stack)
                    res = max(res, h * w)
                stack.append(i)
        return res




S = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(S.maximalRectangle(matrix))
# matrix = ["1","0","0","1","1"]
# print(S.maximalRectangle(matrix))
# matrix = [['0']]
# print(S.maximalRectangle(matrix))
# matrix = [["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]
# print(S.maximalRectangle(matrix))
# matrix = [['1']]
# print(S.maximalRectangle(matrix))