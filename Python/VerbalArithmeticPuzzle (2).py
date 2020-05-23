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
1 <= words[i].length, results.length <= 7
words[i], result contains only upper case English letters.
Number of different characters used on the expression is at most 10.
"""

class Solution:
    def isSolvable(self, words, result: str) -> bool:


        


        layer_set_list = []

        map_dict = dict()
        used = [0]*10
        characters = set(result)
        max_letter_len = max(len(w) for w in words)
        if max_letter_len > len(result):
            return False
        max_letter_len = max(max_letter_len, len(result))
        layer_set_list = [set() for _ in range(max_letter_len)]
        for w in words:
            characters |= set(w)
            rev_w = w[::-1]
            for i in range(len(rev_w)):
                layer_set_list[i].add(rev_w[i])
        
        for c in characters:
            map_dict[c] = -1
        len_c = len(characters)
        nums = [i for i in range(10)]

        rev_result = result[::-1]
        c = 0
        visited = [0]*10
        for i in range(len(layer_set_list)):
            letters = layer_set_list[i]
            r = rev_result[i]
            unused = [i for i in range(10) if not visited[i]]
            
            
        print(layer_set_list)
        

#ref from: https://leetcode.com/problems/verbal-arithmetic-puzzle/discuss/463921/python-backtracking-with-pruning-tricks
class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:


        def dfs(idx, i, carry, visited, mp):
            if idx == n:
                return carry == 0
            if i == len(words) + 1:
                sums = sum(mp[word[-idx - 1]] if idx < len(word) else 0 for word in words) + carry
                if sums % 10 == mp[result[-idx - 1]]:
                    carry = sums // 10
                    return dfs(idx + 1, 0, carry, visited, mp)
                return False

            if (i < len(words) and idx >= len(words[i])): # no letter in word[i], continue
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


        start = set()
        for word in words + [result]:
            if len(word) > 1:
                start.add(word[0])

        n = max(map(len, words + [result]))
        if len(result) < n:
            return False

        return dfs(0, 0, 0, set(), {})      

s = Solution()
words = ["SEND","MORE"]
result = "MONEY"
print(s.isSolvable(words, result))
words = ["SIX","SEVEN","SEVEN"]
result = "TWENTY"
print(s.isSolvable(words, result))

words = ["THIS","IS","TOO"]
result = "FUNNY"
print(s.isSolvable(words, result))

words = ["LEET","CODE"]
result = "POINT"
print(s.isSolvable(words, result))

