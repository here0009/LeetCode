"""
Given a list of strings, you need to find the longest uncommon subsequence among them. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
"""

"""
Pay attention to the definiton of subsequence, its not the same as usual.
"""
class Solution:
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        
        str_dict = dict()
        for string in strs:
            str_dict[string] = str_dict.get(string, 0) + 1

        l_to_s = sorted(str_dict.keys(), key = len)[::-1] #long to short list of str_dict.keys
        # print(l_to_s)
        for index, key in enumerate(l_to_s):
            if str_dict[key] == 1:
                if index == 0:
                    return len(key)
                index_tmp = index-1
                break_flag = False
                while index_tmp >= 0:
                    if not self.isSubsequence(key, l_to_s[index_tmp]):
                        index_tmp-=1
                    else:
                        break_flag = True
                        break
                if not break_flag: 
                    return len(key)
        return -1
    def isSubsequence(self, subseq, seq):
        pre_pos = 0
        for letter in subseq:
            pos = seq.find(letter, pre_pos)
            if pos == -1:
                return False
            else:
                pre_pos = pos + 1
        return True


s = Solution()
test = ["aaa","aaa","aa"]
print(s.findLUSlength(test))
# test = sorted(test)[::-1]
# print(test)
test = ["aba", "cdc", "eae"]
print(s.findLUSlength(test))
test = ["aabbcc", "aabbcc","c"]
print(s.findLUSlength(test))

test = ["aabbcc", "aabbcc","cb","abc"]
print(s.findLUSlength(test))