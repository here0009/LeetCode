"""
有个内含单词的超大文本文件，给定任意两个单词，找出在这个文件中这两个单词的最短距离(相隔单词数)。如果寻找过程在这个文件中会重复多次，而每次寻找的单词不同，你能对此优化吗?

示例：

输入：words = ["I","am","a","student","from","a","university","in","a","city"], word1 = "a", word2 = "student"
输出：1
提示：

words.length <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-closest-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
from typing import List
class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:

        word_idx_list = defaultdict(list)
        for i, v in enumerate(words):
            word_idx_list[v].append(i)

        w1_list = word_idx_list[word1]
        w2_list = [-float('inf')] + word_idx_list[word2] + [float('inf')]
        j = 0
        res = float('inf')
        for i_idx in w1_list:
            j = 0
            while j < len(w2_list) and w2_list[j] < i_idx: 
                j += 1
            res = min(res, i_idx - w2_list[j - 1], w2_list[j] - i_idx)
        return res


S = Solution()
words = ["I","am","a","student","from","a","university","in","a","city"]
word1 = "a"
word2 = "student"
print(S.findClosest(words, word1, word2))
