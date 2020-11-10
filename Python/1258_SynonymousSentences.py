"""
Given a list of pairs of equivalent words synonyms and a sentence text, Return all possible synonymous sentences sorted lexicographically.
 

Example 1:

Input:
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]],
text = "I am happy today but was sad yesterday"
Output:
["I am cheerful today but was sad yesterday",
"I am cheerful today but was sorrow yesterday",
"I am happy today but was sad yesterday",
"I am happy today but was sorrow yesterday",
"I am joy today but was sad yesterday",
"I am joy today but was sorrow yesterday"]
Example 2:

Input: synonyms = [["happy","joy"],["cheerful","glad"]], text = "I am happy today but was sad yesterday"
Output: ["I am happy today but was sad yesterday","I am joy today but was sad yesterday"]
Example 3:

Input: synonyms = [["a","b"],["c","d"],["e","f"]], text = "a c e"
Output: ["a c e","a c f","a d e","a d f","b c e","b c f","b d e","b d f"]
Example 4:

Input: synonyms = [["a","QrbCl"]], text = "d QrbCl ya ya NjZQ"
Output: ["d QrbCl ya ya NjZQ","d a ya ya NjZQ"]
 

Constraints:

0 <= synonyms.length <= 10
synonyms[i].length == 2
synonyms[i][0] != synonyms[i][1]
All words consist of at most 10 English letters only.
text is a single space separated sentence of at most 10 words.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/synonymous-sentences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def generateSentences(self, synonyms, text: str):
        def find(w):
            if w not in root:
                root[w] = w
            if root[w] != w:
                root[w] = find(root[w])
            return root[w]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri == rj:
                return False
            root[ri] = rj
            return True

        root = dict()
        dictionary = defaultdict(set)
        words = set()
        for w1, w2 in synonyms:
            words |= set([w1, w2])
            union(w1, w2)

        for word in words:
            dictionary[find(word)].add(word)

        res = [[]]
        text_list = text.split(' ')
        for word in text_list:
            rw = find(word)
            if rw in dictionary:
                app = dictionary[rw]
            else:
                app = set([word])
            res2 = []
            for lst in res:
                for w in app:
                    res2.append(lst + [w])
            res = res2
        return sorted([' '.join(w) for w in res])

S = Solution()
synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]
text = "I am happy today but was sad yesterday"
print(S.generateSentences(synonyms, text))
synonyms = [["happy","joy"],["cheerful","glad"]]
text = "I am happy today but was sad yesterday"
print(S.generateSentences(synonyms, text))
synonyms = [["a","b"],["c","d"],["e","f"]]
text = "a c e"
print(S.generateSentences(synonyms, text))

synonyms = [["a","QrbCl"]]
text = "d QrbCl ya ya NjZQ"
print(S.generateSentences(synonyms, text))