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
    def superpalindromesInRange(self, L: str, R: str) -> int:
        def genPalinrome(d):
            half_d = d //2
            if d == 1:
                for num in range(1,10):
                    yield num
            elif d % 2 == 0:
                for num in range(10**(half_d-1), 10**(half_d)):
                    yield int(str(num) + str(num)[::-1])
            else:
                for num in range(10**(half_d-1), 10**(half_d)):
                    for j in range(10):
                        yield int(str(num) + str(j) + str(num)[::-1])

        L, R = int(L), int(R)
        sqrt_L, sqrt_R = int(sqrt(L)), int(sqrt(R)+1)
        res = 0
        dl = len(str(sqrt_L))
        dr = len(str(sqrt_R)) + 1
        # print(sqrt_L, sqrt_R, dl, dr)
        for d in range(dl, dr):
            for num in genPalinrome(d):
                # print(d, num)
                num2 = num**2
                if num2 >= L and num2 <= R:
                    str_num2 = str(num2)
                    if str_num2 == str_num2[::-1]:
                        # print(num, num2)
                        res += 1
        return res


S = Solution()
L = "4"
R = "1000"
print(S.superpalindromesInRange(L, R))
