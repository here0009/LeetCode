"""
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

 

Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 

Note:

1 <= N <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/armstrong-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isArmstrong(self, N: int) -> bool:
        digits = list(map(int, str(N)))
        k = len(digits)
        return N == sum(i**k for i in digits)

S = Solution()
print(S.isArmstrong(153))
print(S.isArmstrong(123))