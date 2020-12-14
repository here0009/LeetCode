"""
Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

Each character is decoded as one digit (0 - 9).
Every pair of different characters they must map to different digits.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on left side (words) will equal to the number on right side (result). 
Return True if the equation is solvable otherwise return False.

 

Example 1:

Input: words = ["SEND","MORE"], result = "MONEY"
Output: true
Explanation: Map 'S'-> 9, 'E'->5, 'N'->6, 'D'->7, 'M'->1, 'O'->0, 'R'->8, 'Y'->'2'
Such that: "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
Example 2:

Input: words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
Output: true
Explanation: Map 'S'-> 6, 'I'->5, 'X'->0, 'E'->8, 'V'->7, 'N'->2, 'T'->1, 'W'->'3', 'Y'->4
Such that: "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
Example 3:

Input: words = ["THIS","IS","TOO"], result = "FUNNY"
Output: true
Example 4:

Input: words = ["LEET","CODE"], result = "POINT"
Output: false
 

Constraints:

2 <= words.length <= 5
1 <= words[i].length, result.length <= 7
words[i], result contains only upper case English letters.
Number of different characters used on the expression is at most 10.
"""


from typing import List
from itertools import permutations
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        def backTrack(cum, index):
            print(cum, index)
            if index == len_w:
                return cum == 0
            keys = set()
            for word in words:
                if index >= len(word):
                    break
                w = word[index]
                if w in self.w_dict:
                    cum += self.w_dict[w]
                else:
                    keys.add(w)

            r = result[index]
            if len(self.nums) < len(keys) + int(r not in self.w_dict):
                return False
            if not keys:
                cum, rmd = divmod(cum, 10)
                if r in self.w_dict:
                    if self.w_dict[r] == rmd:
                        if backTrack(cum, index + 1):
                            return True
                else:
                    if rmd in self.nums:
                        self.nums.remove(rmd)
                        self.w_dict[r] = rmd
                        if backTrack(cum, index + 1):
                            return True
                        self.nums.add(rmd)
                return False


            keys = list(keys)
            nums = list(self.nums)
            print(keys, nums)
            for perm in permutations(nums, len(keys)):
                print(perm)
                for i, v in enumerate(keys):
                    self.w_dict[v] = perm[i]
                    cum += perm[i]
                cum, rmd = divmod(cum, 10)
                self.nums -= set(perm)
                if r in self.w_dict:
                    if self.w_dict[r] == rmd:
                        if backTrack(cum, index + 1):
                            return True
                else:
                    if rmd in self.nums:
                        self.nums.remove(rmd)
                        self.w_dict[r] = rmd
                        if backTrack(cum, index + 1):
                            return True
                        self.nums.add(rmd)
                self.nums |= set(perm)
            return False

        words = sorted([word[::-1] for word in words], key=len, reverse=True)
        result = result[::-1]
        if len(words[0]) > len(result):
            return False
        self.nums = set(range(10))
        len_w = len(result)
        self.w_dict = dict()
        return backTrack(0, 0)

S = Solution()
words = ["SEND","MORE"]
result = "MONEY"
print(S.isSolvable(words, result))
# words = ["SIX","SEVEN","SEVEN"]
# result = "TWENTY"
# print(S.isSolvable(words, result))
# words = ["THIS","IS","TOO"]
# result = "FUNNY"
# print(S.isSolvable(words, result))
# words = ["LEET","CODE"]
# result = "POINT"
# print(S.isSolvable(words, result))