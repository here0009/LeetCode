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
            i_set = deepcopy(letter_in[puzzle[0]])  # stupid mistake, we should use copy/deepcopy because i_set might change during the iteration
            forbid = set(ascii_lowercase) - set(puzzle)
            for letter in forbid:
                i_set -= letter_in[letter]
                if not i_set:
                    break
            # print(puzzle, i_set, forbid)
            res[i] = len(i_set)
        return res


from typing import List
from collections import defaultdict
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        use bits to represent word and puzzle, so each of them can be represented as a bit of max len == 26
        TLE 9/10
        """
        def bitfy(word: str) -> int:
            """
            return the bit representation of word
            """
            num = 0
            for c in set(word):
                num = num | (1 <<(ord(c) - ord('a')))
            return num

        len_p = len(puzzles)
        letters = defaultdict(list)
        w_nums = []
        for i, word in enumerate(words):
            for c in set(word):
                letters[c].append(i)
            w_nums.append(bitfy(word))

        # print(bin(num) for num in w_nums)
        # print(letters)
        res = [0] * len_p
        for i, puzzle in enumerate(puzzles):
            lst = letters[puzzle[0]]
            p_num = bitfy(puzzle)
            for idx in lst:
                if p_num == p_num | w_nums[idx]:
                    res[i] += 1
        return res



from typing import List
from collections import defaultdict
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        use bits to represent word and puzzle, so each of them can be represented as a bit of max len == 26
        TLE
        """
        len_p = len(puzzles)
        letters = defaultdict(list)
        w_nums = []
        for i, word in enumerate(words):
            num = 0
            for c in set(word):
                num |= (1 <<(ord(c) - ord('a')))
                letters[c].append(i)
            w_nums.append(num)

        res = [0] * len_p
        for i, puzzle in enumerate(puzzles):
            lst = letters[puzzle[0]]
            p_num = 0
            for c in puzzle:
                p_num |= (1 <<(ord(c) - ord('a')))
            for idx in lst:
                if p_num == p_num | w_nums[idx]:
                    res[i] += 1
        return res


from typing import List
from collections import Counter
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        we should solve the problem based on the features of the parmaters
        both words and puzzles are around 1E4 ~ 1E5, a method of complexity O(len(words) * len(puzzles)) probably won't pass all the test
        but we can find each puzzle is very short : 7
        so the letter combinations in puzzle is at most 7 * 7 = 49 (assuming every letter unique)
        and the problem can be tackled in 49*O(len(puzzles)) 
        we need to store the letter information of word in a Counter
        """
        def bitfy(word: str) -> int:
            """
            return the bit representation of word
            """
            num = 0
            for c in set(word):
                num = num | (1 << (ord(c) - ord('a')))
            return num

        counts = Counter()
        len_p = len(puzzles)
        for word in words:
            counts[bitfy(word)] += 1

        res = [0] * len_p
        for i, puzzle in enumerate(puzzles):
            bfs = [puzzle[0]]
            for j in puzzle[1:]:  # all the sub_puzzles of puzzle
                bfs.extend([tmp + j for tmp in bfs])
            for sub_puzzle in bfs:
                res[i] += counts[bitfy(sub_puzzle)]
        return res

# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/discuss/372145/Python-Bit-manipulation-detailed-explanation
from typing import List
from collections import Counter
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        """
        further more, we do not need generate sub_puzzle using bfs.
        we can generate directly using bit operation.
        let: sub_bit = origin_bit = mask,
        then iterate : sub_bit = (sub_bit - 1) & origin_bit
        until sub_bit == 0
        the sub_bits are the bit representation of sub_puzzles
        when sub_bit - 1, it convert lowest bit to 0 and all bit right to it to 1
        so if there's any 1 in the corresponding postion of origin_bit it will be recovered.
        using this method we can generate evey sub_bit of the orgin_bit
        """
        def bitfy(word: str) -> int:
            """
            return the bit representation of word
            """
            num = 0
            for c in set(word):
                num = num | (1 << (ord(c) - ord('a')))
            return num

        counts = Counter()
        len_p = len(puzzles)
        for word in words:
            counts[bitfy(word)] += 1

        res = [0] * len_p
        for i, puzzle in enumerate(puzzles):
            first_bit = 1 << (ord(puzzle[0]) - ord('a'))
            origin_bit = bitfy(puzzle)
            sub_bit = origin_bit
            while sub_bit != 0:
                if sub_bit & first_bit != 0:
                    res[i] += counts[sub_bit]
                sub_bit = (sub_bit - 1) & origin_bit
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
