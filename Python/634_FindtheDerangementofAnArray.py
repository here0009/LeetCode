"""
In combinatorial mathematics, a derangement is a permutation of the elements of a set, such that no element appears in its original position.

There's originally an array consisting of n integers from 1 to n in ascending order, you need to find the number of derangement it can generate.

Also, since the answer may be very large, you should return the output mod 109 + 7.

Example 1:
Input: 3
Output: 2
Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].
Note:
n is in the range of [1, 106].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-derangement-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findDerangement(self, n: int) -> int:
        """
        dp(n) = (n-1)(dp(n-1) + dp(n-2))
        from n-1 we can got to n in 2 ways:
        1. all num in the list is derangement, we just need to swap n with any num in the list, that is (n-1)*dp(n-1)
        2. one num in the list is in place, others are all out of place, we swap that in-placed num with n. that is (n-1)*dp(n-2)
        """
        if n <= 1:
            return 0
        M = 10**9+7
        pre, curr = 0, 1
        for i in range(3,n+1):
            pre, curr = curr % M, (i - 1)*(pre + curr) % M
        return curr

S = Solution()
for i in range(11):
    print(i, S.findDerangement(i))
print('::3', S.findDerangement(3))
print(99999, S.findDerangement(99999))
