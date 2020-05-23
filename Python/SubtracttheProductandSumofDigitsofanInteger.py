"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)
        list_n = [int(i) for i in str_n]
        p = 1
        s = 0
        # print(list_n)
        for k in list_n:
            p *= k
            s += k
        return p - s

S = Solution()
n = 234
print(S.subtractProductAndSum(n))
n = 4421
print(S.subtractProductAndSum(n))