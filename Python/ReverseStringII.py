"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""
class Solution_1:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        reverse = True
        start = 0
        len_s = len(s)
        while start < len_s:
            end = min(start+k, len_s)
            if reverse:
                res += s[start:end][::-1]
                reverse = False
            else:
                res += s[start:end]
                reverse = True
            start += k
        return res

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        Thoughts: split and join. python can handle slice safely
        """
        s = list(s)
        for i in range(0,len(s), 2*k):
            s[i:i+k] = s[i:i+k][::-1]
        return ''.join(s)

S = Solution()
s = "abcdefg"
k = 2
print(S.reverseStr(s,k))
s = "ab"
k = 3
print(S.reverseStr(s,k))
