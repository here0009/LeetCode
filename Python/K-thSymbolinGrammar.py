"""
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row N and index K, return the K-th indexed symbol in row N. (The values of K are 1-indexed.) (1 indexed).

Examples:
Input: N = 1, K = 1
Output: 0

Input: N = 2, K = 1
Output: 0

Input: N = 2, K = 2
Output: 1

Input: N = 4, K = 5
Output: 1

Explanation:
row 1: 0
row 2: 01
row 3: 0110
row 4: 01101001
Note:

N will be an integer in the range [1, 30].
K will be an integer in the range [1, 2^(N-1)].
"""
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # print(N,K)
        if N == 1 and K == 1:
            return 0
        else:
            if K%2 == 1: #same as ancestor
                return self.kthGrammar(N-1, (K-1)//2+1)
            else: #diff as ancestor
                return 1-self.kthGrammar(N-1, (K-1)//2+1)



s = Solution()
N = 1
K = 1
print(s.kthGrammar(N,K))
N = 2
K = 1
print(s.kthGrammar(N,K))
N = 2
K = 2
print(s.kthGrammar(N,K))
N = 4
K = 5
print(s.kthGrammar(N,K))
N = 3
K = 4
print(s.kthGrammar(N,K))