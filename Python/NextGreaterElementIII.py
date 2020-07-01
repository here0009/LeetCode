"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        """
        wrong answer
        """
        digits = [int(i) for i in list(str(n))]
        # print(digits)
        index = len(digits) - 1
        while index >= 0:
            num = digits[index]
            for i in range(index-1, -1, -1):
                if num > digits[i]:
                    # split from i
                    digits[index], digits[i] = digits[i], digits[index]
                    digits = digits[:i+1] + sorted(digits[i+1:])
                    # print(index,digits)
                    return int(''.join(str(i) for i in digits))
            index -= 1
        return -1


import bisect
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        INT_MAX = 2**31 - 1
        digits = [int(i) for i in list(str(n))]
        # print(digits)
        i = len(digits) - 1
        res = []
        while i >= 0:
            j = bisect.bisect_right(res, digits[i])
            if j == len(res):
                res.append(digits[i])
            else:
                digits[i], res[j] = res[j], digits[i]
                res = int(''.join([str(k) for k in digits[:i+1] + res]))
                return res if res <= INT_MAX else -1
            i -= 1
        return -1


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        length = len(digits)
        i, j = length-2, length-1
        while i >= 0 and digits[i+1] <= digits[i]:
            i -= 1
        #digits[i] < digits[i+1]
        if i == -1:
            return -1
        while digits[j] <= digits[i]: #digits[i:] is non-increasing, so j is the min val in digits[i:] that larger than digits[i]
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        res = int(''.join(digits[:i+1] + digits[i+1:][::-1]))
        if res >= 2**31 or res == n:
            return -1
        return res

print(2**31 - 1)
S = Solution()
n = 12
print(S.nextGreaterElement(n))
n = 12345
print(S.nextGreaterElement(n))
n = 54321
print(S.nextGreaterElement(n))
n = 78123795413412
print(S.nextGreaterElement(n))
n = 25431
print(S.nextGreaterElement(n))
n = 230241
print(S.nextGreaterElement(n))
# Output
# 231024
# Expected
# 230412
n = 1999999999
print(S.nextGreaterElement(n))
# Output
# 9199999999
# Expected
# -1