"""
You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n with value 1.

Let odd denote the number of odd indices in the binary representation of n with value 1.

Note that bits are indexed from right to left in the binary representation of a number.

Return the array [even, odd].



Example 1:

Input: n = 50

Output: [1,2]

Explanation:

The binary representation of 50 is 110010.

It contains 1 on indices 1, 4, and 5.

Example 2:

Input: n = 2

Output: [0,1]

Explanation:

The binary representation of 2 is 10.

It contains 1 only on index 1.
"""

class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        rev_bin_str = bin(n)[2:][::-1]
        even_count = sum([1 for i in range(0, len(rev_bin_str), 2) if rev_bin_str[i] == '1'])
        odd_count = sum([1 for i in range(1, len(rev_bin_str), 2) if rev_bin_str[i] == '1'])
        return even_count, odd_count