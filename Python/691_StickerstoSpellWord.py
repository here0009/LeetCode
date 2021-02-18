"""
We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.
"""


from typing import List
from collections import Counter
from functools import lru_cache
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        @lru_cache(None)
        def dp(s_index, t_vals):
            if sum(t_vals) == 0:
                return 0
            res = float('inf')
            if s_index == len_s:
                return res
            s_counts = sticker_lst[s_index]
            tv_list = list(t_vals)
            max_cycle = max(t_vals[x_dict[x]] // v + 1 for x, v in s_counts.items())
            for cycle in range(max_cycle + 1):
                t2 = tv_list[:]
                for x, v in s_counts.items():
                    t2[x_dict[x]] = max(0, tv_list[x_dict[x]] - cycle * v)
                res = min(res, cycle + dp(s_index + 1, tuple(t2)))
            return res

        t_counts = Counter(target)
        t_keys = list(t_counts.keys())
        t_vals = [t_counts[key] for key in t_keys]
        x_dict = {x: i for i, x in enumerate(t_keys)}  # index of letter in t_keys
        # print(t_keys, x_dict)

        sticker_lst = []
        s_keys = set()
        for sticker in stickers:
            s2 = ''.join(x for x in sticker if x in x_dict)
            if s2:
                sticker_lst.append(Counter(s2))
            s_keys |= set(s2)
        if len(set(t_keys) - s_keys) > 0:
            return -1
        len_s = len(sticker_lst)
        # print('t_keys', t_keys)
        # print('tv_vals', t_vals)
        # print(sticker_lst)
        # print(t_counts)
        return dp(0, tuple(t_vals))


from typing import List
from collections import Counter
from functools import lru_cache
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        @lru_cache(None)
        def dp(s_index, t_vals):
            if sum(t_vals) == 0:
                return 0
            res = float('inf')
            if s_index == len_s:
                return res
            s_counts = sticker_lst[s_index]
            tv_list = list(t_vals)
            max_cycle = max(t_vals[x_dict[x]] // v + 1 for x, v in s_counts.items())
            for cycle in range(max_cycle + 1):
                t2 = tv_list[:]
                for x, v in s_counts.items():
                    t2[x_dict[x]] = max(0, tv_list[x_dict[x]] - cycle * v)
                res = min(res, cycle + dp(s_index + 1, tuple(t2)))
            return res

        t_counts = Counter(target)
        t_keys = list(t_counts.keys())
        t_vals = [t_counts[key] for key in t_keys]
        x_dict = {x: i for i, x in enumerate(t_keys)}  # index of letter in t_keys

        sticker_lst = []
        s_keys = set()
        for sticker in stickers:
            s2 = ''.join(x for x in sticker if x in x_dict)
            if s2:
                sticker_lst.append(Counter(s2))
            s_keys |= set(s2)
        if len(set(t_keys) - s_keys) > 0:
            return -1
        len_s = len(sticker_lst)
        return dp(0, tuple(t_vals))



S = Solution()
print(S.minStickers(["with", "example", "science"], "thehat"))
print(S.minStickers(["notice", "possible"], "basicbasic"))
print(S.minStickers(["these","guess","about","garden","him"], "atomher"))
print(S.minStickers(["fly","me","charge","mind","bottom"], "centorder"))

# Output
# 5
# Expected
# 3
