"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-rectangle-enclosing-black-pixels
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def minArea(self, image, x: int, y: int) -> int:
        def dfs(i, j):
            visited[i][j] = 1
            n, e, w, s = self.news
            self.news = [min(i,n), max(j,e), min(j,w), max(i,s)]
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i+di, j+dj
                # print(ni,nj)
                if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0 and image[ni][nj] == '1':
                    dfs(ni, nj)

        R, C = len(image), len(image[0])
        visited = [[0]*C for _ in range(R)]
        self.news = [x, y, y, x] #the outer limits of black pixels
        dfs(x, y)
        n, e, w, s = self.news
        # print(self.news)
        return (e-w+1)*(s-n+1)

S = Solution()
image = ["0010","0110","0100"]
x = 0
y = 2
print(S.minArea(image, x, y))
