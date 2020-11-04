"""
Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...

So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...

Given a positive integer n, you need to return the n-th integer after removing. Note that 1 will be the first integer.

 

Example 1:

Input: n = 9
Output: 10
 

Constraints:

1 <= n <= 8 x 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-9
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def newInteger(self, n: int) -> int:
        """
        calculate counts of nums that <= n and contain 9
        wrong answer
        """
        if n < 10:
            return (n == 9) + n
        str_n = str(n)
        k = int(str_n[0])
        d = len(str_n) - 1
        return int(str(k)+'0'*d) + k*9**(d-1) + ((k == 9) + 1) * self.newInteger(int(str_n[1:]))


class Solution:
    def newInteger(self, n: int) -> int:
        """
        Thoughts: convert n to 9-based num
        """
        res = []
        while n > 0:
            n, rmd = divmod(n, 9)
            res.append(rmd)
        return int(''.join(str(i) for i in res)[::-1])

class Solution:
    def newInteger(self, n: int) -> int:
        """
        Thoughts: convert n to 9-based num
        """
        res,i = 0, 0
        while n > 0:
            n, rmd = divmod(n, 9)
            res += rmd*(10**i)
            i += 1
        return res

S = Solution()
for i in range(100):
    print(i, S.newInteger(i))