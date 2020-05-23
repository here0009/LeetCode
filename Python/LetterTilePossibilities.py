"""
You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
class Solution_1:
    def numTilePossibilities(self, tiles: str) -> int:
        len_t = len(tiles)
        tiles = tiles * 2
        res = set()
        for length in range(1,len_t+1):
            for start in range(len_t):
                if tiles[start:start+length] not in res:
                    res.add(tiles[start:start+length])
        print(res)
        return len(res)

from itertools import permutations
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = 0
        for i in range(1, len(tiles)+1):
            res += len(set(permutations(tiles,i)))
        return res


s = Solution()
tiles = "AAB"
print(s.numTilePossibilities(tiles))
tiles = "AAABBC"
print(s.numTilePossibilities(tiles))
