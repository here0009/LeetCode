"""
Given an array of integers A, consider all non-empty subsequences of A.

For any sequence S, let the width of S be the difference between the maximum and minimum element of S.

Return the sum of the widths of all subsequences of A. 

As the answer may be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: [2,1,3]
Output: 6
Explanation:
Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= 20000
"""
class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        large_num = 10**9+7
        ans = 0
        if len(A) == 1:
            return ans
        A = sorted(A)
        n = len(A)
        for index, num in enumerate(A):
            ans += ((2**index - 2**(n-1-index))*num)%large_num

        return ans%large_num

# import math
class Solution:
    """
    Wrong answer
    """
    def sumSubseqWidths(self, A) -> int:
        """
        Thoughts using a stack to build peak and vally, in peak, the value is smaller than ajecnt values,
        e.g A = [9,6,7,5,8] contruct the peak in following steps:
        A = [+inif] + [9,6,7,5,8] +[+inf]
        [9]
        [9,6]
        [9,6] +7 , 6 is smaller than both of the ajacent values, pop 6
        [9,7,5]
        [9,7,5] + 8, pop 5
        [9,7] + 8, pop 7
        [9,8]
        """

        res  = 0
        N = 10**9+7
        max_num = 20001
        min_num = 0

        A = [max_num] + A + [max_num]
        peaks = []
        print(A)
        for i,v in enumerate(A):
            while peaks and v > A[peaks[-1]]:
                curr = peaks.pop()
                res += A[curr] * 2**(i-peaks[-1]-2)
                print(peaks,  A[curr], A[curr] * 2**(i-peaks[-1]-2))
                print(res)
            peaks.append(i)


        A[0],A[-1] = min_num, min_num
        valleys = []
        print(A)
        for i,v in enumerate(A):
            while valleys and v < A[valleys[-1]]:
                curr = valleys.pop()
                res -=  A[curr] * 2**(i-valleys[-1]-2)
                print(valleys, A[curr], A[curr] * 2**(i-valleys[-1]-2))
                print(res)
            valleys.append(i)

        return res

class Solution:
    def sumSubseqWidths(self, A) -> int:
        res = 0
        N = 10**9+7
        A = sorted(A)
        n = len(A)
        for i,v in enumerate(A):
            res += v*(2**i-2**(n-1-i)) #there are i number smaller than v, n-1-i number larger than v
        return res % N

class Solution:
    def sumSubseqWidths(self, A) -> int:
        res = 0
        N = 10**9+7
        A = sorted(A)
        n = len(A)
        for i,v in enumerate(A):
            res += v*((1<<i) - (1<<(n-1-i))) #there are i number smaller than v, n-1-i number larger than v
        return res % N


s = Solution()
A = [2,1,3]
print(s.sumSubseqWidths(A))