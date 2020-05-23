"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from collections import Counter
from collections import defaultdict

class Solution_1:
    def countertoStr(self,counter):
        res = ''
        for key in sorted(counter.keys()):
            res += key
            res += str(counter[key])
        return res

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = dict()
        for string in strs:
            tmp = Counter(string)
            tmp = self.countertoStr(tmp)
            if tmp in res:
                res[tmp].append(string)
            else:
                res[tmp] = [string]
        return [value for value in res.values()]

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for string in strs:
            res[''.join(sorted(string))].append(string)
        return [value for value in res.values()]


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))

