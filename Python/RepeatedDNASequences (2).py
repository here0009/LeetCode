"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution:
    def findRepeatedDnaSequences(self, s: str):
        tmp = s[:10]
        c_str = {tmp:1}
        for i in range(len(s)-10):
            # print(tmp)
            tmp = tmp[1:] + s[i+10]
            c_str[tmp] = c_str.get(tmp,0) + 1

        # print(c_str)
        return [key for key in c_str.keys() if c_str[key]>1]


class Solution:
    def findRepeatedDnaSequences(self, s: str):
        c_str = {}
        for i in range(len(s)-9):
            # print(tmp)
            tmp = s[i:i+10]
            c_str[tmp] = c_str.get(tmp,0) + 1

        # print(c_str)
        return [key for key in c_str.keys() if c_str[key]>1]

S = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(S.findRepeatedDnaSequences(s))