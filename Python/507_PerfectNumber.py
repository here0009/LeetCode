"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""

from math import sqrt
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if res == 1:
            return False
        res,i = 1,2
        while i * i <= num:
            if num % i == 0:
                if i != num //i:
                    res += i + num //i
                else:
                    res += i
            i += 1
        return res == num

S = Solution()
num = 28
print(S.checkPerfectNumber(num))
num = 6
print(S.checkPerfectNumber(num))
