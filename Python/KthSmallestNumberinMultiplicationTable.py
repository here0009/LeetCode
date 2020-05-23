"""
Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?

Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 
Explanation: 
The Multiplication Table:
1   2   3
2   4   6
3   6   9

The 5-th smallest number is 3 (1, 2, 2, 3, 3).
Example 2:
Input: m = 2, n = 3, k = 6
Output: 
Explanation: 
The Multiplication Table:
1   2   3
2   4   6

The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
Note:
The m and n will be in the range [1, 30000].
The k will be in the range [1, m * n]
"""
import heapq
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
        TLE
        """
        def push(i,j):
            if i>= 0 and i<=m and j>=0 and j<=n:
                heapq.heappush(nums,(i*j,i,j))

        nums = [(1,1,1)] #(i*j,i,j)
        counts = 0
        while nums and counts < k:
            # print(nums)
            num,i,j = heapq.heappop(nums)
            counts += 1
            if counts == k:
                return num
            push(i,j+1)
            if j == 1:
                push(i+1,j)
        return None

from bisect import bisect
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m*n
        while lo < hi:
            mid = (lo+hi)//2 #the counts of the num <= mid in table is k
            counts, j,max_v = 0,n,0
            for i in range(1,m+1):
                while j > 0 and i*j > mid:
                    j -= 1
                counts += j
                if j == 0:
                    break
            if counts >= k:
                hi = mid
            else:
                lo = mid+1
        return lo
                

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo,hi = 1,m*n
        while lo < hi:
            mid = (lo + hi)//2
            counts = sum(min(n, mid//i) for i in range(1,m+1)) #the sum of nums smaller than mid in each row
            if counts < k:
                lo = mid+1
            else:
                hi = mid
        return lo


S = Solution()
m = 3
n = 3
k = 5
print(S.findKthNumber(m,n,k))

m = 2
n = 3
k = 6
print(S.findKthNumber(m,n,k))

m = 9895
n = 28405
k = 100787757
print(S.findKthNumber(m,n,k))
