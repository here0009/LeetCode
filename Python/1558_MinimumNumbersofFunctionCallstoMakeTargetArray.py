"""
Your task is to form an integer array nums from an initial array of zeros arr that is the same size as nums.

Return the minimum number of function calls to make nums from arr.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: nums = [1,5]
Output: 5
Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
Total of operations: 1 + 2 + 2 = 5.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Increment by 1 (both elements) [0, 0] -> [0, 1] -> [1, 1] (2 operations).
Double all the elements: [1, 1] -> [2, 2] (1 operation).
Total of operations: 2 + 1 = 3.
Example 3:

Input: nums = [4,2,5]
Output: 6
Explanation: (initial)[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5](nums).
Example 4:

Input: nums = [3,2,2,4]
Output: 7
Example 5:

Input: nums = [2,4,8,16]
Output: 8
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
"""

import math
class Solution:
    def minOperations(self, nums) -> int:
        """
        wrong answer
        """
        max_v = max(nums)
        mul = int(math.log(max_v, 2))
        print(max_v, mul, 2**mul, max_v - 2**mul)
        res = math.ceil(math.log(max_v, 2))
        for num in nums:
            if num == 1 or num == max_v:
                res += 1
            elif num < max_v:
                res += num % 2 + 1
        # print(nums, max_v, res)
        return res

from functools import lru_cache
class Solution:
    def minOperations(self, nums) -> int:
        @lru_cache(None)
        def minOpt(num):
            if num == 0:
                return 0, 0
            if num % 2 == 1:
                m, a = minOpt(num -1)
                return m, a + 1
            else:
                m, a = minOpt(num //2 )
                return m + 1, a

        multiply, add = 0, 0
        for num in nums:
            m, a = minOpt(num)
            multiply = max(m, multiply)
            add += a
        return multiply + add

class Solution:
   def minOperations(self, A):
        return sum(bin(a).count('1') for a in A) + len(bin(max(A))) - 3
        
S = Solution()
nums = [1,5]
print(S.minOperations(nums))
nums = [2,2]
print(S.minOperations(nums))
nums = [4,2,5]
print(S.minOperations(nums))
nums = [3,2,2,4]
print(S.minOperations(nums))
nums = [2,4,8,16]
print(S.minOperations(nums))
nums = [1000000000]
print(S.minOperations(nums))
# Output
# 31
# Expected
# 42
