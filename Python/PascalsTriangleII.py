"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
class Solution:
    def getRow(self, rowIndex: int):
        res = [1]
        while rowIndex > 0:
            res2 = [1]
            for i in range(1,len(res)):
                res2.append(res[i-1]+res[i])
            res2.append(1)
            res = res2
            rowIndex -= 1
        return res

class Solution:
    def getRow(self, rowIndex: int):
        row = [1]
        for i in range(rowIndex):
            row = [1] + [row[j]+row[j+1] for j in range(len(row)-1)] + [1] 
        return row

class Solution:
    def getRow(self, rowIndex: int):
        dp = [1]*(rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(1,i):
                dp[i-j] += dp[i-j-1]
        return dp
 
S = Solution()
rowIndex = 3
print(S.getRow(rowIndex))
for i in range(10):
    print(S.getRow(i))