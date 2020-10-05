"""
Given an integer n, you must transform it into 0 using the following operations any number of times:

Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

 

Example 1:

Input: n = 0
Output: 0
Example 2:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.
Example 3:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
Example 4:

Input: n = 9
Output: 14
Example 5:

Input: n = 333
Output: 393
 

Constraints:

0 <= n <= 109
"""


from functools import lru_cache
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        def intToBin(n):
            return list(bin(n)[2:])

        @lru_cache(None)
        def dp(n):
            visited.add(n)
            res = []
            if n == 0:
                return 0
            lst = intToBin(n)
            lst1 = lst[:]
            if lst1[-1] == '0':
                lst1[-1] = '1'
            else:
                lst1[-1] = '0'
            n1 = int(''.join(lst1), 2)
            if n1 not in visited:
                res.append(n1)
            lst2 = lst[:]
            length = len(lst2)
            index = length-1
            while index > 0 and lst2[index] == '0':
                index -= 1
            if index > 0:
                if lst2[index-1] == '0':
                    lst2[index-1] = '1'
                else:
                    lst2[index-1] = '0'
            else:
                lst2 = ['1'] + lst2
            n2 = int(''.join(lst2), 2)
            if n2 not in visited:
                res.append(n2)
            print(n,intToBin(n),res)
            return 1 + min(dp(i) for i in res)

        visited = set()
        print("++++++++++++++++", n)
        return dp(n)
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/877708/PythonC%2B%2B-O(log-n)-with-Prove

# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/discuss/877798/JavaC%2B%2BPython-3-Solutions-with-Prove-O(1)-Space

from functools import lru_cache
from math import log2
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        @lru_cache(None)
        def bto0(b):
            return (1 << b+1) - 1
        @lru_cache(None)
        def nto0(n):
            if n == 0:
                return 0
            b = int(log2(n))
            return bto0(b) - nto0(n - (1<<b))

        return nto0(n)




S = Solution()
n = 0
print(S.minimumOneBitOperations(n))
n = 3
print(S.minimumOneBitOperations(n))
n = 6
print(S.minimumOneBitOperations(n))
n = 9
print(S.minimumOneBitOperations(n))
n = 333
print(S.minimumOneBitOperations(n))