"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2**31,  2**31 − 1].
"""
class Solution_1:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        ugly_facor_set = {2,3,5}
        for ugly_facor in ugly_facor_set:
            while num % ugly_facor == 0:
                num = num / ugly_facor
        if num != 1:
            return False
        else:
            return True






counts = 0
s = Solution_1()
for i in range(100):
    if s.isUgly(i):
        counts += 1
        print(counts, i)
