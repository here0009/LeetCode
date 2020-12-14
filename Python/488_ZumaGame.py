"""
Think about Zuma Game. You have a row of balls on the table, colored red(R), yellow(Y), blue(B), green(G), and white(W). You also have several balls in your hand.

Each time, you may choose a ball in your hand, and insert it into the row (including the leftmost place and rightmost place). Then, if there is a group of 3 or more balls in the same color touching, remove these balls. Keep doing this until no more balls can be removed.

Find the minimal balls you have to insert to remove all the balls on the table. If you cannot remove all the balls, output -1.

 

Example 1:

Input: board = "WRRBBW", hand = "RB"
Output: -1
Explanation: WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
Example 2:

Input: board = "WWRRBBWW", hand = "WRBRW"
Output: 2
Explanation: WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
Example 3:

Input: board = "G", hand = "GGGGG"
Output: 2
Explanation: G -> G[G] -> GG[G] -> empty 
Example 4:

Input: board = "RBYYBBRRB", hand = "YRBGB"
Output: 3
Explanation: RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty 
 

Constraints:

You may assume that the initial row of balls on the table won’t have any 3 or more consecutive balls with the same color.
1 <= board.length <= 16
1 <= hand.length <= 5
Both input strings will be non-empty and only contain characters 'R','Y','B','G','W'.
"""



# https://leetcode.com/problems/zuma-game/discuss/97007/SOLVED-Standard-test-program-is-wrong
# you might not get corret answer using greedy algorithm to insert balls to the same color
# RRWWRRBBRR -> RRWWRRBBR[W]R -> RRWWRRBB[B]RWR -> RRWWRRRWR -> RRWWWR -> RRR -> empty


from typing import Tuple
from collections import Counter
from functools import lru_cache
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        """
        can not remove all, that is how it played?
        wrong answer, wrong analysis
        """

        def remove_all(string: str) -> str:
            # print('rm before', string)
            while len(string) > 0:
                res = remove(string)
                if res == string:
                    break
                else:
                    string = res
            # print('rm after ', string)
            return string

        def remove(string: str) -> str:
            """
            we can choose to not remove all in one step
            """
            # print('before', string)
            res = ''
            i = 0
            pre = None
            c = 1  # counts of continue letters
            while i < len(string):
                if string[i] == pre:
                    c += 1
                else:
                    if c < 3:
                        res += string[i - c: i]
                    pre = string[i]
                    c = 1
                i += 1
            if c < 3:
                res += string[i - c: i]
            # print('after', b2)
            return res

        @lru_cache(None)
        def dp(string: str, avl: Tuple[int]) -> int:
            # print('before', string, avl)
            if not string:
                return 0
            tmp_string = remove_all(string)
            if not tmp_string:
                return 0
            avl_list = list(avl)
            pre = None
            res = float('inf')
            # print('s', string, string[5], string[6])
            for i, v in enumerate(string):
                # print(i, pre, v, avl_list)
                if v != pre:
                    if v in color_dict and avl_list[color_dict[v]] > 0:
                        b2 = string[:i] + v + string[i:]
                        avl_list[color_dict[v]] -= 1
                        res = min(res, 1 + dp(b2, tuple(avl_list)))
                        avl_list[color_dict[v]] += 1
                pre = v
            # print('after', string, avl)
            # print('res', res)
            return res

        counts = Counter(hand)
        keys = list(counts.keys())

        # if len(set(board) - set(keys)):
        #     return -1
        color_dict = {v: i for i, v in enumerate(keys)}
        avl = tuple(counts.values())
        # print(counts, keys, color_dict, avl)
        res = dp(board, avl)
        return res if res != float('inf') else -1



from functools import lru_cache
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        INF = float('inf')
        def de_dup(board):
            prev_en = 0
            for i, c in enumerate(board):
                if c != board[prev_en]:
                    if i - prev_en >= 3:
                        return de_dup(board[:prev_en] + board[i:])
                    prev_en = i
            return board

        @lru_cache(None)
        def dfs(board, hand):
            board = de_dup(board)
            if board == "#":
                return 0
            board_set = set(board)
            hand = "".join(h for h in hand if h in board_set)
            if not hand:
                return INF 
            ans = INF 
            for i in range(len(board)):
                for h_id, h in enumerate(hand):
                    new_hand = hand[:h_id] + hand[h_id+1:]
                    new_board = board[:i] + h + board[i:]
                    ans = min(ans, 1 + dfs(new_board, new_hand))
            return ans

        ans = dfs(board + "#", hand)
        return ans if ans < INF else -1


from typing import Tuple
from collections import Counter
from functools import lru_cache
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove(board: str) -> str:
            # print('before', board)
            while len(board) > 2:
                b2 = ''
                i = 0
                pre = None
                c = 1  # counts of continue letters
                while i < len(board):
                    if board[i] == pre:
                        c += 1
                    else:
                        if c < 3:
                            b2 += board[i - c: i]
                        pre = board[i]
                        c = 1
                    i += 1
                if c < 3:
                    b2 += board[i - c: i]
                if b2 == board:
                    board = b2
                    break
                board = b2
            # print('after', board)
            return board

        @lru_cache(None)
        def dp(bstring: str, hstring: str) -> int:
            # print('before', bstring, hstring)
            bstring = remove(bstring)
            hstring = ''.join(h for h in hstring if h in bstring)
            # print('after ', bstring, hstring)
            if not bstring:
                return 0
            res = float('inf')
            if not hstring:
                return res

            for i, b in enumerate(bstring):
                pre_h = None
                for j, h in enumerate(hstring):
                    if pre_h != h:
                        b2 = bstring[:i] + h + bstring[i:]
                        h2 = hstring[:j] + hstring[j + 1:]
                        res = min(res, 1 + dp(b2, h2))
                    pre_h = h
            # print(res)
            return res

        hand = ''.join(sorted(list(hand)))
        # hand = 
        res = dp(board, hand)
        return res if res != float('inf') else -1


from typing import Tuple
from collections import Counter
from functools import lru_cache
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove(board: str) -> str:
            while len(board) > 2:
                b2 = ''
                i, pre, c = 0, None, 0
                while i < len(board):
                    if board[i] == pre:
                        c += 1
                    else:
                        if c < 3:
                            b2 += board[i - c: i]
                        pre = board[i]
                        c = 1
                    i += 1
                if c < 3:
                    b2 += board[i - c: i]
                if b2 == board:
                    break
                board = b2
            return board

        @lru_cache(None)
        def dp(bstring: str, hstring: str) -> int:
            bstring = remove(bstring)
            hstring = ''.join(h for h in hstring if h in bstring)
            res = float('inf')
            if not bstring:
                return 0
            if not hstring:
                return res
            for i, b in enumerate(bstring):  # insertion point matters, even the letter are same
                pre_h = None
                for j, h in enumerate(hstring):
                    if pre_h != h:
                        b2 = bstring[:i] + h + bstring[i:]
                        h2 = hstring[:j] + hstring[j + 1:]
                        res = min(res, 1 + dp(b2, h2))
                    pre_h = h
            return res

        hand = ''.join(sorted(list(hand)))
        res = dp(board, hand)
        return res if res != float('inf') else -1

S = Solution()
# board = "WRRBBW"
# hand = "RB"
# print(S.findMinStep(board, hand))
# board = "WWRRBBWW"
# hand = "WRBRW"
# print(S.findMinStep(board, hand))
# board = "G"
# hand = "GGGGG"
# print(S.findMinStep(board, hand))
# board = "RBYYBBRRB"
# hand = "YRBGB"
# print(S.findMinStep(board, hand))
# board = "RRWWRRW"
# hand ="RR"
# print(S.findMinStep(board, hand))
# board = "RRWWRRBBRR"
# hand ="WB"
# print(S.findMinStep(board, hand))
# # Output
# # -1
# # Expected
# # 2
# board ="RRWWRRW"
# hand ="RR"
# print(S.findMinStep(board, hand))
# board = "WWBBWBBWW"
# hand = "BB"
# print(S.findMinStep(board, hand))

board = "WWRRBBWW"
hand = "WRBRW"
print(S.findMinStep(board, hand))
# Output
# 3
# Expected
# 2