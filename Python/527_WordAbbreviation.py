"""
Given an array of n distinct non-empty strings, you need to generate minimal possible abbreviations for every word following rules below.

Begin with the first character and then the number of characters abbreviated, which followed by the last character.
If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.
If the abbreviation doesn't make the word shorter, then keep it as original.
Example:
Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
Note:
Both n and the length of each word will not exceed 400.
The length of each word is greater than 1.
The words consist of lowercase English letters only.
The return answers should be in the same order as the original array.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-abbreviation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# from collections import defacultdict
from collections import Counter
class TreeNode:
    def __init__(self):
        self.val = Counter() # the rest length of word in a Counter
        self.children = dict()


class Trie:
    def __init__(self, root):
        self.root = root

    def add(self, word):
        node = self.root
        length = len(word)
        for c in word:
            if c not in node.children:
                node.children[c] = TreeNode()
            node = node.children[c]
            length -= 1
            node.val[length] += 1
        node.children['$'] = 1

    def search(self, word):
        #  find the unique prefix for word, the length of the prefix is >= 2
        node = self.root
        pre = ''
        length = len(word)
        counts = 0
        for c in word:
            if c in node.children:
                node = node.children[c]
                pre += c
                counts += 1
                if counts > 1 and node.val[length - counts] == 1:
                    break
        return pre


class Solution:
    def wordsAbbreviation(self, words):
        root = TreeNode()
        tree = Trie(root)
        for word in words:
            word = word[-1] + word[:-1]
            tree.add(word)
        res = []
        for word in words:
            word = word[-1] + word[:-1]
            prefix = tree.search(word)
            length = len(word) - len(prefix)
            # print(word, prefix, length)
            if length > 1:
                word = prefix+str(length)
            res.append(word[1:] + word[0])
        return res

# 作者：lml2020
# 链接：https://leetcode-cn.com/problems/word-abbreviation/solution/yi-chong-bi-jiao-zhi-guan-ke-du-xing-hao-de-python/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


from collections import defaultdict
class Solution:
    def wordsAbbreviation(self, lst):
        def abbr(word, target_len):
            if len(word) <= target_len:
                return word
            else:
                return word[:target_len-2] + str(len(word) - target_len + 1) + word[-1]

        def recur(words, target_len):
            abbr_dict = defaultdict(list)
            for word in words:
                abbr_dict[abbr(word, target_len)].append(word)

            res = dict()
            remaining = []
            for key, values in abbr_dict.items():
                if len(abbr_dict[key]) == 1:
                    res[values[0]] = key
                else:
                    remaining.extend(values)
            return res, remaining

        words = lst
        res = dict()
        target_len = 3  # target_len is initialized as 3, and prefix is word[:target_len-2], the length is 1
        while words:
            tmp_res, words = recur(words, target_len)
            res.update(tmp_res)
            target_len += 1

        res_list = [res[word] for word in lst]
        return res_list


S = Solution()
words = ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
print(S.wordsAbbreviation(words))
words = ["meet","met"]
print(S.wordsAbbreviation(words))
# 输出：
# ["meet","met"]
# 预期结果：
# ["m2t","met"]