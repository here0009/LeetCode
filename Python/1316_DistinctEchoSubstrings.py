"""
Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself (i.e. it can be written as a + a where a is some string).

 

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
 

Constraints:

1 <= text.length <= 2000
text has only lowercase English letters.
"""


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        thought: suffix array, wroang for the case:
        abcabcdabcc:
        sorted as
        abcabcdabcc
        abcc
        abcdabcc
        """
        suffix_arry = []
        len_text = len(text)
        for i in range(len_text):
            suffix_arry.append((text[i:], i))
        suffix_arry.sort()


class TreeNode:

    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.children = dict()

# https://leetcode.com/problems/distinct-echo-substrings/discuss/477935/Python-hash-1068ms
from collections import defaultdict
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        """
        len_text = len(text)
        idx = defaultdict(list)
        res = set()
        for i, v in enumerate(text):
            for j in idx[v][::-1]:
                if i + i - j > len_text:
                    break
                if text[j:i] == text[i:i + i - j]:
                    res.add(text[j:i])
            idx[v].append(i)
        return len(res)

class Solution_1:
    def distinctEchoSubstrings(self, text: str) -> int:
        res = set()
        ix = {}
        for i, c in enumerate(text):
            if c in ix:
                for j in ix[c][::-1]:
                    if i + i - j > len(text): break # Early stopping 
                    if text[j:i] == text[i:i+i-j]:
                        res.add(text[j:i+i-j])
                ix[c].append(i)
            else:
                ix[c] = [i]
        print(res)
        return len(res) 

S = Solution()
text = "abcabcabc"
print(S.distinctEchoSubstrings(text))
text = "leetcodeleetcode"
print(S.distinctEchoSubstrings(text))
text = 'tkfbgwgqvdsbnukcpxlpifuhbvtdxhhhqurotspohiuwhblnra'
print(S.distinctEchoSubstrings(text))