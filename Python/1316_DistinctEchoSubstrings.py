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


class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        """
        try to use suffix tree
        """
        res = set()
        root = TreeNode(0, -1)
        for i,v in enumerate(text):
            string = text[i:]
            _insert(root, string)