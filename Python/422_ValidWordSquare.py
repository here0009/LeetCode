"""
Given a sequence of words, check whether it forms a valid word square.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:
The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
[
  "abcd",
  "bnrt",
  "crmy",
  "dtye"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".

Therefore, it is a valid word square.
Example 2:

Input:
[
  "abcd",
  "bnrt",
  "crm",
  "dt"
]

Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".

Therefore, it is a valid word square.
Example 3:

Input:
[
  "ball",
  "area",
  "read",
  "lady"
]

Output:
false

Explanation:
The third row reads "read" while the third column reads "lead".

Therefore, it is NOT a valid word square.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-word-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def validWordSquare(self, words) -> bool:
        length = len(words)
        len_w = max(len(word) for word in words)
        c_words = ['' for _ in range(len_w)]
        for i in range(length):
            for j in range(len(words[i])):
                c_words[j] += words[i][j]
        # print(c_words)
        if len(c_words) != length:
            return False
        return all(c_words[i] == words[i] for i in range(length))



# 作者：mnm135
# 链接：https://leetcode-cn.com/problems/valid-word-square/solution/bu-yong-bu-wei-tian-jia-tiao-jian-qu-chu-bu-ke-nen/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True

    


S = Solution()
words = ["abcd","bnrt","crmy","dtye"]
print(S.validWordSquare(words))
words = ["abcd","bnrt","crm","dt"]
print(S.validWordSquare(words))
words = ["ball","area","read","lady"]
print(S.validWordSquare(words))