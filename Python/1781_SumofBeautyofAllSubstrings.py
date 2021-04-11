"""
The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

 

Example 1:

Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
Example 2:

Input: s = "aabcbaa"
Output: 17
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters.
"""


from collections import Counter
class Solution:
    def beautySum(self, string: str) -> int:
        res = 0
        length = len(string)
        for i in range(length):
            counts = Counter()
            for j in range(i, length):
                counts[string[j]] += 1
                res += counts.most_common()[0][1] - counts.most_common()[-1][1]
        return res


from collections import Counter
class Solution:
    def beautySum(self, string: str) -> int:
        res = 0
        length = len(string)
        for i in range(length):
            counts = [0] * 26
            for j in range(i, length):
                key = string[j]
                counts[ord(key) - ord('a')] += 1
                lst = [i for i in counts if i > 0]
                res += max(lst) - min(lst)
        return res

S = Solution()
string = "aabcb"
print(S.beautySum(string))
string = "aabcbaa"
print(S.beautySum(string))