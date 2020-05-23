"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:

Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
Example 2:

Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199
Follow up:
How would you handle overflow for very large input integers?
"""
from itertools import combinations
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        len_num = len(num)
        for i, j in combinations(range(1,len_num),2):
            a, b = num[:i], num[i:j]
            if a != str(int(a)) or b != str(int(b)):
                continue
            while j < len_num:
                c = str(int(a)+int(b))
                print(a,b,c)
                if num[j:j+len(c)] != c:
                    break
                else:
                    a, b = b, c
                    j += len(c)
            if j == len_num:
                return True
        return False

s = Solution()
num = "199100199"
print(s.isAdditiveNumber(num))

num = "1023"
print(s.isAdditiveNumber(num))

num = "000"
print(s.isAdditiveNumber(num))