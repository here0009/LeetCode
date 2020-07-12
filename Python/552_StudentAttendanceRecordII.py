"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times.
Note: The value of n won't exceed 100,000.
"""


class Solution:
    def checkRecord(self, n: int) -> int:
        """
        wrong answer
        """
        a,l,p,al,ap,ll = 1,1,1,0,0,0
        M = 10**9 + 7
        while n > 1:
            next_a = (l + p + ll) % M
            next_al = a  # there is an a before
            next_ap = a
            next_p = (l + p + ll) % M
            next_l = p
            next_ll = l
            a,l,p,al,ap,ll = next_a, next_l, next_p, next_al, next_ap, next_ll
            n -= 1
            print("a,l,p,al,ap",a,l,p,al,ap,ll)
        return sum([a,l,p,al,ap,ll]) % M

"""
https://leetcode.com/problems/student-attendance-record-ii/discuss/356750/Solution-in-Python-3-(five-lines)-(with-explanation)
"""

class Solution:
    def checkRecord(self, num: int) -> int:
        n, l, ll, a_n, a_l, a_ll = 1, 1, 0, 1, 0, 0
        M = 10**9 + 7
        while num > 1:
            n, l, ll, a_n, a_l, a_ll = sum([n, l, ll]) % M, n, l, sum([n, l, ll, a_n, a_l, a_ll]) % M, a_n, a_l
            num -= 1
        return sum([n, l, ll, a_n, a_l, a_ll]) % M


S = Solution()
n = 2
print(S.checkRecord(n))
n = 3
print(S.checkRecord(n))
# Your input
# 3
# Output
# 15
# Expected
# 19
# Your input
# 10
n = 10
print(S.checkRecord(n))
# Output
# 1076
# Expected
# 3536