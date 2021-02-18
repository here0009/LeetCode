"""
On an infinite number line, the position of the i-th stone is given by stones[i].  Call a stone an endpoint stone if it has the smallest or largest position.

Each turn, you pick up an endpoint stone and move it to an unoccupied position so that it is no longer an endpoint stone.

In particular, if the stones are at say, stones = [1,2,5], you cannot move the endpoint stone at position 5, since moving it to any position (such as 0, or 3) will still keep that stone as an endpoint stone.

The game ends when you cannot make any more moves, ie. the stones are in consecutive positions.

When the game ends, what is the minimum and maximum number of moves that you could have made?  Return the answer as an length 2 array: answer = [minimum_moves, maximum_moves]

 

Example 1:

Input: [7,4,9]
Output: [1,2]
Explanation: 
We can move 4 -> 8 for one move to finish the game.
Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
Example 2:

Input: [6,5,4,3,10]
Output: [2,3]
We can move 3 -> 8 then 10 -> 7 to finish the game.
Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
Notice we cannot move 10 -> 2 to finish the game, because that would be an illegal move.
Example 3:

Input: [100,101,104,102,103]
Output: [0,0]
 

Note:

3 <= stones.length <= 10^4
1 <= stones[i] <= 10^9
stones[i] have distinct values.
"""
"""
Thoughts:
min moves: fill the smaller gaps first
max moves: fill the larger gaps first
"""


class Solution:
    def numMovesStonesII(self, stones):
        """
        sort the stones, and fill the gap between stones
        if we want to take more moves, we try our best to keep the gap. so every gap can be used
        if equals to the gaps in the sorted list
        if we want to take less moves, we will try to eliminated the gap as fast as possible
        just consider the final status, find the largest cluster and extend it
        wrong answer, can only move stones from the end to non-end
        """
        stones.sort()
        gap_counts = 0
        max_cluster = 0
        cluster = 0
        for i in range(1, len(stones)):
            gap = stones[i] - stones[i - 1]
            if gap > 1:
                gap_counts += gap - 1
            if gap == 1:
                cluster += 1
                max_cluster = max(max_cluster, cluster)
            else:
                cluster = 0
        return [len(stones) - max_cluster, gap_counts]


# https://leetcode.com/problems/moving-stones-until-consecutive-ii/discuss/289357/c%2B%2B-with-picture
class Solution:
    def numMovesStonesII(self, stones):
        """
        sort stones 1st
        max move: use gap as possible as we can: the 1st gap or the last gap can not be used because we remvoe end stones 1st, other gap can all be used if we move the stone from this end to that end
        s.....s....ss..........ss....s
        so the max moves is max(stones[n-1] - stones[1] - (n - 2), stones[n-2] - stones[0] - (n -2))
        for the min move, think of size slide along the stones, find the min stones need to be moved
        """
        stones.sort()
        n = len(stones)
        max_moves = max(stones[n - 1] - stones[1] - (n - 2), stones[n - 2] - stones[0] - (n -2))
        i = 0
        min_moves = n
        for j in range(n):
            while stones[j] - stones[i] >= n:  # can not form a window of size n - 1
                i += 1
            if stones[j] - stones[i] == n - 2 and j - i == n - 2:  # a continous stone of size n - 1, we can not move the end directly, because then it will also be an end. we have to form a gap 1st, then move then end, 2 moves
                min_moves = min(min_moves, 2)
            else:
                min_moves = min(min_moves, n - (j - i + 1))
        return [min_moves, max_moves]

S = Solution()
stones = [7,4,9]
print(S.numMovesStonesII(stones))

stones = [6,5,4,3,10]
print(S.numMovesStonesII(stones))

stones = [100,101,104,102,103]
print(S.numMovesStonesII(stones))
