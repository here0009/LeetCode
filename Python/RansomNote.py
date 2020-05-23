"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""
class Solution_1:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ran_dict = self.strToDict(ransomNote)
        mag_dict = self.strToDict(magazine)
        for key, value in ran_dict.items():
            if key not in mag_dict or value > mag_dict[key]:
                return False
        return True

    def strToDict(self, string):
        dict_s = dict()
        for s in string:
            dict_s[s] = dict_s.get(s, 0) + 1
        return dict_s

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for s in set(ransomNote):
            if ransomNote.count(s) > magazine.count(s):
                return False
        return True


s = Solution()
print(s.canConstruct('a', 'b'))
print(s.canConstruct("aa", "ab"))
print(s.canConstruct("aa", "aab"))