"""
You are given a binary string s. You are allowed to perform two types of operations on the string in any sequence:

Type-1: Remove the character at the start of the string s and append it to the end of the string.
Type-2: Pick any character in s and flip its value, i.e., if its value is '0' it becomes '1' and vice-versa.
Return the minimum number of type-2 operations you need to perform such that s becomes alternating.

The string is called alternating if no two adjacent characters are equal.

For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
 

Example 1:

Input: s = "111000"
Output: 2
Explanation: Use the first operation two times to make s = "100011".
Then, use the second operation on the third and sixth elements to make s = "101010".
Example 2:

Input: s = "010"
Output: 0
Explanation: The string is already alternating.
Example 3:

Input: s = "1110"
Output: 1
Explanation: Use the second operation on the second element to make s = "1010".
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""


class Solution:
    def minFlips(self, string: str) -> int:
        """
        TLE
        """

        def calc(s2):
            diff = sum([s2[i] != target[i] for i in range(length)])
            return min(diff, length - diff)


        length = len(string)
        if length == 1:
            return 0
        target = '01' * (length // 2)
        if length % 2 == 1:
            target += '0'
        res = calc(string)
        for i in range(1, length):
            s2 = string[i:] + string[:i]
            if s2[0] == s2[-1]:
            # print(s2, calc(s2))
                res = min(res, calc(s2))
        return res


class Solution:
    def minFlips(self, string: str) -> int:

        length = len(string)
        string = string * 2
        s1 = '10' * (2 * length)
        s2 = '01' * (2 * length)
        score1 = sum([s1[i] != string[i] for i in range(length)])
        score2 = sum([s2[i] != string[i] for i in range(length)])
        res = min(score1, score2)
        for i in range(length, 2 * length):
            score1 += (s1[i] != string[i])
            score2 += (s2[i] != string[i])
            score1 -= (s1[i - length] != string[i - length])
            score2 -= (s2[i - length] != string[i - length])
            res = min(res, score1, score2)
        return res


S = Solution()
string = "111000"
print(S.minFlips(string))
string = "010"
print(S.minFlips(string))
string = "1110"
print(S.minFlips(string))
string = "01001001101"
# 01001101010 2 
print(S.minFlips(string))
# 输出：
# 5
# 预期：
# 2