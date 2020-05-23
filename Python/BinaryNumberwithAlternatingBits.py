"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101

Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.

Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.

Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
"""
class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bit_string = "{:b}".format(n)
        for i in range(len(bit_string)-1):
            if not int(bit_string[i]) ^ int(bit_string[i+1]):
                return False
        return True

s = Solution()
test = [5,7,11,10]
for i in test:
    print(s.hasAlternatingBits(i))
