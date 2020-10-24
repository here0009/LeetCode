"""
Given a picture consisting of black and white pixels, and a positive integer N, find the number of black pixels located at some specific row R and column C that align with all the following rules:

Row R and column C both contain exactly N black pixels.
For all rows that have a black pixel at column C, they should be exactly the same as row R
The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

Example:
Input:                                            
[['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'B', 'W', 'B', 'B', 'W'],    
 ['W', 'W', 'B', 'W', 'B', 'W']] 

N = 3
Output: 6
Explanation: All the bold 'B' are the black pixels we need (all 'B's at column 1 and 3).
        0    1    2    3    4    5         column index                                            
0    [['W', 'B', 'W', 'B', 'B', 'W'],    
1     ['W', 'B', 'W', 'B', 'B', 'W'],    
2     ['W', 'B', 'W', 'B', 'B', 'W'],    
3     ['W', 'W', 'B', 'W', 'B', 'W']]    
row index

Take 'B' at row R = 0 and column C = 1 as an example:
Rule 1, row R = 0 and column C = 1 both have exactly N = 3 black pixels. 
Rule 2, the rows have black pixel at column C = 1 are row 0, row 1 and row 2. They are exactly the same as row R = 0.

Note:
The range of width and height of the input 2D array is [1,200].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lonely-pixel-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
from collections import defaultdict
class Solution:
    def findBlackPixel(self, picture, N) -> int:
        row, col = len(picture), len(picture[0])
        c_counter = Counter()
        r_counter = Counter()
        row_sign = defaultdict(list)
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    r_counter[i] += 1
                    c_counter[j] += 1

        for i, lst in enumerate(picture):
            row_sign[''.join(lst)].append(i)
        # print(row_sign)
        res = 0
        for key, lst in row_sign.items():
            if len(lst) == N:  # we got N same rows, for a pixel (i,j) if c_counter[i] == r_counter[j] == N, then it meets all the requirements
                for j,v in enumerate(key):
                    if v == 'B' and c_counter[j] == N:
                        for i in lst:
                            if r_counter[i] == N:
                                res += 1
        return res


from collections import Counter
from collections import defaultdict
class Solution:
    def findBlackPixel(self, picture, N) -> int:
        row, col = len(picture), len(picture[0])
        c_counter = Counter()
        r_counter = Counter()
        row_sign = defaultdict(list)
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    r_counter[i] += 1
                    c_counter[j] += 1

        for i, lst in enumerate(picture):
            row_sign[''.join(lst)].append(i)
        # print(row_sign)
        res = 0
        for key, lst in row_sign.items():
            if len(lst) == N and sum(k == 'B' for k in key) == N:
            # we got N same rows, for a pixel (i,j) if c_counter[i] == r_counter[j] == N, then it meets all the requirements
                for j,v in enumerate(key):
                    if v == 'B' and c_counter[j] == N:
                        res += N
        return res

S = Solution()
picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","W","B","W","B","W"]]
N = 3
print(S.findBlackPixel(picture, N))

picture = [["W","B","W","B","B","W"],["W","B","W","B","B","W"],["W","B","W","B","B","W"],["B","W","B","W","W","B"]]
N = 1
print(S.findBlackPixel(picture, N))
# 输出：
# 3
# 预期结果：
# 0