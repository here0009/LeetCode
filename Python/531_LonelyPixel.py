"""
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:
Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:
The range of width and height of the input 2D array is [1,500].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lonely-pixel-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def findLonelyPixel(self, picture) -> int:
        r_counter = Counter()
        c_counter = Counter()
        row, col = len(picture), len(picture[0])
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B':
                    r_counter[i] += 1
                    c_counter[j] += 1
        res = 0
        for i in range(row):
            for j in range(col):
                if picture[i][j] == 'B' and r_counter[i] == 1 and c_counter[j] == 1:
                    res += 1
        return res

S = Solution()
picture = [['W', 'W', 'B'],['W', 'B', 'W'],['B', 'W', 'W']]
print(S.findLonelyPixel(picture))