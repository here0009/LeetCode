"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"
Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]

Output: 
"a"
Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""
class Solution:
    def findLongestWord(self, s: str, d) -> str:
        d = sorted(d, key = lambda x: (-len(x),x))
        len_s = len(s)
        for word in d:
            index_s = 0
            index_w = 0
            while index_w < len(word) and index_s < len_s:
                if s[index_s] == word[index_w]:
                    index_w += 1
                index_s += 1
            if index_w == len(word):
                return word
        return ''

class Solution:
    def findLongestWord(self, s: str, d) -> str:
        d = sorted(d, key = lambda x: (-len(x),x))
        for word in d:
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ''

S = Solution()
s = "abpcplea"
d = ["ale","apple","monkey","plea"]
print(S.findLongestWord(s,d))

s = "abpcplea"
d = ["a","b","c"]
print(S.findLongestWord(s,d))

s ="bab"
d = ["ba","ab","a","b"]
print(S.findLongestWord(s,d))


