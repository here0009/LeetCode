"""
Given an array of integers cost and an integer target. Return the maximum integer you can paint under the following rules:

The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
The total cost used must be equal to target.
Integer does not have digits 0.
Since the answer may be too large, return it as string.

If there is no way to paint any integer given the condition, return "0".

 

Example 1:

Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: "7772"
Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.
Digit    cost
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
Example 2:

Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
Output: "85"
Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
Example 3:

Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
Output: "0"
Explanation: It's not possible to paint any integer with total cost equal to target.
Example 4:

Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
Output: "32211"
 

Constraints:

cost.length == 9
1 <= cost[i] <= 5000
1 <= target <= 5000
"""


from typing import List
from functools import lru_cache
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        """
        wrong anwer
        """
        def comp(str1, str2):
            if str1 is None:
                return str2
            if str2 is None:
                return str1
            len_s1, len_s2 = len(str1), len(str2)
            if len_s1 > len_s2:
                return str1
            elif len_s2 > len_s1:
                return str2
            else:
                if str1 > str2:
                    return str1
            return str2

        @lru_cache(None)
        def dp(value, index):
            if value == 0:
                print('v', value)
                return ''
            if index == len_keys:
                return None
            res = dp(value, index + 1)
            v = keys[index]
            k = str(cost_dict[v])
            ks = ''
            while value - v >= 0:
                value -= v
                ks += k
                next_v = dp(value, index + 1)
                if next_v:
                    res = comp(res, ks + next_v)
            # if res != -float('inf'):
            #     res_str = sorted(list(str(res)), reverse=True)
            #     res = int(''.join(res_str))
            print(value, index, res)
            return res

        cost_dict = dict()  # max digit you can get for that cost
        for i, v in enumerate(cost, 1):
            cost_dict[v] = i
        # print(cost_dict)
        keys = sorted(cost_dict.keys(), key=lambda x: cost_dict[x], reverse=True)
        len_keys = len(keys)
        res = dp(target, 0)
        return res if res else '0'


from typing import List
from functools import lru_cache
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        @lru_cache(None)
        def dp(value, index):
            if value == 0:
                return 0
            if index == len_keys:
                return -float('inf')
            res = dp(value, index + 1)
            v = keys[index]
            k = str(cost_dict[v])
            ks = ''
            while value - v >= 0:
                value -= v
                ks += k
                next_v = dp(value, index + 1)
                if next_v != -float('inf'):
                    str_next_v = str(next_v) if next_v > 0 else ''
                    res = max(res, int(ks + str_next_v))
            return res

        cost_dict = dict()  # max digit you can get for that cost
        for i, v in enumerate(cost, 1):
            cost_dict[v] = i
        # print(cost_dict)
        keys = sorted(cost_dict.keys(), key=lambda x: cost_dict[x], reverse=True)
        len_keys = len(keys)
        res = dp(target, 0)
        return str(res) if res != -float('inf') else '0'

S = Solution()
cost = [4,3,2,5,6,7,2,5,5]
target = 9
print(S.largestNumber(cost, target))
cost = [7,6,5,5,5,6,8,7,8]
target = 12
print(S.largestNumber(cost, target))
cost = [2,4,6,2,4,6,4,4,4]
target = 5
print(S.largestNumber(cost, target))
cost = [6,10,15,40,40,40,40,40,40]
target = 47
print(S.largestNumber(cost, target))