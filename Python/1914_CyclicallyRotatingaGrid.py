"""
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.

 

Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:

  
Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109
"""


from typing import List
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        def get_value(layer, r, k):
            return layers[layer][(r + k) % len(layers[layer])]

        R, C = len(grid), len(grid[0])
        layers = []
        layer = 0
        rank = dict()
        while layer < min(R, C)//2:
            layers.append([])
            for j in range(layer, C - layer - 1):
                layers[-1].append(grid[layer][j])
                rank[(layer, j)] = (layer, len(layers[-1]) - 1)
            for i in range(layer, R - layer - 1):
                layers[-1].append(grid[i][C - layer - 1])
                rank[(i, C - layer - 1)] = (layer, len(layers[-1]) - 1)
            for j in range(C - layer - 1, layer, -1):
                layers[-1].append(grid[R - layer - 1][j])
                rank[(R - layer - 1, j)] = (layer, len(layers[-1]) - 1)
            for i in range(R - layer - 1, layer, -1):
                layers[-1].append(grid[i][layer])
                rank[(i, layer)] = (layer, len(layers[-1]) - 1)
            layer += 1
        
        # for row in layers:
        #     print(row)

        res = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                layer, r = rank[(i, j)]
                res[i][j] = get_value(layer, r, k)
        return res

S = Solution()

grid = [[40,10],[30,20]]
k = 1
print(S.rotateGrid(grid, k))
grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
k = 2
print(S.rotateGrid(grid, k))