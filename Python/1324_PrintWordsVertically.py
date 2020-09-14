"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

 

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 

Constraints:

1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.
"""


class Solution:
    def printVertically(self, s: str):
        words = s.split()
        max_len = max(len(w) for w in words)
        res = []
        for i in range(len(words)):
            w = words[i]
            if len(w) < max_len:
                words[i] = w + (max_len - len(w))*' '
        for i in range(max_len):
            tmp = ''
            for j in range(len(words)):
                tmp += words[j][i]
            res.append(tmp.rstrip())
        return res

# https://leetcode.com/problems/print-words-vertically/discuss/484283/Python-zip_longest-with-steps
# https://www.geeksforgeeks.org/python-itertools-zip_longest/
import itertools
def printVertically(self, s):
    columns = s.split()
    rows = itertools.zip_longest(*columns, fillvalue=' ')
    return [''.join(row).rstrip() for row in rows]


S = Solution()
s = "HOW ARE YOU"
print(S.printVertically(s))
s = "TO BE OR NOT TO BE"
print(S.printVertically(s))
s = "CONTEST IS COMING"
print(S.printVertically(s))