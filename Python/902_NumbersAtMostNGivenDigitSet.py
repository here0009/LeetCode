"""
We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.  (Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.

 

Example 1:

Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.
 

Note:

D is a subset of digits '1'-'9' in sorted order.
1 <= N <= 10^9
"""


class Solution:
    def atMostNGivenDigitSet(self, D, N: int) -> int:
        def dfs(index, up_limit):
            if index == len_N-1:
                return int(str_N[index] >= up_limit)
            res = 0
            p = len_N - index - 1
            if str_N[index] > up_limit:
                while p > 0:
                    res += len_D**p
                    p -= 1
            for d in D:
                if str_N[index] > d:
                    res += len_D**(len_N-index-1)
                elif str_N[index] == d:
                    res += dfs(index+1, d)
            print(index, up_limit, res)
            return res
        print(D)
        str_N = str(N)
        len_N = len(str_N)
        len_D = len(D)
        return dfs(0, '0')

class Solution:
    def atMostNGivenDigitSet(self, D, N: int) -> int:
        def dfs(index, limit):
            if index == len_N:
                return 1
            res = 0
            print(index, limit, res)
            if limit == False:
                return len_D**(len_N-index-1) + dfs(index+1, False)

            for d in D:
                if str_N[index] > d:
                    res += dfs(index+1, False)
                elif str_N[index] == d:
                    res += dfs(index+1, True)
            
            return res

        str_N = str(N)
        len_N = len(str_N)
        len_D = len(D)
        print(D)
        return dfs(0, False)

# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/168440/My-straightforward-self-explanatory-Python-solution
class Solution:
    def atMostNGivenDigitSet(self, D, N):
        def less(c):
            return len([char for char in D if char < c])
        d, cnt, l = len(D), 0, len(str(N))
        # For numbers which have less digits than N, simply len(D) ** digits_length different numbers can be created
        for i in range(1, l):
            cnt += d ** i
        """
        We should also consider edge cases where previous digits match with related digits in N. 
        In this case, we can make a number with previous digits + (digits less than N[i]) + D ** remaining length
        If current digit, N[i] not in D, we should break because we cannot continue for further edge cases
        """
        for i, c in enumerate(str(N)):
            cnt += less(c) * (d ** (l - i - 1))
            if c not in D: break
            if i == l - 1: cnt += 1
        return cnt

from bisect import bisect_left
class Solution:
    def atMostNGivenDigitSet(self, D, N: int) -> int:
        str_N = str(N)
        d, n = len(D), len(str_N)
        res = sum(d**i for i in range(1, n)) # all the nums can be constructed of digits 1~n-1
        for i, v in enumerate(str_N): 
            index = bisect_left(D, v) #len(digits) in D can be used (less than v)
            res += index*(d**(n-i-1)) #these digits can construct d**(n-i-1) nums
            if v not in D: # no edge cases any more
                break
        else:
            res += 1 #no break so besides the previous nums, there is an addtional num that is i == n-1 and v == D[index] 
        return res


S = Solution()
# D = ["3","5","7"]
# N = 100
# print(S.atMostNGivenDigitSet(D, N))
D = ["1","3","5","7"]
N = 100
print(S.atMostNGivenDigitSet(D, N))
D = ["1","4","9"]
N = 1000000000
print(S.atMostNGivenDigitSet(D, N))
D = ["3","4","8"]
N = 4
print(S.atMostNGivenDigitSet(D, N))
D = ["1","2","3","4","6","7","9"]
N = 333
print(S.atMostNGivenDigitSet(D, N))
D = ["1","2","3","4","5","6","7","8","9"]
N = 152
print(S.atMostNGivenDigitSet(D, N))