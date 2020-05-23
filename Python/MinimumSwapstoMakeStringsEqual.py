"""
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

 

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: 
Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
Example 2: 

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: 
Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you can't swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1
Example 4:

Input: s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
Output: 4
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
"""  
from collections import Counter
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        
        s1_remain = ''
        s2_remain = ''
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                s1_remain += s1[i]
                s2_remain += s2[i]
        # print(s1_remain)
        # print(s2_remain)
        s1_counter = Counter(s1_remain)
        s2_counter = Counter(s2_remain)
        s1_x, s1_y = s1_counter['x'], s1_counter['y']
        s2_x, s2_y = s2_counter['x'], s2_counter['y']
        if s1_x != s2_y or s1_y != s2_x or s1_x % 2 != s1_y % 2: #s1_x should be always eaqual to s2_y, and s1_y should be always equal to s2_x
            return -1
        res = s1_x // 2 + s1_y // 2 
        if s1_x % 2 + s1_y % 2 == 2:
            res += 2
        return res

        


s = Solution()
s1 = "xx"
s2 = "yy"
print(s.minimumSwap(s1,s2))

s1 = "xy"
s2 = "yx"
print(s.minimumSwap(s1,s2))

s1 = "xx"
s2 = "xy"
print(s.minimumSwap(s1,s2))

s1 = "xxyyxyxyxx"
s2 = "xyyxyxxxyx"
print(s.minimumSwap(s1,s2))