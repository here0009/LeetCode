"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""
from collections import defaultdict
from collections import Counter
class Solution:
    def numOfWays(self, n: int) -> int:
        M = 10**9+7
        comb = set()
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j!= k:
                        comb.add((i,j,k))
        # print(comb)
        # print(len(comb))
        next_row_dict = defaultdict(list)
        for i1,j1,k1 in comb:
            for i2,j2,k2 in comb:
                if i1 != i2 and j1 != j2 and k1 != k2:
                    next_row_dict[(i1,j1,k1)].append((i2,j2,k2))

        curr_dict = Counter(comb)
        # res = 0
        for key,val in next_row_dict.items():
            print(key, len(val),val)
        #     res += len(val)
        # print(res)
        # next_dict = Counter(comb)
        # print(next_dict)
        while n > 1:
            next_dict = Counter()
            for key,val in curr_dict.items():
                for nex_key in next_row_dict[key]:
                    next_dict[nex_key] += val
            curr_dict = next_dict
            n -= 1
        
        return sum(curr_dict.values()) % M

class Solution:
    def numOfWays(self, n: int) -> int:
        """
        two types of combination aba and abc, the next row of aba could be 3 kind of aba or 2 kind of abc. the next row of abc could be 2 kind of aba or 2 kind of abc
        for the 1st row, there are 6 aba and 6 abc
        """
        M = 10**9+7
        aba,abc = 6,6
        while n > 1:
            aba, abc = 3*aba+2*abc, 2*aba+2*abc
            n -= 1
        return (aba + abc) % M
        


S = Solution()
vals = [1,2,3,7,5000]
for n in vals:
    print(n, S.numOfWays(n))
