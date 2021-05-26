"""
Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.

 

Example 1:

Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.
Example 2:

Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.
Example 3:

Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.
 

Constraints:

1 <= s.length <= 100
s[i] is either '0' or '1'.
"""


class Solution:
    def checkZeroOnes(self, string: str) -> bool:
        zeros, ones = 0, 0
        tmp_0, tmp_1 = 0, 0
        pre = None
        for s in string:
            if s == '0':
                if pre == '0':
                    tmp_0 = tmp_0 + 1
                else:
                    tmp_0 = 1
                tmp_1 = 0
            else:
                if pre == '1':
                    tmp_1 = tmp_1 + 1
                else:
                    tmp_1 = 1
                tmp_0 = 0
            pre = s
            zeros = max(zeros, tmp_0)
            ones = max(ones, tmp_1)
        # print(zeros, ones)
        return True if ones > zeros else False


S = Solution()
string = "1101"
print(S.checkZeroOnes(string))
string = "111000"
print(S.checkZeroOnes(string))
string = "110100010"
print(S.checkZeroOnes(string))