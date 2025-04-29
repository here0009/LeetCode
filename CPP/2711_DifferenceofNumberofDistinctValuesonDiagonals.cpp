/*
Given a 2D grid of size m x n, you should find the matrix answer of size m x n.

The cell answer[r][c] is calculated by looking at the diagonal values of the cell grid[r][c]:

Let leftAbove[r][c] be the number of distinct values on the diagonal to the left and above the cell grid[r][c] not including the cell grid[r][c] itself.
Let rightBelow[r][c] be the number of distinct values on the diagonal to the right and below the cell grid[r][c], not including the cell grid[r][c] itself.
Then answer[r][c] = |leftAbove[r][c] - rightBelow[r][c]|.
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until the end of the matrix is reached.

For example, in the below diagram the diagonal is highlighted using the cell with indices (2, 3) colored gray:
Red-colored cells are left and above the cell.
Blue-colored cells are right and below the cell.


Return the matrix answer.

 

Example 1:

Input: grid = [[1,2,3],[3,1,5],[3,2,1]]

Output: Output: [[1,1,0],[1,0,1],[0,1,1]]

Explanation:

To calculate the answer cells:

answer	left-above elements	leftAbove	right-below elements	rightBelow	|leftAbove - rightBelow|
[0][0]	[]	0	[grid[1][1], grid[2][2]]	|{1, 1}| = 1	1
[0][1]	[]	0	[grid[1][2]]	|{5}| = 1	1
[0][2]	[]	0	[]	0	0
[1][0]	[]	0	[grid[2][1]]	|{2}| = 1	1
[1][1]	[grid[0][0]]	|{1}| = 1	[grid[2][2]]	|{1}| = 1	0
[1][2]	[grid[0][1]]	|{2}| = 1	[]	0	1
[2][0]	[]	0	[]	0	0
[2][1]	[grid[1][0]]	|{3}| = 1	[]	0	1
[2][2]	[grid[0][0], grid[1][1]]	|{1, 1}| = 1	[]	0	1
Example 2:

Input: grid = [[1]]

Output: Output: [[0]]

 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n, grid[i][j] <= 50
 */
#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
 public:
    vector<vector<int>> differenceOfDistinctValues(const vector<vector<int>>& grid) {
      int m = grid.size(), n = grid[0].size();
      vector<vector<int>> res(m, vector<int>(n));
      unordered_set<int> num_set;
      for (int k = 1; k < m + n; k++) {
        int min_j = max(n-k, 0);
        int max_j = min(m+n-1-k, n-1);
        num_set.clear();
        for (int j = min_j; j <= max_j; j++) {
          int i = k+j-n;
          res[i][j] = num_set.size();
          num_set.insert(grid[i][j]);
        }
        num_set.clear();
      for (int j = max_j; j >= min_j; j--) {
        int i = k+j-n;
        res[i][j] = abs(res[i][j] - static_cast<int>(num_set.size()));
        num_set.insert(grid[i][j]);
      }
      }
      return res;
    }
};

int main() {
  Solution sol;
  vector<vector<int>> grid = {{1, 2, 3}, {3, 1, 5}, {3, 2, 1}};
  vector<vector<int>> result = sol.differenceOfDistinctValues(grid);
  
  for (const auto& row : result) {
    for (int val : row) {
      cout << val << " ";
    }
    cout << endl;
  }
  
  return 0;
}