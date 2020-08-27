"""
Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        """
        TLE
        """
        def genPalinrome(d):
            half_d = d //2
            if d == 1:
                for num in range(10):
                    yield num
            elif d % 2 == 0:
                for num in range(10**(half_d-1), 10**(half_d)):
                    yield int(str(num) + str(num)[::-1])
            else:
                for num in range(10**(half_d-1), 10**(half_d)):
                    for j in range(10):
                        yield int(str(num) + str(j) + str(num)[::-1])
        
        length = len(n)
        dl, dr = length-1, length+1
        int_n = int(n)
        if length == 1:
            dl, dr = 1, 2
        min_diff = float('inf')
        # print(dl, dr)
        res = None
        for d in range(dl, dr+1):
            for num in genPalinrome(d):
                tmp = num - int_n
                # print(num, tmp)
                if tmp < 0:
                    if min_diff > abs(tmp):
                        min_diff = abs(tmp)
                        res = num
                elif tmp > 0: # tmp > 0
                    # print(num, res, tmp, min_diff)
                    return str(num) if tmp < min_diff else str(res)


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        int_n = int(n)
        if length == 1:
            return str(int_n - 1)
        half_len, rmd = divmod(length, 2)
        half = int(n[:half_len])
        if n == n[::-1]:
            if rmd == 1:
                mid = int(n[half_len])
                if mid > 0:
                    mid -= 1
                else:
                    mid += 1
                return str(half) + str(mid) + str(half)[::-1]
            else:
                half -= 1
                return str(half) + str(half)[::-1]
        else:
            # print(half,rmd)
            diff = float('inf')
            res = 0
            if rmd == 1:
                for i in range(-1,2,1):
                    for j in range(10):
                        tmp = half+i
                        num = str(tmp) + str(j) + str(tmp)[::-1]
                        # print(num)
                        tmp_diff = abs(int(num) - int_n)
                        if tmp_diff < diff:
                            diff = tmp_diff
                            res = num
            else:
                for i in range(-1,2,1):
                    tmp = half+i
                    if str(tmp)[-1] == '9':
                        num = str(tmp) + '9' + str(tmp)[::-1]
                    else:
                        num = str(tmp) + str(tmp)[::-1]
                    print(num)
                    tmp_diff = abs(int(num) - int_n)
                    if tmp_diff < diff:
                        diff = tmp_diff
                        res = num
            return res


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        int_n = int(n)
        if length == 1:
            return str(int_n-1)
        half_len, rmd = divmod(length, 2)
        candidates = ['9'*(length-1), '1'+'0'*(length-1)+'1']
        half_n = int(n[:half_len+rmd])
        for i in range(-1,2,1):
            tmp = half_n+i
            if rmd:
                candidates.append(str(tmp)+str(tmp)[-2::-1])
            else:
                candidates.append(str(tmp)+str(tmp)[::-1])
        # print(candidates)
        diff, res = float('inf'), float('inf')
        candidates = map(int, candidates)
        for num in candidates:
            tmp_diff = abs(int(num) - int_n)
            if tmp_diff == 0:
                continue
            if tmp_diff < diff:
                res = num
                diff = tmp_diff
            elif tmp_diff == diff and num < res:
                res = num
        return str(res)
        
# https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation
class Solution:
    def nearestPalindromic(self, S):
        print(S)
        K = len(S)
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
        prefix = S[:(K+1)//2]
        P = int(prefix)
        for start in map(str, (P-1, P, P+1)):
            candidates.append(start + (start[:-1] if K%2 else start)[::-1])
        print(candidates)
        def delta(x):
            return abs(int(S) - int(x))
        
        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans
S = Solution()
n = '5'
print(n, S.nearestPalindromic(n))
n = "101"
print(n, S.nearestPalindromic(n))
n = "123"
print(n, S.nearestPalindromic(n))
# for i in range(1,101):
#     print(str(i), S.nearestPalindromic(str(i)))
n = "1000"
print(n, S.nearestPalindromic(n))
n = "807045053224792883"
print(n, S.nearestPalindromic(n))
n = "9999"
print(n, S.nearestPalindromic(n))