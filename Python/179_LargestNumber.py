"""
Given a list of non-negative integers nums, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
Example 3:

Input: nums = [1]
Output: "1"
Example 4:

Input: nums = [10]
Output: "10"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""


from typing import List
from collections import defaultdict
class Solution:
    """
    wrong answer
    """
    def largestNumber(self, nums: List[int]) -> str:
        def mergeString(lst: List[(str, int)]) -> List[(str, int)]:
            """
            merege str in lst
            """
            str_dict = defaultdict(list)
            for string, flag in lst:
                if len(string) == 1:
                    str_dict[string[0]].append((string[0], 0))
                else:
                    str_dict[string[0]].append((string[1:], 1))
            keys = sorted(str_dict.keys(), reverse=True)
            res = []
            for key in keys:
                tmp = ''
                vals = mergeString(str_dict[key])
                for string, flag in vals:
                    if flag:
                        tmp += key + val
                    else:
                        tmp += key
                res.append(tmp)
            return res


        str_nums = [str(num) for num in nums]
        return mergeString(str_nums)


from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = [str(num) for num in nums]
        max_len = max(len(s) for s in str_nums)
        pad_str = dict()
        for s in str_nums:
            tmp = s
            len_s = len(s)
            while len(tmp) < max_len:
                tmp += s[:min(len_s, max_len-len(tmp))]
            pad_str[s] = tmp
        # print(pad_str)
        str_nums = sorted([str(num) for num in nums], key=lambda x:(pad_str[x], len(x)), reverse = True)
        return ''.join(str_nums)

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        It is hard to find a pattern and implement one
        so we just compare a+b and b+a
        """
        cmp = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        str_nums = map(str, nums)
        str_nums = sorted(str_nums, key= cmp_to_key(cmp), reverse = True)
        return str(int(''.join(str_nums)))

S = Solution()
nums = [10,2]
print(S.largestNumber(nums))
nums = [3,30,34,5,9]
print(S.largestNumber(nums))
nums = [1]
print(S.largestNumber(nums))
nums = [10]
print(S.largestNumber(nums))
nums = [432,43243]
print(S.largestNumber(nums))
# Output
# "43243243"
# Expected
# "43243432"
nums = [111311, 1113]
# Output
# "1113111113"
# Expected
# "1113111311"