"""
Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.

Return 0 if S is odd, otherwise return 1.

 

Example 1:

Input: [34,23,1,24,75,33,54,8]
Output: 0
Explanation: 
The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.
Example 2:

Input: [99,77,33,66,55]
Output: 1
Explanation: 
The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
 

Constraints:

1 <= A.length <= 100
1 <= A[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def sumOfDigits(self, A) -> int:
        return int(sum([int(i) for i in list(str(min(A)))]) % 2 == 0)

S = Solution()
A = [34,23,1,24,75,33,54,8]
print(S.sumOfDigits(A))
A = [99,77,33,66,55]
print(S.sumOfDigits(A))