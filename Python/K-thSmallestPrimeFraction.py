"""
A sorted list A contains 1, plus some number of primes.  Then, for every p < q in the list, we consider the fraction p/q.

What is the K-th smallest fraction considered?  Return your answer as an array of ints, where answer[0] = p and answer[1] = q.

Examples:
Input: A = [1, 2, 3, 5], K = 3
Output: [2, 5]
Explanation:
The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
The third fraction is 2/5.

Input: A = [1, 7], K = 1
Output: [1, 7]
Note:

A will have length between 2 and 2000.
Each A[i] will be between 1 and 30000.
K will be between 1 and A.length * (A.length - 1) / 2.
"""
import heapq
class Solution:
    def kthSmallestPrimeFraction(self, A, K: int):
        
        p,q = 0,len(A)-1
        hp = [(A[p]/A[q], p,q)]
        counts = 0
        visited = set((p,q))
        while counts < K:
            _, p, q = heapq.heappop(hp)
            counts += 1
            if q-p > 1:
                if (p,q-1) not in visited:
                    heapq.heappush(hp,(A[p]/A[q-1],p,q-1))
                    visited.add((p,q-1))
                if (p+1, q) not  in visited:
                    heapq.heappush(hp,(A[p+1]/A[q],p+1,q))
                    visited.add((p+1,q))
        return [A[p],A[q]]



import heapq
class Solution:
    def kthSmallestPrimeFraction(self, A, K: int):
        # def push(i,j):
        #     if i < j 

        len_A = len(A)
        p,q = 0, len_A-1
        hp = [(A[p]/A[q], p,q)]
        counts = 0
        while counts < K:
            _, p, q = heapq.heappop(hp)
            # print('{},{}/{}'.format(A[p]/A[q],A[p],A[q]))
            # print(hp)
            counts += 1
            if q-p>1:
                heapq.heappush(hp,(A[p+1]/A[q], p+1, q))
                if p == 0:
                    heapq.heappush(hp,(A[p]/A[q-1], p, q-1))
        return [A[p],A[q]]


"""
binary search
"""
class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        n = len(A)
        l,r = 0, 1
        while l <= r:
            mid = (l+r)/2
            total, maxi, j = 0, 0, 1
            for i in range(n-1):
                while j < n and A[i]/mid > A[j]: 
                    j+= 1
                if j == n: 
                    break
                total += n - j 
                if A[i]/A[j] > maxi:
                    p, q, maxi = A[i], A[j], A[i]/A[j]
            if total == K: 
                return [p,q]
            elif total < K: 
                l = mid
            else: 
                r = mid
        return []
"""
for each row i, all the numbers (call them A[j]) to the right of A[i]/m, are the ones such that A[i]/A[j] will be smaller than m.
sum them up so that you will know the total number of pairs A[i]/A[j] that are smaller than m. Find a proper m such that the total number equals K, and then you find the maximum A[i]/A[j] among all pairs that are smaller than A[i]/m, which is the Kth smallest number.
"""
from bisect import bisect_right
class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        lo,hi,N = 0,1,len(A)
        while True:
            mid = (lo+hi)/2
            borders = [bisect_right(A,A[i]/mid) for i in range(N)]
            counts = N*N - sum(borders)
            if counts > K:
                hi = mid
            elif counts < K:
                lo = mid
            else:
                return max([(A[i],A[v]) for i,v in enumerate(borders) if v < N], key = lambda x:x[0]/x[1]) #v is N that means for all the i,



class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        """
        there should be a value between 0 and 1 (m)
        """
        lo, hi = 0, 1
        n = len(A)
        while lo <= hi:
            mid = (lo + hi)/2
            total,max_v,j = 0,0,1
            for i in range(n-1):
                while j < n and A[i]/A[j] > mid: #A[i]/A[j] > mid so A[i+1]/A[j] also > mid
                    j += 1
                if j == n: #A[i]/A[n-1] > mid so A[i+1]/A[n-1] also > mid
                    break 
                total += n-j #count the rest nums A[i]/A[j] <= mid
                if A[i]/A[j] > max_v:
                    p,q,max_v = i,j,A[i]/A[j]
                
            if total == K:
                return [A[p], A[q]]
            elif total < K:
                lo = mid #should increas mid, so other values could be included in
            else:
                hi = mid
        return []
                    

S = Solution()
A = [1, 2, 3, 5]
K = 3
print(S.kthSmallestPrimeFraction(A,K))

A = [1, 7]
K = 1
print(S.kthSmallestPrimeFraction(A,K))            

A = [1,7,23,29,47]
K = 8
print(S.kthSmallestPrimeFraction(A,K))
# Output
# [7,23]
# Expected
# [23,47]