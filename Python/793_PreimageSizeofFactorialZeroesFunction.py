"""
Let f(x) be the number of zeroes at the end of x!. (Recall that x! = 1 * 2 * 3 * ... * x, and by convention, 0! = 1.)

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has 2 zeroes at the end. Given K, find how many non-negative integers x have the property that f(x) = K.

Example 1:
Input: K = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with K = 0 zeroes.

Example 2:
Input: K = 5
Output: 0
Explanation: There is no x such that x! ends in K = 5 zeroes.
Note:

K will be an integer in the range [0, 10^9].
"""


class Solution:
    def preimageSizeFZF(self, K: int) -> int:
        """
        the res will be zero or 5
        K x
        0 0~4
        1 5~9
        2 10~14
        3 15~19
        4 20~24
        6 25~29

        the pattern of K is
        0~4, 6~10, 12~16

        directly computing can be difficult, we can test how may trailing zeros a number have easily. just count the counts of factor 5 it got.
        so we can use binary search to guess and test.
        number right = 5*K got at least K trailing zeros,  and left = 0 got 0 zeros
        computing of the counts of factor 5 a number get can be done by the following example
        num = 100
        d = 5
        counts += 100//5
        num = 100//5 = 20
        counts += 20//5
        num = 20//5 = 4
        counts += 4//5
        finaly counts = 24
        """
        def factor5(num):
            res = 0
            while num > 0:
                num = num // 5
                res += num
            return res

        left, right = 0, 5*K
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            tmp = factor5(mid)
            if tmp < K:
                left = mid + 1
            else:
                right = mid
        if factor5(left) == K:
            return 5
        return 0
        



S = Solution()
for i in range(12):
    print(i, S.preimageSizeFZF(i))
# print(S.preimageSizeFZF(2))
# def zeros(num):
#     str_num = str(num)
#     index = len(str_num) - 1
#     while index >= 0 and str_num[index] == '0':
#         index -= 1
#     return len(str_num) - 1 - index

# base = 1
# for i in range(1, 52):
#     base *= i
#     print(i, base, zeros(base))
print(28246, S.preimageSizeFZF(28246))