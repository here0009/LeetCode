"""
Let's say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].

 

Example 1:

Input: L = "4", R = "1000"
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
 

Note:

1 <= len(L) <= 18
1 <= len(R) <= 18
L and R are strings representing integers in the range [1, 10^18).
int(L) <= int(R)
"""
from math import sqrt
class Solution:
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        sqrt_L = int(sqrt(L))
        sqrt_R = int(sqrt(R))
        res = 0
        res_list = []
        for i in range(sqrt_L,sqrt_R):
            if self.isPalindrome(str(i)) and self.isPalindrome(str(i**2)):
                res_list.append(i)
                res+=1
        print(res_list)
        return res
        
    def isPalindrome(self, string):
        """
        test if a string is palindrome
        """
        if len(string) == 1:
            return True
        if len(string) == 2:
            if string[0] != string[-1]:
                return False
            else:
                return True
        if string[0] != string[-1]:
            return False
        return self.isPalindrome(string[1:-1])


s = Solution()
# for i in range(1,10000):
#     if s.isPalindrome(str(i)):
#         print(i)
print(s.superpalindromesInRange(1000000,10000000))