"""
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""


from typing import List
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        2 sources:
        1. the num is palindrome
        2. num % 11 + rev(num) % 11 == 11
        """

        def rev(num):
            return int(str(num)[::-1])

        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                n1, n2 = nums[i], nums[j]
                if n1 + rev(n2) == n2 + rev(n1):
                    print(n1, n2, n1 + n2, n2 + rev(n1))
        print(nums)
        print([num % 11 for num in nums])
        rev_nums = [rev(num) for num in nums]
        print(rev_nums)
        print([num % 11 for num in rev_nums])

        return


from typing import List
from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        2 sources:
        1. the num is palindrome
        2. num % 11 + rev(num) % 11 == 11
        """

        def rev(num):
            return int(str(num)[::-1])

        res = 0
        M = 10**9 + 7
        length = len(nums)
        rev_nums = [rev(num) for num in nums]
        pl = []
        non_pl = []
        for i in range(length):
            if nums[i] == rev_nums[i]:
                pl.append(nums[i])
            else:
                non_pl.append(nums[i])

        
        # rmd_counts = Counter([num % 11 for num in non_pl])
        rev_rmd_counts = Counter([rev(num) % 11 for num in non_pl])
        # print(pl)
        # print(non_pl)
        # print([num % 11 for num in non_pl])
        # print([rev(num) for num in non_pl])
        # print([rev(num) % 11 for num in non_pl])
        # print(rmd_counts)
        for num in non_pl:
            rmd = num % 11
            c = rev_rmd_counts[11 - rmd]
            if rev(num) % 11 == 11 - rmd:
                c -= 1
            res += c
            res = res % M
        res = res // 2
        res += len(pl) * (len(pl) - 1) // 2
        res = res % M
        return res


from typing import List
from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int(str(num)[::-1])

        diff = Counter([num - rev(num) for num in nums])
        res = 0
        M = 10**9 + 7
        for v in diff.values():
            res += v * (v - 1) // 2
            res = res % M
        return res

S = Solution()
nums = [42,11,1,97]
print(S.countNicePairs(nums))
nums = [13,10,35,24,76]
print(S.countNicePairs(nums))
nums = [432835222,112141211,5408045,456281503,283322436,414281561,37773,286505682]
print(S.countNicePairs(nums))
# 输出：
# 10
# 预期：
# 6
nums = [352171103,442454244,42644624,152727101,413370302,293999243]
print(S.countNicePairs(nums))
# 输出：
# 1
# 预期：
# 2