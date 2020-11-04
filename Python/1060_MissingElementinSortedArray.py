"""
Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def missingElement(self, nums, k: int) -> int:
        pre = nums[0]
        for num in nums[1:]:
            gap = num - pre - 1
            if gap >= k:
                return pre + k
            else:
                k -= gap
            pre = num
        return pre + k


S = Solution()
A = [4,7,9,10]
K = 1
print(S.missingElement(A, K))
A = [4,7,9,10]
K = 3
print(S.missingElement(A, K))
A = [1,2,4]
K = 3
print(S.missingElement(A, K))