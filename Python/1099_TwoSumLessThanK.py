"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-less-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def twoSumLessThanK(self, A, K: int) -> int:
        length = len(A)
        res = -1
        for i in range(length-1):
            for j in range(i+1, length):
                tmp = A[i] + A[j]
                if tmp < K:
                    res = max(res, tmp)
        return res

S = Solution()
A = [34,23,1,24,75,33,54,8]
K = 60
print(S.twoSumLessThanK(A, K))
A = [10,20,30]
K = 15
print(S.twoSumLessThanK(A, K))