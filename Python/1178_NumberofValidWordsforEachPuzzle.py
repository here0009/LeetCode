"""
With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
 

Example :

Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
 

Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] are English lowercase letters.
Each puzzles[i] doesn't contain repeated characters.
"""


from typing import List
from string import ascii_lowercase
from collections import defaultdict
from copy import deepcopy
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        TLE 9/10
        """
        letter_in = defaultdict(set)
        for i, word in enumerate(words):
            for letter in set(word):
                letter_in[letter].add(i)

        res = [0] * len(puzzles)
        for i, puzzle in enumerate(puzzles):
            i_set = deepcopy(letter_in[puzzle[0]])  # stupid mistake
            forbid = set(ascii_lowercase) - set(puzzle)
            for letter in forbid:
                i_set -= letter_in[letter]
                if not i_set:
                    break
            # print(puzzle, i_set, forbid)
            res[i] = len(i_set)
        return res

S = Solution()
words = ["aaaa","asas","able","ability","actt","actor","access"]
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
print(S.findNumOfValidWords(words, puzzles))
words = ["apple","pleas","please"]
puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
print(S.findNumOfValidWords(words, puzzles))
# Output
# [0,1,1,0,0]
# Expected
# [0,1,3,2,0]