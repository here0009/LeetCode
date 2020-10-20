"""
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sentence-screen-fitting
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def wordsTyping(self, sentence, rows: int, cols: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def update(i,j):
            for word in sentence:
                if j + len(word) > cols:
                    i += 1
                    j = 0
                j += len(word) + 1
            return i,j

        if max(len(word) for word in sentence) > cols:
            return 0
        i, j = 0,0
        res = -1
        # print('++++++++++++',sentence, rows, cols)
        while i < rows:
            res += 1
            i,j = update(i,j)
            # print(i,j)
        return res


# https://leetcode-cn.com/problems/sentence-screen-fitting/solution/c-dpjie-fa-zhua-zhu-ci-chang-he-ci-shu-shao-de-te-/
class Solution:
    def wordsTyping(self, sentence, rows: int, cols: int) -> int:
        """
        Thoughts:
        update each sentence got TLE, 
        so we update the state of each row. 
        record the start word index of each row and the sentence we can got from than index in one row
        """
        len_words = [len(word) for word in sentence]
        length = len(len_words)
        next_col = [0]*length # after put one row, next start index of sentence
        dp = [0]*length  # record how many sentence we can put in one row start with sentence[i]

        for i in range(length):
            counts = 0
            w_i = i  # word index
            j = cols
            while j >= len_words[w_i]:
                j -= len_words[w_i] + 1
                w_i += 1
                if w_i == length:
                    counts += 1
                    w_i = 0
            dp[i] = counts
            next_col[i] = w_i

        w, row, res = 0, 0, 0  # index of word, res
        while row < rows:
            w, v = next_col[w], dp[w]
            res += v
            row += 1
        return res




S = Solution()
rows = 2
cols = 8
sentence = ["hello", "world"]
print(S.wordsTyping(sentence, rows, cols))
rows = 3
cols = 6
sentence = ["a", "bcd", "e"]
print(S.wordsTyping(sentence, rows, cols))
rows = 4
cols = 5
sentence = ["I", "had", "apple", "pie"]
print(S.wordsTyping(sentence, rows, cols))
sentence = ["f","p","a"]
rows = 8
cols = 7
print(S.wordsTyping(sentence, rows, cols))
# # 输出：
# # 8
# # 预期结果：
# # 10
sentence = ["try","to","be","better"]
rows =10000
cols = 9001
print(S.wordsTyping(sentence, rows, cols))