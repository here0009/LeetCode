"""
你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

示例 1：

输入： pattern = "abba", value = "dogcatcatdog"
输出： true
示例 2：

输入： pattern = "abba", value = "dogcatcatfish"
输出： false
示例 3：

输入： pattern = "aaaa", value = "dogcatcatdog"
输出： false
示例 4：

输入： pattern = "abba", value = "dogdogdogdog"
输出： true
解释： "a"="dogdog",b=""，反之也符合规则
提示：

1 <= len(pattern) <= 1000
0 <= len(value) <= 1000
你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pattern-matching-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:

        @lru_cache(None)
        def dp(pi, vi, a, b):
            # print(pi, vi, a, b)
            if pi == len_pattern and vi == len_value and (a or b):
                return True
            if pi == len_pattern: # because a or b can be '', when vi == len_value, pi can smaller than pi
                return False

            if pattern[pi] == 'a':
                if a is not None:
                    return value[vi: vi + len(a)] == a and dp(pi + 1, vi + len(a), a, b)
                else:
                    for k in range(max_a + 1):
                        if dp(pi + 1, vi + k, value[vi: vi + k], b):
                            return True
                    return False
            else:
                if b is not None:
                    return value[vi: vi + len(b)] == b and dp(pi + 1, vi + len(b), a, b)
                else:
                    for k in range(max_b + 1):
                        if dp(pi + 1, vi + k, a, value[vi: vi + k]):
                            return True
                    return False

        len_value = len(value)
        len_pattern = len(pattern)
        count_a, count_b = pattern.count('a'), pattern.count('b')
        if len_value == 0:
            return count_a == 0 or count_b == 0
        max_a = len_value // count_a if count_a != 0 else 0
        max_b = len_value // count_b if count_b != 0 else 0
        # print(pattern, value, max_a, max_b)
        return dp(0, 0, None, None)


S = Solution()
pattern = "abba"
value = "dogcatcatdog"
print(S.patternMatching(pattern, value))
pattern = "abba"
value = "dogcatcatfish"
print(S.patternMatching(pattern, value))
pattern = "aaaa"
value = "dogcatcatdog"
print(S.patternMatching(pattern, value))
pattern = "abba"
value = "dogdogdogdog"
print(S.patternMatching(pattern, value))

# for i in range(len(value) + 1):
#     print(i, value[0:i])

pattern = "a"
value = ""
print(S.patternMatching(pattern, value))
pattern = "bbbbbbbbbbbbbbabbbbb"
value = "ppppppppppppppjsftcleifftfthiehjiheyqkhjfkyfckbtwbelfcgihlrfkrwireflijkjyppppg"
# print(len(pattern), len(value))
print(S.patternMatching(pattern, value))
# 输出：
# false
# 预期结果：
# true