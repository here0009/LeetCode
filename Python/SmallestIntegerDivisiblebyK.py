"""
Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

 

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
 

Note:

1 <= K <= 10^5
"""
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        """
        如果K可以被2或5整除, 则不存在11.111可以整除K, 因为末尾为1.
        K个11..11除以K, 最多有K个余数, 如果有1个为0, 整除返回
        如果有两个为0. 则这两个数的差为11..000形式, 可以被2或5整除, 再第一步返回.
        """
        if K%2 == 0 or K%5 == 0:
            return -1
        r = 1
        for digits in range(1,K+1):
            if r % K == 0:
                return digits
            else:
                r = (r*10 + 1)%K
        return -1

s = Solution()
print(s.smallestRepunitDivByK(1))
print(s.smallestRepunitDivByK(2))
print(s.smallestRepunitDivByK(3))
print(s.smallestRepunitDivByK(5))
print(s.smallestRepunitDivByK(9))

# def test(K, iterations):
#     N = 1
#     for i in range(iterations):
#         print(N, N%K)
#         N = N*10 + 1
# test(9,40)