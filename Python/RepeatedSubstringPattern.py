"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""
class Solution_1:
    def repeatedSubstringPattern(self, s: str) -> bool:
        first = s[0]
        first_list = []
        for i in range(1,len(s)):
            if s[i] == first:
                first_list.append(i)
        for bp in first_list: #break point
            first_substring = s[:bp]
            break_flag = False
            for k in range(bp,len(s),bp):
                if s[k:k+bp] != first_substring:
                    # print(first_substring, s[k:k+bp])
                    break_flag = True
                    break
            if not break_flag:
                return True
        return False

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        如果s中存在重复元素,2s去掉首尾后,必然还能在中间找到一个s
        """
        ss = (s + s)[1:-1]
        return ss.find(s) != -1


S = Solution()
s = "abab"
print(S.repeatedSubstringPattern(s))

s = "aba"
print(S.repeatedSubstringPattern(s))

s = "abcabcabcabc"
print(S.repeatedSubstringPattern(s))