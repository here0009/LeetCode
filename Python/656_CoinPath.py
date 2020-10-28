"""
Given an array A (index starts at 1) consisting of N integers: A1, A2, ..., AN and an integer B. The integer B denotes that from any place (suppose the index is i) in the array A, you can jump to any one of the place in the array A indexed i+1, i+2, …, i+B if this place can be jumped to. Also, if you step on the index i, you have to pay Ai coins. If Ai is -1, it means you can’t jump to the place indexed i in the array.

Now, you start from the place indexed 1 in the array A, and your aim is to reach the place indexed N using the minimum coins. You need to return the path of indexes (starting from 1 to N) in the array you should take to get to the place indexed N using minimum coins.

If there are multiple paths with the same cost, return the lexicographically smallest such path.

If it's not possible to reach the place indexed N then you need to return an empty array.

Example 1:

Input: [1,2,4,-1,2], 2
Output: [1,3,5]
 

Example 2:

Input: [1,2,4,-1,2], 1
Output: []
 

Note:

Path Pa1, Pa2, ..., Pan is lexicographically smaller than Pb1, Pb2, ..., Pbm, if and only if at the first i where Pai and Pbi differ, Pai < Pbi; when no such i exists, then n < m.
A1 >= 0. A2, ..., AN (if exist) will in the range of [-1, 100].
Length of A is in the range of [1, 1000].
B is in the range of [1, 100].
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def cheapestJump(self, A, B):
        """
        :type A: List[int]
        :type B: int
        :rtype: List[int]
        """
        @lru_cache(None)
        def minpath(index):
            """
            the min cost and path to index
            """
            cost, path = float('inf'), []
            # print(index)
            if A[index] == -1:
                return cost, path
            if index == 0:
                return 0, [1]
            start = max(0, index-B)
            for i in range(start, index):
                pre_cost, pre_path = minpath(i)
                tmp_cost, tmp_path = pre_cost + A[i], pre_path + [index+1]
                if tmp_cost < cost or (tmp_cost == cost and tmp_path < path):
                    cost = tmp_cost
                    path = tmp_path
            # print(index+1, cost, path)
            return cost, path

        cost, path = minpath(len(A)-1)
        return path




class Solution:
    def cheapestJump(self, A, B):
        N = len(A)
        if A[0] == -1 or A[-1] == -1:
            return []
        dp = [(0, [1])]
        for i in range(1, N):
            if A[i] == -1:
                dp.append((float('inf'), []))
                continue
            start = max(0, i-B)
            cost, path = float('inf'), []
            for j in range(start, i):
                pre_cost, pre_path = dp[j]
                tmp_cost, tmp_path = pre_cost + A[i], pre_path + [i+1]
                if tmp_cost < cost or (tmp_cost == cost and tmp_path < path):
                    cost = tmp_cost
                    path = tmp_path
            dp.append((cost, path))
            # print(dp)
        # cost, path = 
        return dp[-1][-1]


class Solution:
    def cheapestJump(self, A, B):
        def minpath(index):
            """
            the min cost and path to index
            """
            if index in cache:
                return cache[index]
            cost, path = float('inf'), []
            if A[index] != -1:
                start = max(0, index-B)
                for i in range(start, index):
                    pre_cost, pre_path = minpath(i)
                    tmp_cost, tmp_path = pre_cost + A[i], pre_path + [index+1]
                    if tmp_cost < cost or (tmp_cost == cost and tmp_path < path):
                        cost = tmp_cost
                        path = tmp_path
            cache[index] = (cost, path)
            return cache[index]

        cache = dict()
        cache[0] = (0, [1])
        cost, path = minpath(len(A)-1)
        return path


S = Solution()
A = [1,2,4,-1,2]
B = 2
print(S.cheapestJump(A, B))
A = [1,2,4,-1,2]
B = 1
print(S.cheapestJump(A, B))

A = [0,-1,0,0,0,0]
B = 3
print(S.cheapestJump(A, B))