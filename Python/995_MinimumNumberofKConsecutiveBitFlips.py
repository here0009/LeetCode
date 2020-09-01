"""
In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.  If it is not possible, return -1.

 

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].
Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].
Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]
 

Note:

1 <= A.length <= 30000
1 <= K <= A.length
"""

class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        """
        TLE
        """
        length = len(A)
        target = [1]*length
        res = 0
        index = 0
        while index < length-K+1:
            if A[index] == 0:
                res += 1
                for j in range(index, index+K):
                    A[j] = 1 - A[j]
            index += 1
        return res if A == target else -1

class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        A = [1] + A
        length = len(A)
        bin_A = int(''.join(map(str, A)), 2)
        ones = int('1'*K, 2)
        res = 0
        # print(bin_A, ones)
        while len(bin(bin_A)[2:]) > K:
            # print(bin_A, bin(bin_A))
            if bin_A & 1 == 0:
                res += 1
                bin_A = bin_A ^ ones
            bin_A = bin_A >> 1

        str_A = bin(bin_A)[2:]
        length = len(str_A)
        # print(bin_A, ones, res, length)
        if length == 0 or str_A == '1'*length:
            return res
        else:
            return -1


class Solution:
    def minKBitFlips(self, A, K: int) -> int:
        flipped, res = 0, 0
        length = len(A)
        isFlipped = [0]*length
        for i, v in enumerate(A):
            if i >= K:
                flipped ^= isFlipped[i-K]
            if flipped == v:
                if i + K > length:
                    return -1
                isFlipped[i] = 1
                flipped ^= 1
                res += 1
        return res

S = Solution()
A = [0,1,0]
K = 1
print(S.minKBitFlips(A, K))
A = [1,1,0]
K = 2
print(S.minKBitFlips(A, K))
A = [0,0,0,1,0,1,1,0]
K = 3
print(S.minKBitFlips(A, K))
