"""
Given a string s, return the last substring of s in lexicographical order.

 

Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
Example 2:

Input: "leetcode"
Output: "tcode"
 

Note:

1 <= s.length <= 4 * 10^5
s contains only lowercase English letters.
"""
class Solution_1:
    """
    almost TLE, try another method
    """
    def lastSubstring(self, string):
        res = string
        for i in range(1,len(string)):
            tmp = string[i:]
            res = max(res, tmp)
        return res

from collections import defaultdict
class Solution:
    def lastSubstring(self, string):
        pos_dict = defaultdict(list)
        pre = string[0]
        len_s = len(string)
        pos_dict[pre].append(0)
        for i in range(1,len_s):
            s = string[i]
            if s != pre: #if we encounter a repeated sequence, such as 'zzzzzzzzzzzzzz', we only record the 1st postion of z, for it will leading to the largest substring
                pos_dict[s].append(i) 
                pre = s
        res = pos_dict[max(pos_dict.keys())]
        # print(res)
        plus_index = 1
        while len(res) > 1:
            res_2 = []
            plus_letter = ''
            for pos in res:
                tmp = pos + plus_index
                if tmp < len_s:
                    if string[tmp] > plus_letter:
                        res_2 = [pos]
                        plus_letter = string[tmp]
                    elif string[tmp] == plus_letter:
                        res_2.append(pos)
            res = res_2
            plus_index += 1
        return string[res.pop():]

s = Solution()
string = "abab"
print(s.lastSubstring(string))

string = "leetcode"
print(s.lastSubstring(string))

