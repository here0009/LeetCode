"""
To some string S, we will perform some replacement operations that replace groups of letters with new ones (not necessarily the same size).

Each replacement operation has 3 parameters: a starting index i, a source word x and a target word y.  The rule is that if x starts at position i in the original string S, then we will replace that occurrence of x with y.  If not, we do nothing.

For example, if we have S = "abcd" and we have some replacement operation i = 2, x = "cd", y = "ffff", then because "cd" starts at position 2 in the original string S, we will replace it with "ffff".

Using another example on S = "abcd", if we have both the replacement operation i = 0, x = "ab", y = "eee", as well as another replacement operation i = 2, x = "ec", y = "ffff", this second operation does nothing because in the original string S[2] = 'c', which doesn't match x[0] = 'e'.

All these operations occur simultaneously.  It's guaranteed that there won't be any overlap in replacement: for example, S = "abc", indexes = [0, 1], sources = ["ab","bc"] is not a valid test case.

Example 1:

Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
Output: "eeebffff"
Explanation: "a" starts at index 0 in S, so it's replaced by "eee".
"cd" starts at index 2 in S, so it's replaced by "ffff".
Example 2:

Input: S = "abcd", indexes = [0,2], sources = ["ab","ec"], targets = ["eee","ffff"]
Output: "eeecd"
Explanation: "ab" starts at index 0 in S, so it's replaced by "eee". 
"ec" doesn't starts at index 2 in the original S, so we do nothing.
Notes:

0 <= indexes.length = sources.length = targets.length <= 100
0 < indexes[i] < S.length <= 1000
All characters in given inputs are lowercase letters.
"""
class Solution_1:
    def findReplaceString(self, s: str, indexes, sources, targets) -> str:
        res = ''
        index = 0
        len_search = len(indexes)
        in_s_t = sorted([(indexes[i],sources[i],targets[i]) for i in range(len_search)])
        start = 0
        print(in_s_t)
        for i in range(len_search):
            k,source,target = in_s_t[i]
            len_source = len(source)
            res += s[start:k]
            if s[k:k+len_source] == source:
                res += target
            else:
                res += s[k:k+len_source]
            start = k+len_source
        res += s[start:]
        return res

class Solution:
    def findReplaceString(self, s: str, indexes, sources, targets) -> str:
        #search from right to left, so the length differences of source and target won't be a problem
        in_s_t = sorted(zip(indexes,sources,targets), reverse = True)
        for k in range(len(in_s_t)):
            i,sc,tg = in_s_t[k]
            if s[i:i+len(sc)] == sc:
                s = s[:i] + tg + s[i+len(sc):]
        return s


S = Solution()
s = "abcd"
indexes = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]
print(S.findReplaceString(s,indexes,sources,targets))


s = "abcd"
indexes = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print(S.findReplaceString(s,indexes,sources,targets))

s = "vmokgggqzp"
indexes = [3,5,1]
sources = ["kg","ggq","mo"]
targets = ["s","so","bfr"]
print(S.findReplaceString(s,indexes,sources,targets))
# Output
# "vmossobfrkgggqzp"
# Expected
# "vbfrssozp"