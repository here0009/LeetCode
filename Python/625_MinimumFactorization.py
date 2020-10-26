"""
Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input:

48 
Output:
68
Example 2
Input:

15
Output:
35

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-factorization
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def smallestFactorization(self, a: int) -> int:
        if a < 10:
            return a
        M = 1 << 31
        lst = []
        for d in range(9, 1, -1):
            while a % d == 0:
                lst.append(d)
                a = a//d
        lst = sorted(lst)
        if not lst or a != 1:
            return 0
        res = int(''.join(str(i) for i in lst))
        return res if res < M else 0

S  = Solution()
print(S.smallestFactorization(48))
print(S.smallestFactorization(15))
for i in range(1,20):
    print(i, S.smallestFactorization(i))
print(S.smallestFactorization(22))
a = 18000000
print(S.smallestFactorization(a))