"""
A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.

Note:

The number of stones is ≥ 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.
Example 1:

[0,1,3,5,6,8,12,17]

There are a total of 8 stones.
The first stone at the 0th unit, second stone at the 1st unit,
third stone at the 3rd unit, and so on...
The last stone at the 17th unit.

Return true. The frog can jump to the last stone by jumping 
1 unit to the 2nd stone, then 2 units to the 3rd stone, then 
2 units to the 4th stone, then 3 units to the 6th stone, 
4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

[0,1,2,3,4,8,9,11]

Return false. There is no way to jump to the last stone as 
the gap between the 5th and 6th stone is too large.
"""
from bisect import bisect_left
class Solution:
    def canCross(self, stones) -> bool:
        length = len(stones)
        def dfs(index,k):
            if (index,k) not in visited and not self.res:
                visited.add((index,k))
                if index == length-1:
                    self.res = True
                next_index = bisect_left(stones, stones[index]+ k)
                # print(index,k,stones[index],next_index)
                if next_index < length and stones[next_index] == stones[index]+k:
                    for next_k in [k-1,k,k+1]:
                        dfs(next_index, next_k)
        self.res = False
        visited = set()
        dfs(0,1)
        return self.res


from functools import lru_cache
class Solution:
    def canCross(self, stones) -> bool:
        # @lru_cache(None)
        def dfs(pos,k):
            if (pos,k) not in visited and not self.res:
                visited.add((pos,k))
                if pos == target:
                    self.res = True
                next_pos = pos + k
                if next_pos in pos_set:
                    for next_k in [k-1,k,k+1]:
                        dfs(next_pos, next_k)

        length = len(stones)
        target = stones[-1]
        pos_set = set(stones)
        self.res = False
        visited = set()
        dfs(0,1)
        return self.res


from functools import lru_cache
class Solution:
    def canCross(self, stones) -> bool:
        # @lru_cache(None)
        def dfs(pos,k):
            next_pos = pos+k
            if next_pos not in pos_set or (pos,k) in visited:
                return False
            if next_pos == target:
                return True
            visited.add((pos,k))
            return dfs(next_pos,k-1) or dfs(next_pos,k) or dfs(next_pos,k+1)


        target = stones[-1]
        pos_set = set(stones)
        visited = set()
        return dfs(0,1)


class Solution:
    def canCross(self, stones) -> bool:
        if len(stones)==2 and stones[1]!=1:
            return False
            
        st=set(stones)
        mem={}
        def helper(k,stone):
            if (k,stone) in mem:
                return mem[(k,stone)]
            if stone not in st or k==0:
                return False
            if stone==stones[-1]:
                return True
            
            mem[(k,stone)]=helper(k,stone+k) or helper(k-1,stone+(k-1)) or helper(k+1,stone+k+1)
            return mem[(k,stone)]
        return helper(1,1)

S = Solution()
stones = [0,1,3,5,6,8,12,17]
print(S.canCross(stones))

stones = [0,1,2,3,4,8,9,11]
print(S.canCross(stones))

stones = [0,1,3,4,5,7,9,10,12]
print(S.canCross(stones))

stones = [0,2]
print(S.canCross(stones))