"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
from collections import deque
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        def trim_str(string):
            res = deque()
            for s in string:
                if s == '#':
                    if res:
                        res.pop()
                else:
                    res.append(s)
            return ''.join(res)

        return trim_str(S) == trim_str(T)
        # return trim_str(S),trim_str(T)

s = Solution()
S = "ab#c"
T = "ad#c"
print(s.backspaceCompare(S,T))
S = "ab##"
T = "c#d#"
print(s.backspaceCompare(S,T))
S = "a##c"
T = "#a#c"
print(s.backspaceCompare(S,T))
S = "a#c"
T = "b"
print(s.backspaceCompare(S,T))
S = "y#fo##f"
T = "y#f#o##f"
print(s.backspaceCompare(S,T))