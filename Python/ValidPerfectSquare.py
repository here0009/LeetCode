"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""
class Solution_1:
    def isPerfectSquare(self, num: int) -> bool:
        """
        Newton's method
        """
        r = num
        while r*r > num:
            print(r)
            r = (r + num/r) // 2
        return r * r == num

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        the number 1+3+5+...+(2n-1) if perfectsquare
        """
        tmp = 0
        i = 1
        while tmp < num:
            tmp += 2*i-1
            i += 1
        return tmp == num


s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(2147483647))
