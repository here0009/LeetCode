"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_set = set(s)
        t_set = set(t)
        diff_element = t_set - s_set
        if diff_element:
            res = diff_element.pop()
            return res
        s_dict = dict()
        t_dict = dict()
        for letter in s:
            s_dict[letter] = s_dict.get(letter,0)+1
        for letter in t:
            t_dict[letter] = t_dict.get(letter,0)+1
        for letter in t_set:
            if t_dict[letter] > s_dict[letter]:
                return letter
        return 0

class Solution_1:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in set(t):
            if t.count(i) > s.count(i):
                print(t.count(i))
                print(s.count(i))
                return i

q = Solution_1()
s = "abcd"
t = "abcde"
print(q.findTheDifference(s,t))
s = "abcde"
t = "abcdea"
print(q.findTheDifference(s,t))