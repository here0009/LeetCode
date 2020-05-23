"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4
"""
import sys
class Solution_1:
    def countVowelPermutation(self, n: int) -> int:

        sys.setrecursionlimit(100000)
        def countVstring(s,n):
            if n == 0:
                return 1
            if (s,n) in memo:
                return memo[(s,n)]
            else:
                if s == 'a':
                    res = countVstring('e',n-1)
                elif s == 'e':
                    res =  countVstring('a',n-1) + countVstring('i',n-1)
                elif s == 'i':
                    res =  countVstring('a',n-1) + countVstring('e',n-1) + countVstring('o',n-1) + countVstring('u',n-1)
                elif s == 'o':
                    res =  countVstring('i',n-1) + countVstring('u',n-1)
                elif s == 'u':
                    res =  countVstring('a',n-1)
                memo[(s,n)] = res % M
                return res % M
 
        res = 0
        M = 10**9 + 7
        memo = dict()
        for s in 'aeiou':
            res += countVstring(s,n-1)
        return res % M


class Solution_2:
    """
    bottom up, more simple
    a = u+i+e
    e = a+i
    i = e+o
    o = i
    u = o+i
    """
    def countVowelPermutation(self, n: int) -> int:
        M = 10**9 + 7
        a,e,i,o,u = 1,1,1,1,1
        
        for _ in range(n-1):
            a,e,i,o,u = u+i+e, a+i, e+o, i, o+i
            # print(a,e,i,o,u)
        res = sum([a,e,i,o,u]) % M
        return res

import numpy as np
class Solution:
    """
    matrix multiplication, do not understand this solution
    url:
    https://leetcode.com/problems/count-vowels-permutation/discuss/398224/easy-peasy-python-O(logN)-matrix-rank
    """
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        counts = np.array([1, 1, 1, 1, 1])
        m = np.array([[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0]])
        power = n - 1
        while power:
            power, odd = divmod(power, 2)
            if odd:
                counts = m @ counts % mod
            m = m @ m % mod
        return sum(counts) % mod


s = Solution()
n = 1
print(s.countVowelPermutation(n))

n= 2
print(s.countVowelPermutation(n))

n= 5
print(s.countVowelPermutation(n))

n = 144
print(s.countVowelPermutation(n))

n = 30000
print(s.countVowelPermutation(n))