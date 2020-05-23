"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import Counter
class Solution_1:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_Counter = Counter(s)
        # print(s_Counter)
        unique_set = set()

        for key, value in s_Counter.items():
            if value == 1:
                unique_set.add(key)
        # print(unique_set)
        if len(unique_set) == 0:
            return -1
        for index, letter in enumerate(s):
            if letter in unique_set:
                return index

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for letter in s:
            l = s.find(letter)
            r = s.rfind(letter)
            if l == r != -1:
                return l
        return -1

s = Solution()
print(s.firstUniqChar("leetcode"))
print(s.firstUniqChar("loveleetcode"))
print(s.firstUniqChar(""))