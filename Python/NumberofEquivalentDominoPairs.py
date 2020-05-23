"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""
class Solution:
    def numEquivDominoPairs(self, dominoes) -> int:
        counts = dict()
        for i,j in dominoes:
            if i <= j:
                counts[(i,j)] = counts.get((i,j),0) + 1
            else:
                counts[(j,i)] = counts.get((j,i),0) + 1

        # print(counts)
        res = 0
        for v in counts.values():
            if v > 1:
                res += v*(v-1)//2
        return res

s = Solution()
dominoes = [[1,2],[2,1],[3,4],[5,6]]
print(s.numEquivDominoPairs(dominoes))

dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(s.numEquivDominoPairs(dominoes))