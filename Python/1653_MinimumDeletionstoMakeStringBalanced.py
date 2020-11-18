"""
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        wronag answer
        """
        first_b = s.find('b')
        last_a = s.rfind('a')
        a, b = 0, 0
        for i,v in enumerate(s):
            if v == 'a' and i > first_b:
                a += 1
            elif v == 'b' and i < last_a:
                b += 1
        print(first_b, last_a, a, b)
        return min(a, b)

class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        max length of string can be made by deletion
        """
        pre, a, b = 0, 0, 0
        for letter in s:
            if letter == 'a':
                a += 1
            elif letter == 'b':
                b += 1
            if a >= b:
                pre += a
                a = 0
                b = 0
        return len(s) - (pre + max(a, b))


class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = 0, 0
        for c in s:
            if c == 'a':
                a += 1
            else:
                a = min(a, b)
                b += 1
        return min(a, b)

S = Solution()
s = "aababbab"
print(S.minimumDeletions(s))
s = "bbaaaaabb"
print(S.minimumDeletions(s))
s = "ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa"
print(S.minimumDeletions(s))
# 输出：
# 28
# 预期：
# 25