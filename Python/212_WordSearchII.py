"""
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""


from typing import List
from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def inRange(i,j):
            return 0 <= i < R and 0 <= j < C

        def dfs(i,j,word):
            # print(i,j,word,visited)
            if not word:
                return True
            if not inRange(i,j) or board[i][j] != word[0]:
                return False
            word = word[1:]
            for di,dj in dir4:
                ni,nj = i+di, j+dj
                if (ni,nj) not in visited:
                    visited.add((ni,nj))
                    if dfs(ni,nj,word):
                        return True
                    visited.remove((ni,nj))
            return False

        R, C = len(board), len(board[0])
        dir4 = [(0,1),(0,-1),(1,0),(-1,0)]
        start_letters = set([word[0] for word in words])
        start_dict = defaultdict(list)
        for i in range(R):
            for j in range(C):
                c = board[i][j]
                if c in start_letters:
                    start_dict[c].append((i,j))
        res = []
        for word in words:
            for i,j in start_dict[word[0]]:
                visited = set()
                visited.add((i,j))
                if dfs(i,j,word):
                    res.append(word)
                    break
        return res

S = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(S.findWords(board, words))

board = [["a","b"],["c","d"]]
words = ["abcb"]
print(S.findWords(board, words))

board =[["a","a"]]
words = ["a"]
print(S.findWords(board, words))

board = [["a","a"]]
words = ["aaa"]
print(S.findWords(board, words))