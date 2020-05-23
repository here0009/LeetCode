"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
"""
class Solution_1:
    def isPowerOfFour(self, num: int) -> bool:
        """
        Wrong answer, it could be an integer that is divisible by 4, but not the power of 4
        """
        print(bin(num))
        return bin(num)[-2:] == '00'

        
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        tmp = 1
        while tmp < num:
            tmp = tmp * 4
        return tmp == num

s = Solution_1()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(12))
print(s.isPowerOfFour(2))
print(s.isPowerOfFour(4))
print(s.isPowerOfFour(-2147483648))
print(s.isPowerOfFour(1))
# for i in range(50):
#     print(4**i)