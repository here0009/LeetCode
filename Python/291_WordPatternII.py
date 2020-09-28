"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

 

Example 1:

Input: pattern = "abab", str = "redblueredblue"
Output: true
Example 2:

Input: pattern = "aaaa", str = "asdasdasdasd"
Output: true
Example 3:

Input: pattern = "aabb", str = "xyzabcxzyabc"
Output: false
 

Constraints:

You may assume both pattern and str contains only lowercase letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def wordPatternMatch(self, pattern: str, string: str) -> bool:
        """
        Thoughts: top-down test(p, s)
        """
        def test(p, s):
            # print(p, s, maps, rev_maps)
            len_p, len_s = len(p), len(s)
            if len_p == len_s == 0:
                return True
            if len_p > len_s or len_p == 0:
                return False
            letter = p[0]
            if letter in maps:
                target = maps[letter]
                if target not in rev_maps or rev_maps[target] != letter:
                    return False
                else:
                    return s[:len(target)] == target and test(p[1:], s[len(target):])
            else:
                for i in range(1, len_s-len_p+2):
                    maps[p[0]] = s[:i]
                    if s[:i] in rev_maps and rev_maps[s[:i]] != p[0]:
                        del maps[p[0]]
                        continue
                    rev_maps[s[:i]] = p[0]
                    if test(p[1:], s[i:]):
                        return True
                    del maps[p[0]]
                    del rev_maps[s[:i]]
                return False

        maps = dict()
        rev_maps = dict()
        # print(pattern, string)
        return test(pattern, string)

S = Solution()
pattern = "abab"
string = "redblueredblue"
print(S.wordPatternMatch(pattern, string))
pattern = "aaaa"
string = "asdasdasdasd"
print(S.wordPatternMatch(pattern, string))
pattern = "aabb"
string = "xyzabcxzyabc"
print(S.wordPatternMatch(pattern, string))
pattern = "ab"
string = "aa"
print(S.wordPatternMatch(pattern, string))
pattern = "abba"
string = "dogcatcatdog"
print(S.wordPatternMatch(pattern, string))
pattern = "itwasthebestoftimes"
string = "ittwaastthhebesttoofttimes"
print(S.wordPatternMatch(pattern, string))
# 输出：
# false
# 预期结果：
# true