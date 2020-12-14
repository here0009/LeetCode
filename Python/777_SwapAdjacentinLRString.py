"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

 

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
Example 3:

Input: start = "LLR", end = "RRL"
Output: false
Example 4:

Input: start = "XL", end = "LX"
Output: true
Example 5:

Input: start = "XLLR", end = "LXLX"
Output: false
 

Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        Thoughts: test if start_no_x == end_no_x after removal of X
        wrong for the test case
        start = "LXXLXRLXXL"
        end = "XLLXRXLXLX"
        LX can transform to XL
        """
        if len(start) != len(end):
            return False
        start_no_x = ''.join(start.split('X'))
        end_no_x = ''.join(end.split('X'))
        return start_no_x == end_no_x


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        Thoughts: L can move to the most left position of adjecent Xs, R can move to the most right position of ajecent Xs
        wrong answer
        """
        if len(start) != len(end):
            return False
        start_lst = list(start)
        len_s = len(start_lst)
        si = 0
        transform_dict = {'X': 'L', 'R': 'X'}
        while si < len_s:
            # print(si, start_lst)
            if start_lst[si] != end[si]:
                # print(start_lst[si], end[si])
                v = start_lst[si]
                if v not in transform_dict:
                    return False
                target = transform_dict[v]
                ei = si + 1
                # print(ei)
                while ei < len_s and start[ei] != target:
                    if start[ei] != 'X':
                        return False
                    ei += 1
                if ei == len_s:
                    return False
                start_lst[si], start_lst[ei] = start_lst[ei], start_lst[si]
                # print(start_lst[si])
            si += 1
        return True

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        move X seems more convinient, move X to the right of L, to the left of R
        """
        if len(start) != len(end):
            return False
        start_lst = list(start)
        len_s = len(start_lst)
        for i, v in enumerate(start_lst):
            # print(i, v)
            if end[i] == 'X' and v != 'X':
                if v == 'L':  # find X in the left
                    j = i - 1
                    while j >= 0 and start_lst[j] in 'XL' and start_lst[j] == end[j]:
                        j -= 1
                    if j < 0 or start_lst[j] != 'X':
                        return False
                elif v == 'R':  # find X in the right
                    j = i + 1
                    while j < len_s and start_lst[j] in 'R':
                        j += 1
                    if j >= len_s or start_lst[j] != 'X':
                        return False
                start_lst[i], start_lst[j] = start_lst[j], start_lst[i]
            # print(start_lst, end)
        return ''.join(start_lst) == end


S = Solution()
start = "RXXLRXRXL"
end = "XRLXXRRLX"
print(S.canTransform(start, end))
start = "X"
end = "L"
print(S.canTransform(start, end))
start = "LLR"
end = "RRL"
print(S.canTransform(start, end))
start = "XL"
end = "LX"
print(S.canTransform(start, end))
start = "XLLR"
end = "LXLX"
print(S.canTransform(start, end))
start = "LXXLXRLXXL"
end = "XLLXRXLXLX"
print(S.canTransform(start, end))
start = "XLXRRXXRXX"
end = "LXXXXXXRRR"
print(S.canTransform(start, end))
start = "XXXXXLXXXX"
end = "LXXXXXXXXX"
print(S.canTransform(start, end))
