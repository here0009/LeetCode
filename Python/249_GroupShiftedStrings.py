"""
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/group-shifted-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def groupStrings(self, strings):
        """
        Thoughts: the strings that got the same length and letter diff intervals can be grouped together
        """
        lst = defaultdict(list)
        for string in strings:
            length, diff_list = len(string), []
            for i in range(1, length):
                diff_list.append((ord(string[i])-ord(string[i-1])) % 26)
            lst[(length, tuple(diff_list))].append(string)
        return list(lst.values())

S = Solution()
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
print(S.groupStrings(strings))