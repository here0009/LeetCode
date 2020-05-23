"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
from collections import deque
from collections import Counter
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pos_set = set()
        pos_list = deque()
        pos_dict = defaultdict(deque)
        t_counter = Counter(t)
        len_t = len(t)
        min_len = float('inf')
        for i,v in enumerate(s):
            if v in t_counter:
                pos_dict[v].append(i)
                pos_set.add(i)
                pos_list.append(i)
                # print(pos_dict[v])
                # print(t_counter[v])
                if len(pos_dict[v]) > t_counter[v]:
                    index = pos_dict[v].popleft()
                    pos_set.remove(index)
                    while pos_list[0] not in pos_set:
                        pos_list.popleft()
                if len(pos_set) == len_t:
                    if pos_list[-1]-pos_list[0] + 1 < min_len:
                        start, end = pos_list[0],pos_list[-1]
                        min_len = end+1-start
        if min_len == float('inf'):
            return ''
        else:
            return s[start:end+1]

S = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(S.minWindow(s,t))
