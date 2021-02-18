"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
"""


from typing import List
from math import gcd
from functools import lru_cache
from itertools import permutations
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def calc(n1, n2, sign):
            p1, q1 = n1
            p2, q2 = n2
            if sign == '/':
                p3 = p1 * q2
                q3 = p2 * q1
            else:
                q3 = q1 * q2
                if sign == '+':
                    p3 = p1 * q2 + p2 * q1
                elif sign == '-':
                    p3 = p1 * q2 - p2 * q1
                elif sign == '*':
                    p3 = p1 * p2
            k = gcd(p3, q3)
            if k != 0:
                return p3 // k, q3 // k
            else:
                return p3, q3

        def dfs(index):
            # print(index)
            if index == 4:
                return []
            if index == 3:  # the last one
                # print(index, [nums2[3]])
                return [nums2[3]]
            res = []
            # 2 ways
            # 1. calc index, index + 1, dfs(index + 2)
            # 2. calc index  sign dfs(index + 1)
            num = nums2[index]
            for sign in signs:
                for n2 in dfs(index + 1):
                    res.append(calc(num, n2, sign))
            lst = dfs(index + 2)
            for sign in signs:
                n1 = calc(nums2[index], nums2[index + 1], sign)
                for sign in signs:
                    for n2 in lst:
                        res.append(calc(n1, n2, sign))
            # print(index, res)
            return res

        signs = '+-*/'
        for perm in permutations(nums):
            nums2 = [(v, 1) for v in perm]
            lst = dfs(0)  # use fraction to do the calculation
            for p, q in lst:
                if q != 0 and p // q == 24 and p % q == 0:
                    # print(p, q)
                    return True
        return False


from typing import List
from math import gcd
from functools import lru_cache
from itertools import permutations
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def calc(n1, n2, sign):
            p1, q1 = n1
            p2, q2 = n2
            if sign == '/':
                p3 = p1 * q2
                q3 = p2 * q1
            else:
                q3 = q1 * q2
                if sign == '+':
                    p3 = p1 * q2 + p2 * q1
                elif sign == '-':
                    p3 = p1 * q2 - p2 * q1
                elif sign == '*':
                    p3 = p1 * p2
            k = gcd(p3, q3)
            if k != 0:
                return p3 // k, q3 // k
            else:
                return p3, q3

        def dfs(index):
            if index == 4:
                return set()
            if index == 3:  # the last one
                return set([nums2[3]])
            res = set()
            num = nums2[index]
            for sign in signs:
                for n2 in dfs(index + 1):
                    res.add(calc(num, n2, sign))
            lst = dfs(index + 2)
            for sign in signs:
                n1 = calc(nums2[index], nums2[index + 1], sign)
                for sign in signs:
                    for n2 in lst:
                        res.add(calc(n1, n2, sign))
            return res

        signs = '+-*/'
        for perm in permutations(nums):
            nums2 = [(v, 1) for v in perm]  # use fraction to do the calculation
            lst = dfs(0)
            for p, q in lst:
                if q != 0 and p // q == 24 and p % q == 0:
                    return True
        return False

S = Solution()
nums = [4, 1, 8, 7]
print(S.judgePoint24(nums))
nums = [1, 2, 1, 2]
print(S.judgePoint24(nums))
# for perm in permutations(nums):
#     print(perm)
nums = [1,1,7,7]
print(S.judgePoint24(nums))