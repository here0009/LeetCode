"""
For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format.

Example 1:

Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.
 

Example 2:

Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
 

Example 3:

Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
"""
class Solution:
    """
    time limits exceeds
    """

    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for i in range(1,n+1):
            tmp_n, base = n, i
            break_flag = False
            while tmp_n != 0:
                tmp_n, rmd = divmod(tmp_n,base)
                if rmd != 1:
                    break_flag = True
                    break
            if not break_flag:
                return str(base)

s = Solution()
print(s.smallestGoodBase('13'))
print(s.smallestGoodBase('4681'))
print(s.smallestGoodBase("1000000000000000000"))