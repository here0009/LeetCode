"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
s
"""
from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        remove the peaks from beginning to end, if peak numbers is not larger than k, remove the last digits in nums (k - peak_numbers)
        """
        nums = deque([int(i) for i in num])
        stack = [-float('inf')]
        peak_counts = 0
        index = 0
        while nums and peak_counts < k:
            n = nums.popleft()
            if n < stack[-1]:
                stack.pop()
                peak_counts += 1
            stack.append(n)
            # print(nums,stack,peak_counts)
        print(stack[:])
        print(nums)
        res = ''.join([str(i) for i in stack[1+k-peak_counts:] + list(nums)])
        if not res:
            return '0'
        else:
            return str(int(res))

from functools import lru_cache
class Solution:
    """
    wrong answer
    """
    def removeKdigits(self, num: str, k: int) -> str:
        def int_to_strlist(n):
            return [i for i in str(n)]

        def str_to_int(string):
            return int(''.join(s for s in  string))

        @lru_cache(None)
        def dp(index, k):
            if self.counts < 100:
                 self.counts +=1
            else:
                return 0
            print(index,k)
            if index >= length or k <= 0 or length-index < k:
                return int(num)+1
            if length-index == k:
                return 0

            return min(str_to_int(nums_list[:index] + int_to_strlist(dp(j,k-1))) for j in range(index+1, length-k+1)) #remove nums[index]
        
        self.counts = 0
        nums_list = int_to_strlist(num)
        length = len(nums_list)
        return dp(0,k)

from collections import deque
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        nums = [int(i) for i in num]
        stack = [-float('inf')]
        peak_counts = 0
        index = 0
        length = len(nums)
        while index < length and peak_counts < k:
            while nums[index] < stack[-1] and peak_counts < k:
                stack.pop()
                peak_counts += 1
            stack.append(nums[index])
            index += 1
        # print(nums)
        # print(stack)
        if peak_counts == k:
            return str(int(''.join(str(i) for i in stack[1:]+nums[index:])))
        else:
            if len(stack)-1 <= k-peak_counts:
                return '0'
            return str(int(''.join(str(i) for i in stack[1:-(k-peak_counts)])))

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for d in num:
            while k and res and res[-1]>d:
                res.pop()
                k -= 1
            res.append(d)
        return ''.join(res[:-k or None]).lstrip('0') or '0' #if k == 0 return the entire res, that is res[:None] euqal to res, if k >0, that is res[:-k]

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for x in num:
            while stack and stack[-1] > x and k:
                stack.pop()
                k -= 1
            stack.append(x)
            
        return "".join(stack[:len(stack)-k]).lstrip("0") or "0"

S = Solution()
num = "1432219"
k = 3
print(S.removeKdigits(num, k))

num = "10200"
k = 1
print(S.removeKdigits(num, k))

num = "10"
k = 2
print(S.removeKdigits(num, k))

num ="9"
k = 1
print(S.removeKdigits(num, k))

num = "112"
k = 1
print(S.removeKdigits(num, k))

num = "1234567890"
k = 9
print(S.removeKdigits(num, k))
# Output
# "1"
# Expected
# "0"