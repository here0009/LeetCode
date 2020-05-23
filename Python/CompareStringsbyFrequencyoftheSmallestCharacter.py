"""
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.
"""
from collections import Counter
from bisect import bisect_right
from bisect import bisect_left
class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(string):
            sCounter = Counter(string)
            min_key = min(sCounter.keys())
            return sCounter[min_key]

        q_num = [f(q) for q in queries]
        w_num = sorted([f(w) for w in words])
        # print(q_num)
        # print(w_num)
        res = []
        len_w = len(w_num)
        for q in q_num:
            # print(q,bisect_left(w_num, q),bisect_right(w_num, q))
            res.append(len_w - bisect_right(w_num, q))
        return res

s = Solution()
queries = ["cbd"]
words = ["zaaaz"]
print(s.numSmallerByFrequency(queries, words))

queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]
print(s.numSmallerByFrequency(queries, words))