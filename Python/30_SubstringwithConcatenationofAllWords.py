"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""


from collections import Counter
class Solution:
    def findSubstring(self, string: str, words):
        def dfs(index, visited):
            # print(index,visited)
            if visited == word_counter:
                return True
            if index >= len_string:
                return False
            word = string[index: index + word_size]
            visited[word] += 1
            if visited[word] > word_counter[word]:
                return False
            return dfs(index + word_size, visited)

        if not words:
            return None
        word_size = len(words[0])
        word_counter = Counter(words)
        len_words = word_size*len(words)
        len_string = len(string)

        res = []
        for i in range(len_string - len_words + 1):
            # print(i)
            if dfs(i, Counter()):
                res.append(i)
        return res

from collections import Counter
class Solution:
    def findSubstring(self, string: str, words):
        if not words:
            return None
        word_size = len(words[0])
        word_counter = Counter(words)
        length = len(words)
        len_words = word_size*length
        len_string = len(string)
        res = []
        for start in range(word_size):
            end = start + len_words
            if end > len_string:
                break
            visited = Counter()
            counts, tmp = 0, start
            while counts < length:
                visited[string[tmp: tmp + word_size]] += 1
                counts += 1
                tmp += word_size
            if visited == word_counter:
                res.append(start)
            # print(start, visited)
            while end < len_string:
                pre_word, next_word = string[start:start+word_size], string[end:end+word_size]
                visited[pre_word] -= 1
                if visited[pre_word] == 0:
                    del visited[pre_word]
                visited[next_word] += 1
                start += word_size
                end += word_size
                if visited == word_counter:
                    res.append(start)
                # print(start, visited)
        return res
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/discuss/13669/99ms-Python-O(kmn)-Solution
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words):
        c = Counter(words)
        m = len(words)
        n = len(words[0])
        res = []
        for k in range(n):
            left = k
            subd = Counter()
            count = 0
            #Loop over the string
            for j in range(k, len(s) - n + 1, n):
                word = s[j:j+n]
                if word in c:
                    subd[word] += 1
                    count += 1
                    while subd[word] > c[word]:
                        subd[s[left:left+n]] -= 1
                        left += n
                        count -= 1
                    if count == m:
                        res.append(left)
                else:
                    left = j + n
                    subd = Counter()
                    count = 0
        return res

S = Solution()
string = "barfoothefoobarman"
words = ["foo","bar"]
print(S.findSubstring(string, words))
string = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(S.findSubstring(string, words))

string ="wordgoodgoodgoodbestword"
words =["word","good","best","good"]
print(S.findSubstring(string, words))