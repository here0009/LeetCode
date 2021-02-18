"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.
"""


from functools import lru_cache
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # TLE
        @lru_cache(None)
        def dp(string):
            res = 0
            for i in range(len(string) - 1):
                if string[i: i + 2] == 'ab':
                    res = max(res, x + dp(string[:i] + string[i + 2:]))
                elif string[i: i + 2] == 'ba':
                    res = max(res, y + dp(string[:i] + string[i + 2:]))
            return res

        return dp(s)

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # greedy, TLE
        def findall(string, pattern):
            res = []
            pre, idx = 0, 0
            len_p = len(pattern)
            s2 = ''
            while idx != -1:
                idx = string.find(pattern, pre)
                if idx == -1:
                    return res, s2 + string[pre:]
                else:
                    res.append(idx)
                    s2 += string[pre: idx]
                    pre = idx + len_p
            return res, s2 + string[pre:]

        @lru_cache(None)
        def dp(string):
            lst, s2 = findall(string, first)
            # print(lst, s2)
            if lst:
                return x * len(lst) + dp(s2)
            lst, s2 = findall(string, second)
            if lst:
                return y * len(lst) + dp(s2)
            return 0

        first, second = 'ab', 'ba'
        if x < y:
            first, second = second, first
            x, y = y, x
        return dp(s)


class Solution:
    def maximumGain(self, string: str, x: int, y: int) -> int:
        def strip_ab(string, target, score):
            a, b = target[0], target[1]
            idx = string.find(target)
            if idx == -1:
                return 0, string
            i, j = idx, idx + 1
            while i >= 0 and j < len(string) and string[i] == a and string[j] == b:
                i -= 1
                j += 1
            # print(string, string[i+1:j])
            return score *(j - i - 1) // 2, string[:i + 1] + string[j:]

        first, second = 'ab', 'ba'
        if x < y:
            first, second = second, first
            x, y = y, x
        res = 0
        while True:
            score, s2 = strip_ab(string, first, x)
            # print('first', score, s2)
            if s2 != string:
                res += score
                string = s2
            else:
                score, s2 = strip_ab(string, second, y)
                # print('second', score, s2)
                if s2 != string:
                    res += score
                    string = s2
                else:
                    return res
"""
Greedy:
if ab > ba, we can always delete ba, then delete ab to get maximum score. delete ab won't generate new ba
e.g.
baba
aaba
"""

class Solution:
    def maximumGain(self, string: str, x: int, y: int) -> int:
        def strip_ab(string, a, b, score):
            stack = []
            res = 0
            for c in string:
                if c == b and stack and stack[-1] == a:
                    stack.pop()
                    res += score
                else:
                    stack.append(c)
            return ''.join(stack), res

        a, b = 'a', 'b'
        if x < y:
            a, b = 'b', 'a'
            x, y = y, x
        s2, ab = strip_ab(string, a, b, x)
        _, ba = strip_ab(s2, b, a, y)
        return ab + ba


S = Solution()
string = "cdbcbbaaabab"
"cdbcabab"
x = 4
y = 5
print(S.maximumGain(string, x, y))
string = "aabbaaxybbaabb"
x = 5
y = 4
print(S.maximumGain(string, x, y))
string = "aabbrtababbabmaaaeaabeawmvaataabnaabbaaaybbbaabbabbbjpjaabbtabbxaaavsmmnblbbabaeuasvababjbbabbabbasxbbtgbrbbajeabbbfbarbagha"
x = 8484
y = 4096
print(S.maximumGain(string, x, y))
string = "aaaaaaaaaaaaaaaaaaaaaaaaa"
x = 5
y = 4
print(S.maximumGain(string, x, y))