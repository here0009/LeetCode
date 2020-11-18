"""
Given a string S, return the number of substrings that have only one distinct letter.

 

Example 1:

Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
Example 2:

Input: S = "aaaaaaaaaa"
Output: 55
 

Constraints:

1 <= S.length <= 1000
S[i] consists of only lowercase English letters.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def countLetters(self, string: str) -> int:
        index, counts, res = 0, 0, 0
        curr = None
        length = len(string)
        while index < length:
            if string[index] == curr:
                counts += 1
            else:
                res += (counts + 1)*counts//2
                counts = 1
                curr = string[index]
            index += 1
        res += (counts + 1)*counts//2
        return res

S = Solution()
string = "aaaba"
print(S.countLetters(string))
string = "aaaaaaaaaa"
print(S.countLetters(string))

