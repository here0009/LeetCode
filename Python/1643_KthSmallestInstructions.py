"""
Bob is standing at cell (0, 0), and he wants to reach destination: (row, column). He can only travel right and down. You are going to help Bob by providing instructions for him to reach destination.

The instructions are represented as a string, where each character is either:

'H', meaning move horizontally (go right), or
'V', meaning move vertically (go down).
Multiple instructions will lead Bob to destination. For example, if destination is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.

However, Bob is very picky. Bob has a lucky number k, and he wants the kth lexicographically smallest instructions that will lead him to destination. k is 1-indexed.

Given an integer array destination and an integer k, return the kth lexicographically smallest instructions that will take Bob to destination.

 

Example 1:



Input: destination = [2,3], k = 1
Output: "HHHVV"
Explanation: All the instructions that reach (2, 3) in lexicographic order are as follows:
["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
Example 2:



Input: destination = [2,3], k = 2
Output: "HHVHV"
Example 3:



Input: destination = [2,3], k = 3
Output: "HHVVH"
 

Constraints:

destination.length == 2
1 <= row, column <= 15
1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b
"""


from functools import lru_cache
class Solution:
    def kthSmallestPath(self, destination, k: int) -> str:
        def comb(i,j):
            """
            the combinatiion of i 'V' and j 'H', order matters
            """
            m = i+j
            n = min(i,j)
            res = 1
            for k in range(n):
                res *= m-k
            for k in range(n):
                res = res//(k+1)
            # print(i, j, res)
            return res

        @lru_cache(None)
        def dp(v, h, counts):
            # print('v,h, counts', v, h, counts)
            if counts == 1 or h == 0 or v == 0:
                return h*'H' + v*'V'
            h_counts = comb(v, h-1)
            if counts <= h_counts:
                return 'H' + dp(v, h-1, counts)
            else:
                return 'V' + dp(v-1, h, counts - h_counts)

        v, h = destination
        return dp(v, h, k)


from functools import lru_cache
class Solution:
    def kthSmallestPath(self, destination, k: int) -> str:
        @lru_cache(None)
        def comb(i,j):
            """
            the combinatiion of i 'V' and j 'H', order matters
            """
            if i == 0 and j == 0:
                return 0
            if i == 0 or j == 0:
                return 1
            return comb(i-1, j) + comb(i, j-1)

        
        def dp(v, h, counts):
            if counts == 1 or h == 0 or v == 0:
                return h*'H' + v*'V'
            h_counts = comb(v, h-1)
            if counts <= h_counts:
                return 'H' + dp(v, h-1, counts)
            else:
                return 'V' + dp(v-1, h, counts - h_counts)

        v, h = destination
        return dp(v, h, k)

# 作者：seam
# 链接：https://leetcode-cn.com/problems/kth-smallest-instructions/solution/di-ktiao-zui-xiao-zhi-ling-er-fen-cha-zhao-by-se-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        V, H=destination
        
        ans=''
        while k>0 and H>0 and V>0:
            mid=math.comb(H+V-1, V)
            if mid>=k:
                ans+='H'
                H-=1
            else:
                ans+='V'
                k-=mid
                V-=1
        
        return ans+'H'*H+'V'*V


S = Solution()
for i in range(1, 4):
    print('res',i, S.kthSmallestPath([2,3], i))

destination = [2,2]
k = 5
print(S.kthSmallestPath(destination, k))
# 输出：
# "VVHH"
# 预期结果：
# "VHVH"