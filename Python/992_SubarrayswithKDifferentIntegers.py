"""
Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""


class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int: 
        """
        TLE
        """
        def dp(i,j):
            visited[i][j-1] = 1
            if j - i < K:
                return
            for k in range(i+1, j):
                if not visited[i][k-1]:
                    dp(i,k)
                if not visited[k][j-1]:
                    dp(k,j)
            if len(set(A[i:j])) == K:
                # print(A[i:j], i, j)
                self.res += 1

        length = len(A)
        self.res = 0
        visited = [[0]*length for _ in range(length)]
        dp(0, length)
        return self.res

# https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/523136/JavaC%2B%2BPython-Sliding-Window

from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        def atMostK(nums, k):
            print(nums, k)
            res, left = 0, 0
            counter = Counter()
            for right, v in enumerate(nums):
                if counter[v] == 0:
                    k -= 1
                counter[v] += 1
                while k < 0:
                    counter[A[left]] -= 1
                    if counter[A[left]] == 0:
                        k += 1
                    left += 1
                res += right - left
                # print(counter, res)
            return res
        return atMostK(A, K) - atMostK(A, K-1)


class Solution:
    def subarraysWithKDistinct(self, A, K: int) -> int:
        if K == 0 or len(A) < K:
            return 0
        left, mid, res = 0, 0, 0 # mid to record the index of left most unique element in counter
        counter = dict()
        for v in A:
            counter[v] = counter.get(v, 0) + 1
            if len(counter) == K + 1: # a new elment is added,so replace the last elment of A[mid] 
                counter.pop(A[mid])
                mid += 1
                left = mid
            if len(counter) == K:
                while counter[A[mid]] > 1:
                    counter[A[mid]] -= 1
                    mid += 1
                res += mid - left + 1
        return res



S = Solution()
A = [1,2,1,2,3]
K = 2
print(S.subarraysWithKDistinct(A, K))
A = [1,2,1,3,4]
K = 3
print(S.subarraysWithKDistinct(A, K))
