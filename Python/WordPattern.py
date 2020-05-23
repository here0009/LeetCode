"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""
class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        pattern_list = list(pattern)
        string_list = string.split(' ')
        # print(pattern_list)
        # print(string_list)
        if len(pattern_list) != len(string_list):
            return False
        if len(pattern_list) == 0:
            return True
        pattern_set = set()
        string_set = set()
        comb_set = set()
        for i in range(len(pattern_list)):
            p = pattern_list[i]
            s = string_list[i]
            if (p in pattern_set and s in string_set):
                if (p,s) not in comb_set:
                    return False
                else:
                    continue
            if (p not in pattern_set and s in string_set) or (p in pattern_set and s not in string_set):
                return False
            if p not in pattern_set and s not in string_set:
                pattern_set.add(p)
                string_set.add(s)
                comb_set.add((p,s))
        return True

s = Solution()
pattern = "abba"
string = "dog cat cat dog"
print(s.wordPattern(pattern,string))

pattern = "abba"
string = "dog cat cat fish"
print(s.wordPattern(pattern,string))

pattern = "aaaa"
string = "dog cat cat dog"
print(s.wordPattern(pattern,string))

pattern = "abba"
string = "dog dog dog dog"
print(s.wordPattern(pattern,string))
