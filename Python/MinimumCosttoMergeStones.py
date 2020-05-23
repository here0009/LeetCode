"""
There are N piles of stones arranged in a row.  The i-th pile has stones[i] stones.

A move consists of merging exactly K consecutive piles into one pile, and the cost of this move is equal to the total number of stones in these K piles.

Find the minimum cost to merge all piles of stones into one pile.  If it is impossible, return -1.

 

Example 1:

Input: stones = [3,2,4,1], K = 2
Output: 20
Explanation: 
We start with [3, 2, 4, 1].
We merge [3, 2] for a cost of 5, and we are left with [5, 4, 1].
We merge [4, 1] for a cost of 5, and we are left with [5, 5].
We merge [5, 5] for a cost of 10, and we are left with [10].
The total cost was 20, and this is the minimum possible.
Example 2:

Input: stones = [3,2,4,1], K = 3
Output: -1
Explanation: After any merge operation, there are 2 piles left, and we can't merge anymore.  So the task is impossible.
Example 3:

Input: stones = [3,5,1,2,6], K = 3
Output: 25
Explanation: 
We start with [3, 5, 1, 2, 6].
We merge [5, 1, 2] for a cost of 8, and we are left with [3, 8, 6].
We merge [3, 8, 6] for a cost of 17, and we are left with [17].
The total cost was 25, and this is the minimum possible.
 

Note:

1 <= stones.length <= 30
2 <= K <= 30
1 <= stones[i] <= 100
"""

class Solution:
    def mergeStones(self, stones, K: int) -> int:
        """
        Thoughts: the total merge value is equal to sum(stones), so we need to find the minimum stones[i:i+k] then merge it.
        wrong answer for the test case [6,4,4,6], you should merege [6,4,4,6] => [10,10] => [20]
        """
        length = len(stones)
        if (length-K) % (K-1) != 0:
            return -1
        res = 0
        while len(stones) > 1:
            print(stones)
            min_K, min_K_index = sum(stones[:K]), 0
            total = min_K
            n = len(stones)
            for i in range(n-K):
                total -= stones[i]
                total += stones[i+K]
                # print(total, min_K)
                if total < min_K:
                    min_K = total
                    min_K_index = i+1
                # print(total, min_K,min_K_index,i+1)
            stones = stones[:min_K_index] + [min_K] + stones[min_K_index+K:]
            res += min_K
        print(stones)
        return res

from functools import lru_cache
class Solution:
    def mergeStones(self, stones, K: int) -> int:
        print(stones)
        length = len(stones)
        if (length-K) % (K-1) != 0:
            return -1

        @lru_cache(None)
        def dp(start, end):
            print(start, end)
            if start == end:
                return 0
            if end - start == K:
                return sum(stones[start:end])

            path = (start, start+K)
            for i in range(1,K):
                if start+i > end-i:
                    break
                tmp = sum(stones[start:start+i])+dp(start+i,end-i)+sum(stones[end-(K-i):end])
                if tmp < res:
                    res = tmp

            self.path.append(path)
            return res


        self.res = 0
        dp(0,length)
        print(self.path)
        return self.res



# class Solution:       
#     def mergeStones(self, stones, K: int) -> int:
#         def recursive(i, j, piles):
#             if i == j and piles == 1:
#                 return 0
#             if (j - i + 1 - piles) % (K - 1) != 0: 
#                 return float('inf')  # means impossible
#             if (i, j, piles) in dp:
#                 return dp[(i, j, piles)]
#             if piles == 1:
#                 dp[(i,j,piles)] = recursive(i, j, K) + pre_sum[j+1] - pre_sum[i]
#                 return dp[(i,j,piles)]
#             else:
#                 min_cost = float('inf')
#                 for k in range(i, j, K - 1):
#                     min_cost = min(min_cost, recursive(i, k, 1) + recursive(k + 1, j, piles - 1))
#                 dp[(i, j, piles)] = min_cost
#                 return dp[(i, j, piles)]
        
#         n = len(stones)
#         if (n - 1) % (K - 1) != 0:
#             return -1
#         pre_sum = [0] * (n + 1)
#         for i in range(n):
#             pre_sum[i + 1] = pre_sum[i] + stones[i]
#         dp = {}
#         return recursive(0, n - 1, 1)        


from functools import lru_cache
class Solution:       
    def mergeStones(self, stones, K: int) -> int:

        @lru_cache(None)
        def recursive(i, j, piles):
            print(i,j,piles)
            if i == j and piles == 1:
                return 0
            if (j - i + 1 - piles) % (K - 1) != 0: 
                return float('inf')  # means impossible
            if piles == 1:
                return recursive(i, j, K) + pre_sum[j+1] - pre_sum[i]
            else:
                min_cost = float('inf')
                for k in range(i, j, K - 1):
                    min_cost = min(min_cost, recursive(i, k, 1) + recursive(k + 1, j, piles - 1))
                return min_cost
        
        n = len(stones)
        if (n - 1) % (K - 1) != 0:
            return -1
        pre_sum = [0] * (n + 1)
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + stones[i]
        dp = {}
        return recursive(0, n - 1, 1)    

from functools import lru_cache
class Solution: 
    def mergeStones(self, stones, K):
        """
        wrong answer
        """
        n = len(stones)
        if (n - 1) % (K - 1): return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        import functools
        @functools.lru_cache(None)
        def dp(i, j):
            if j - i  < K: 
                return 0
            res = dp(i,i+1)+dp(i+1,j)
            if i+K < j:
                res = min(res,min(dp(i, mid) + dp(mid, j) for mid in range(i+K, j, K)))
            # res = min(res1,res2)
            if (j - i) % (K-1) == 0:
                res += prefix[j] - prefix[i]
            return res
        return dp(0, n)

from functools import lru_cache
class Solution:
    def mergeStones(self, stones, K: int) -> int:
        @lru_cache(None)
        def dp(i, j):
            if j - i + 1 < K: 
                return 0
            res = min(dp(i, mid) + dp(mid+1, j) for mid in range(i, j,K-1) )
            if (j - i) % (K - 1) == 0:
                res += prefix[j + 1] - prefix[i]
            return res

        n = len(stones)
        if (n - 1) % (K - 1): 
            return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        return dp(0, n-1)


from functools import lru_cache
class Solution:
    def mergeStones(self, stones, K: int) -> int:
        @lru_cache(None)
        def dp(i, j, m):
            if (j-i+1-m) % (K-1):
                return float('inf')
            if i == j:
                return 0 if m == 1 else float('inf')
            if m == 1:
                return dp(i,j,K) + prefix[j+1]-prefix[i]
            return min(dp(i,mid,1)+dp(mid+1,j,m-1) for mid in range(i,j,K-1))


        n = len(stones)
        if (n - 1) % (K - 1): 
            return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        return dp(0, n-1,1)


S = Solution()
stones = [3,2,4,1]
K = 2
print(S.mergeStones(stones,K))
stones = [3,2,4,1]
K = 3
print(S.mergeStones(stones,K))
stones = [3,5,1,2,6]
K = 3
print(S.mergeStones(stones,K))

stones =[6,4,4,6]
K = 2
print(S.mergeStones(stones,K))
