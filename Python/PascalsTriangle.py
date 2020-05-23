"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(numRows-1):
            pre = res[-1]
            curr = [1]
            for i in range(1,len(pre)):
                curr.append(pre[i-1]+pre[i])
            curr.append(1)
            res.append(curr)
            pre = curr
        return res

s = Solution()
print(s.generate(5))
print(s.generate(0))
for index,l in enumerate(s.generate(10)):
    print((9-index)*2*' ',l)