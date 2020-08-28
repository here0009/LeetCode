"""
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation: 
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
Note: 1 <= n <= 109
"""

# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/discuss/103755/python-dp-solution-easily-understood
class Solution:
    def findIntegers(self, num: int) -> int:
        A = bin(num)[2:][::-1]
        # print(A)
        dp = [[1,1] for _ in range(len(A))]
        if A[0] == '0':
            res = 1
        else:
            res = 2
        for i in range(1, len(A)):
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
            dp[i][1] = dp[i-1][0]
            if A[i-1:i+1] == '01':
                res += dp[i][0]
            elif A[i-1:i+1] == '11':
                res = dp[i][0] + dp[i][1]
        # print(dp)
        return res

S = Solution()
print(S.findIntegers(5))
for i in range(11):
    print("++++++++++++++++")
    print(i)
    print(S.findIntegers(i))