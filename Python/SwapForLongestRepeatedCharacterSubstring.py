"""
Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

Example 1:

Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
Example 2:

Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
Example 3:

Input: text = "aaabbaaa"
Output: 4
Example 4:

Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
Example 5:

Input: text = "abcdef"
Output: 1
 

Constraints:

1 <= text.length <= 20000
text consist of lowercase English characters only.
"""
from collections import defaultdict
class Solution:
    def maxLen(self,pos):
        len_p = len(pos)
        if len_p == 1:
            return pos[0][1] - pos[0][0]
        elif len_p == 2 :
            if pos[1][0] - pos[0][1] == 1: #merge
                res = pos[1][1] - pos[0][0] - 1
            else:
                res =  max(pos[1][1]-pos[1][0], pos[0][1]-pos[0][0])+1
        else:
            res = pos[0][1] - pos[0][0] +1
            for i in range(1,len_p):
                if pos[i][0] - pos[i-1][1] == 1:
                    res = max(res, pos[i][1] - pos[i-1][0])
                else:
                    res = max(res, pos[i][1]-pos[i][0]+1)
        return res


    def maxRepOpt1(self, text: str) -> int:
        pos_dict = defaultdict(list)
        pre = text[0]
        start_index = 0
        res = 1
        for i in range(1,len(text)):
            t = text[i]
            if t != pre:
                pos_dict[pre].append((start_index,i))
                start_index = i
                pre = t
        pos_dict[pre].append((start_index,len(text)))
        # print(pos_dict)
        for key in pos_dict:
            res = max(res, self.maxLen(pos_dict[key]))
        return res

s = Solution()
# text = "ababa"
# print(s.maxRepOpt1(text))

# text = "aaabaaa"
# print(s.maxRepOpt1(text))

# text = "aaabbaaa"
# print(s.maxRepOpt1(text))

# text = "aaaaa"
# print(s.maxRepOpt1(text))

# text = "abcdef"
# print(s.maxRepOpt1(text))

text = "babbaaabbbbbaa"
print(s.maxRepOpt1(text))