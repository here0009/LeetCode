"""
Given a group of two strings, you need to find the longest uncommon subsequence of this group of two strings. The longest uncommon subsequence is defined as the longest subsequence of one of these strings and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters without changing the order of the remaining elements. Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings, and the output needs to be the length of the longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.

Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 
Note:

Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings.
"""
"""
Thoughts:
find the longest common subsequence, then use the two input sequences to find the longest uncommon subsequenc.
"""
class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        len_a = len(a)
        len_b = len(b)
        #make a the longer one
        if len_a < len_b:
            a, b = b, a
            len_a, len_b = len_b, len_a
        longestCommonSub = ""
        for index_b, letter_b in enumerate(b):
            # print(longestCommonSub)
            # print(letter_b)
            pos_a = a.find(letter_b)
            tmp_string = letter_b
            if pos_a != -1:
                pos_a += 1
                pos_b = index_b + 1
                while pos_b < len_b and pos_a < len_a:
                    if b[pos_b] == a[pos_a]:
                        tmp_string += b[pos_b]
                        pos_b += 1
                        pos_a += 1
                    else:
                        break
                if len(tmp_string) > len(longestCommonSub):
                    longestCommonSub = tmp_string
        a_start = a.find(longestCommonSub)
        b_start = b.find(longestCommonSub)
        len_lcb = len(longestCommonSub)
        res = max(a_start, b_start, len_a-len_lcb-a_start, len_b-len_lcb-b_start)
        return res

"""
Thoughts:
Got the wrong idea.
The problem is about the longest uncommon subsequence, not the input sequence minus the longest common subsequenc.
It is pretty strange, because the longest uncommon subsequence of two string is either the longer one of the input sequence or -1
"""
class Solution_1:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))

s = Solution()
a = "aba"
b = "cdc"
print(s.findLUSlength(a, b))
a = "ababbbb"
b = "cdcbbcadrferwe"
print(s.findLUSlength(a, b))
a = "aefawfawfawfaw"
b = "aefawfeawfwafwaef"