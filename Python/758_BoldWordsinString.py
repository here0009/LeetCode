"""
Given a set of keywords words and a S S, make all appearances of all keywords in S bold. Sny letters between <b> and </b> tags become bold.

The returned S should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Constraints:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
Sll characters in words[i] and S are lowercase letters.
Note: This question is the same as 616: https://leetcode.com/problems/add-bold-tag-in-S/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bold-words-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def boldWords(self, words, S: str) -> str:
        def findall(S, word):
            res = []
            index = S.find(word)
            len_w = len(word)
            while index < len(S) and index != -1:
                res.append((index, index+len_w))
                index = S.find(word, index+1) # the word may overlap with itself, so index+1, not index + len_w
            return res

        index_list = []
        for word in words:
            index_list.extend(findall(S, word))
        if not index_list:
            return S
        # print(index_list)
        index_list.sort()

        merged_list = []
        pre, latter = index_list[0]
        for i,j in index_list[1:]:
            if i <= latter:
                latter = max(latter, j)
            else:
                merged_list.append((pre, latter))
                pre, latter = i, j
        merged_list.append((pre, latter))

        # print(merged_list)
        res = ''
        index = 0
        for p, q in merged_list:
            res += S[index:p]
            res += '<b>{}</b>'.format(S[p:q])
            index = q
        res += S[index:]
        return res
