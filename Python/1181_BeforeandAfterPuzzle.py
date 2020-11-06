"""
Given a list of phrases, generate a list of Before and After puzzles.

A phrase is a string that consists of lowercase English letters and spaces only. No space appears in the start or the end of a phrase. There are no consecutive spaces in a phrase.

Before and After puzzles are phrases that are formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the Before and After puzzles that can be formed by every two phrases phrases[i] and phrases[j] where i != j. Note that the order of matching two phrases matters, we want to consider both orders.

You should return a list of distinct strings sorted lexicographically.

 

Example 1:

Input: phrases = ["writing code","code rocks"]
Output: ["writing code rocks"]
Example 2:

Input: phrases = ["mission statement",
                  "a quick bite to eat",
                  "a chip off the old block",
                  "chocolate bar",
                  "mission impossible",
                  "a man on a mission",
                  "block party",
                  "eat my words",
                  "bar of soap"]
Output: ["a chip off the old block party",
         "a man on a mission impossible",
         "a man on a mission statement",
         "a quick bite to eat my words",
         "chocolate bar of soap"]
Example 3:

Input: phrases = ["a","b","a"]
Output: ["a"]
 

Constraints:

1 <= phrases.length <= 100
1 <= phrases[i].length <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/before-and-after-puzzle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        start_with = defaultdict(set)
        end_with = defaultdict(set)
        phrases = [tuple(p.split(' ')) for p in phrases]
        for i, phrase in enumerate(phrases):
            s, e = phrase[0], phrase[-1]
            start_with[s].add((phrase, i))
            end_with[e].add((phrase, i))
        # print(start_with, end_with)
        res = set()
        for i, phrase in enumerate(phrases):
            s, e = phrase[0], phrase[-1]
            for q, j in end_with[s]:
                if i != j:
                    res.add(' '.join(q[:-1] + phrase))
            for q, j in start_with[e]:
                if i != j:
                    res.add(' '.join(phrase + q[1:]))
        return sorted(list(res))


# 作者：intoloop
# 链接：https://leetcode-cn.com/problems/before-and-after-puzzle/solution/python-by-intoloop-31/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        headDic,tailDic=collections.defaultdict(set),collections.defaultdict(set)
        res=set()
        phrases=[i.split() for i in phrases]
        for i, words in enumerate(phrases):
            headDic[words[0]].add(i)
            tailDic[words[-1]].add(i)
        
        for tail in tailDic:
            tailIndex=tailDic[tail]
            headIndex=headDic[tail]
            for i in tailIndex:
                for j in headIndex:
                    if i!=j:
                        res.add(' '.join(phrases[i]+phrases[j][1:]))
        return sorted(list(res))


from collections import defaultdict
class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        start_with = defaultdict(set)
        end_with = defaultdict(set)
        phrases = [p.split(' ') for p in phrases]
        for i, phrase in enumerate(phrases):
            s, e = phrase[0], phrase[-1]
            start_with[s].add(i)
            end_with[e].add(i)
        # print(start_with, end_with)
        res = set()
        for p in end_with.keys():
            for i in end_with[p]:
                for j in start_with[p]:
                    if i != j:
                        res.add(' '.join(phrases[i] + phrases[j][1:]))
        return sorted(list(res))



S = Solution()
phrases = ["writing code","code rocks"]
print(S.beforeAndAfterPuzzles(phrases))
phrases = ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"]
print(S.beforeAndAfterPuzzles(phrases))
phrases = ["a","b","a"]
print(S.beforeAndAfterPuzzles(phrases))