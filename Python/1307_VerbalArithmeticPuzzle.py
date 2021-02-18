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
        """
        wrong answer
        """
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


from typing import List
from itertools import permutations
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        enumerate all possible combination of words in result 1st, then test if they can be appied to words 
        wrong answer
        """
        words = sorted([word[::-1] for word in words], key=len, reverse=True)
        result = result[::-1]
        if len(words[0]) > len(result):
            return False
        self.nums = set(range(10))
        len_w = len(result)
        self.w_dict = dict()
        return backTrack(0, 0)





class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        fails at test case words = ["A", "B"] result = "A"
        """
        def solve(i, j, carry):
            if j == len(words): # The current column assignment is over, so check for validity
                csum = carry
                for k in range(len(words)):
                    csum += 0 if i >= len(words[k]) else assign[words[k][i]] 
                if i >= len(result): return False # We have come to column i, but the result itself is not long enough.
                if result[i] in assign:
                    return csum % 10 == assign[result[i]] and solve(i+1, 0, csum // 10) # i th char of result  is already assigned, so check if its valid and go to next column i+1 and start from word 0
                else:
                    # If the current digit can't be assigned to ith char of result or if its 0 and we are looking at first char of a word: then return False
                    if (csum % 10) in assign.values() or (csum % 10 == 0 and i == len(result) - 1): return False
                    assign[result[i]] = csum % 10
                    ret = solve(i+1, 0, csum // 10)
                    del assign[result[i]]
                    return ret

            if i == len(result): 
                for w in words + [result]:
                    if len(w) > 1 and assign[w[-1]] == 0:
                        return False
                return i >= max(len(w) for w in words) and carry == 0
                #and all(assign[w[len(w)-1]] != 0 for w in words + [result] if len(w) > 1)
            # Handle length of word less than the column we are looking at OR the ith column char of the jth word is already assigned previously
            if i >= len(words[j]) or words[j][i] in assign: return solve(i, j+1, carry)
            for val in range(10):
                if val == 0 and i == len(words[j]) - 1: continue  # Handle not to assign 0 for first letter of a word 
                if val not in assign.values():
                    assign[words[j][i]] = val
                    ret = solve(i, j+1, carry)
                    if ret: return True
                    del assign[words[j][i]]
            return False

        result = result[::-1]
        words = [w[::-1] for w in words]
        assign = dict()
        return solve(0, 0, 0)

# https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463921/python-backtracking-with-pruning-tricks
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        start = set()
        for word in words + [result]:
            if len(word) > 1:
                start.add(word[0])


        n = max(map(len, words + [result]))
        if len(result) < n:
            return False

        def dfs(idx, i, carry, visited, mp):
            if idx == n:
                return carry == 0
            if i == len(words) + 1:
                sums = sum(mp[word[-idx - 1]] if idx < len(word) else 0 for word in words) + carry
                if sums % 10 == mp[result[-idx - 1]]:
                    carry = sums // 10
                    return dfs(idx + 1, 0, carry, visited, mp)
                return False

            if (i < len(words) and idx >= len(words[i])):
                return dfs(idx, i + 1, carry, visited, mp)
            tmp = words + [result]
            ch = tmp[i][-idx-1]
            if ch in mp:
                return dfs(idx, i + 1, carry, visited, mp)
            begin = 0
            if ch in start:
                begin = 1
            for x in range(begin, 10):
                if x not in visited:
                    visited.add(x)
                    mp[ch] = x
                    if dfs(idx, i + 1, carry, visited, mp.copy()):
                        return True
                    visited.remove(x)
            return False

        return dfs(0, 0, 0, set(), {})

# https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463920/Python-Backtracking      
class Solution:
    def isSolvable(self, words, result):
        # print(words)
        def search(column, row, bal):
            if column >= C:
                return bal == 0
            if row == R:
                return bal % 10 == 0 and search(column + 1, 0, bal // 10)

            word = words[row]
            if column >= len(word):
                return search(column, row + 1, bal)

            letter = word[~column]  # reverse column, equal to len(word) - 1 - column or -1-column
            begin = 1 if letter in start else 0
            sign = 1 if row < R - 1 else -1  # if row == R - 1, we minus it from the sum, so we only need to check if the total sum is 0
            if letter in assigned:
                return search(column, row + 1, bal + sign * assigned[letter])
            else:
                for d in range(begin, 10):
                    ad = assigned_inv[d]
                    if ad is None:
                        assigned_inv[d] = letter
                        assigned[letter] = d
                        if search(column, row + 1, bal + sign * d):
                            return True
                        assigned_inv[d] = None
                        del assigned[letter]
            return False

        words.append(result)
        R, C = len(words), max(map(len, words))
        assigned = {}
        assigned_inv = [None] * 10
        start = {w[0] for w in words + [result] if len(w) > 1}
        return search(0, 0, 0)
        


from typing import List
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        """
        Thoughts: we can use dfs(i, j, carry) to track the index of words, the index of word, to check if we can solve the puzzle
        pay attention to the start letters, they can not be 0 if unless there's only one digit
        """
        def dfs(row, col, total):
            if col == C:
                return total == 0
            if row == R:
                q, rmd = divmod(total, 10)
                return rmd == 0 and dfs(0, col + 1, q)
            word = words[row]
            if col >= len(word):
                return dfs(row + 1, col, total)
            letter = word[~col]
            sign = -1 if row == R - 1 else 1  # if the word is result, we minus it from total
            if letter in letter_digit:
                return dfs(row + 1, col, total + sign * letter_digit[letter])
            begin = 1 if letter in start_letters else 0
            for i in range(begin, 10):
                if digit_letter[i] is None:
                    digit_letter[i] = letter
                    letter_digit[letter] = i
                    if dfs(row + 1, col, total + sign * letter_digit[letter]):
                        return True
                    digit_letter[i] = None
                    del letter_digit[letter]
            return False

        words.append(result)
        R = len(words)
        C = max(len(w) for w in words)
        if C > len(result):
            return False
        start_letters = set([w[0] for w in words if len(w) > 1])
        letter_digit = dict()
        digit_letter = [None] * 10
        return dfs(0, 0, 0)

S = Solution()
words = ["SEND","MORE"]
result = "MONEY"
print(S.isSolvable(words, result))
words = ["SIX","SEVEN","SEVEN"]
result = "TWENTY"
print(S.isSolvable(words, result))
words = ["THIS","IS","TOO"]
result = "FUNNY"
print(S.isSolvable(words, result))
words = ["LEET","CODE"]
result = "POINT"
print(S.isSolvable(words, result))
words = ["AA","BB"]
result = "AA"
print(S.isSolvable(words, result))
words = ["A", "B"]
result = "A"
print(S.isSolvable(words, result))