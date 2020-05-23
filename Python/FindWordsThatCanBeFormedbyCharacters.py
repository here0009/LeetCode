"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""
from collections import Counter
class Solution:
    def countCharacters(self, words, chars):
        res = 0
        c_counter = Counter(chars)
        for word in words:
            w_counter = Counter(word)
            if  len(w_counter.keys() - c_counter.keys()) == 0:
                for key in w_counter.keys():
                    if w_counter[key] > c_counter[key]:
                        break
                else:
                    res += len(word)
        return res

s = Solution()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(s.countCharacters(words, chars))

words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
print(s.countCharacters(words, chars))