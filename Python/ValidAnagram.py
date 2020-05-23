"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_set = set(s)
        t_set = set(t)
        if s_set != t_set:
            return False
        if all(s.count(letter) ==  t.count(letter) for letter in s_set):
            return True
        else:
            return False

sl = Solution()
s = "anagram"
t = "nagaram"
print(sl.isAnagram(s,t))
s = "rat"
t = "car"
print(sl.isAnagram(s,t))

        