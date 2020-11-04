"""
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

 

Example 1:

Input: [-10,-5,0,3,7]
Output: 3
Explanation: 
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.
Example 2:

Input: [0,2,5,8,17]
Output: 0
Explanation: 
A[0] = 0, thus the output is 0.
Example 3:

Input: [-10,-5,3,4,7,9]
Output: -1
Explanation: 
There is no such i that A[i] = i, thus the output is -1.
 

Note:

1 <= A.length < 10^4
-10^9 <= A[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fixed-point
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def fixedPoint(self, A) -> int:
        for i,v in enumerate(A):
            if i == v:
                return i
        return -1

class Solution:
    def fixedPoint(self, A) -> int:
        left, right = 0, len(A)-1
        while left < right:
            mid = (left + right) //2
            if A[mid] < mid:
                left = mid + 1
            else:
                right = mid
        return left if A[left] == left else -1



S = Solution()
A = [-10,-5,0,3,7]
print(S.fixedPoint(A))
A = [0,2,5,8,17]
print(S.fixedPoint(A))
A = [-10,-5,3,4,7,9]
print(S.fixedPoint(A))
A = [-10,-5,-2,0,4,5,6,7,8,9,10]
print(S.fixedPoint(A))