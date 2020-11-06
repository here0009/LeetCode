"""
Given a year Y and a month M, return how many days there are in that month.

 

Example 1:

Input: Y = 1992, M = 7
Output: 31
Example 2:

Input: Y = 2000, M = 2
Output: 29
Example 3:

Input: Y = 1900, M = 2
Output: 28
 

Note:

1583 <= Y <= 2100
1 <= M <= 12

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-days-in-a-month
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[M-1] + (M == 2 and (Y % 400 == 0 or (Y % 4 == 0 and Y % 100 != 0)))

S = Solution()
Y = 1992
M = 7
print(S.numberOfDays(Y, M))
Y = 2000
M = 2
print(S.numberOfDays(Y, M))
Y = 1900
M = 2
print(S.numberOfDays(Y, M))