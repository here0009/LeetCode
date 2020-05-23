"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            remainder = 0
            while num > 0:
                remainder += num%10
                num = num // 10
            num = remainder
        return num
 

# print(s.addDigits(38))
# print(s.addDigits(0))
# print(s.addDigits(111))
# print(s.addDigits(10))

"""
Thoughts:
From the previous test, we can know that all the possible answer is from 1 to 9, 
if num % 9 == 0, if result is 9. or it will be num % 9.
Sometime, you should try a lot, or think a in a different way to get an intuition.
"""
class Solution_1:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        num = num % 9
        if num != 0:
            return num
        else:
            return 9


s = Solution_1()
for i in range(101):
    print(i, s.addDigits(i))