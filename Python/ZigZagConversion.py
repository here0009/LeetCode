"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def dfs(i, j, k):
            """
            i for row, j for col, k for index of string
            """
            if k >= length:
                return
            res[i] += s[k]
            if j % (numRows-1)== 0 and i != numRows - 1:
                dfs(i+1, j, k+1)
            else:
                dfs(i-1, j+1, k+1)

        # print('s:',s)
        if numRows == 1:
            return s
        res = ['']*numRows
        index = 0
        length = len(s)
        i,j,k = 0,0,0
        dfs(i,j,k)
        for row in res:
            print(row)
        return ''.join(res)



class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = ['']*numRows
        row = 0
        direction = 1
        for c in s:
            # print(row)
            res[row] += c
            if row == 0:
                direction = 1
            elif row == numRows-1:
                direction = -1
            row += direction
        return ''.join(res)


S = Solution()
s = "PAYPALISHIRING"
numRows = 3
print(S.convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 4
print(S.convert(s, numRows))
s = "PAYPALISHIRING"
numRows = 1
print(S.convert(s, numRows))