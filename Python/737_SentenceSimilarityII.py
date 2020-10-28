"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sentence-similarity-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs) -> bool:
        def find(word):
            if word not in root:
                root[word] = word
            if root[word] != word:
                root[word] = find(root[word])
            return root[word]

        def union(p, q):
            rp, rq = find(p), find(q)
            if rp == rq:
                return False
            if rp != rq:
                root[rp] = rq
            return True

        root = dict()

        for p,q in pairs:
            union(p, q)
        # print(root)
        if len(words1) != len(words2):
            return False
        for w1, w2 in zip(words1, words2):
            if find(w1) != find(w2):
                return False
        return True

S = Solution()
words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]]
print(S.areSentencesSimilarTwo(words1, words2, pairs))
