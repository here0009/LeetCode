"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.

Given a balanced string s split it in the maximum amount of balanced strings.

Return the maximum amount of splitted balanced strings.

 

Example 1:


        
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.
Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
 

Constraints:

1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""

class Solution:
    def balancedStringSplit(self, string) -> int:
        res = 0
        l,r = 0,0
        for curr in string:
            if curr == 'L':
                l += 1
            else:
                r += 1
            if l == r:
                res += 1
                l,r = 0,0
        return res

s = Solution()
string = "RLRRLLRLRL"
print(s.balancedStringSplit(string))

string = "RLLLLRRRLR"
print(s.balancedStringSplit(string))

string = "LLLLRRRR"
print(s.balancedStringSplit(string))

string = "LLL"
print(s.balancedStringSplit(string))

string = "RRLRRLRLLLRL"
print(s.balancedStringSplit(string))
# Output = 4
# Expected = 2