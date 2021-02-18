"""
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc" in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.  Any answers specifying more than this number of moves will not be accepted.

 

Example 1:

Input: stamp = "abc", target = "ababc"
Output: [0,2]
([1,0,2] would also be accepted as an answer, as well as some other answers.)
Example 2:

Input: stamp = "abca", target = "aabcaca"
Output: [3,0,1]
 

Note:

1 <= stamp.length <= target.length <= 1000
stamp and target only contain lowercase letters.
"""


from typing import List
from collections import defaultdict, deque
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        """
        wrong answer
        """
        if len(target) < len(stamp) or len(set(target) - set(stamp)) > 0:
            return []
        stamp_i_dict = defaultdict(list)
        for v, i in stamp:
            stamp_i_dict[v].append(i)
        stamp_index = 0
        target_index = 0
        len_stamp, len_target = len(stamp), len(target)
        res = deque([])
        while target_index < len_target:
            t = target[target_index]
            if stamp[stamp_index] == t: 
                stamp_index = (stamp_index + 1) % len_stamp
            else:
                stamp_index = stamp_i_dict[t]



from typing import List
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]: 
        """
        try to reverse the process
        if we can change target to '?'*len(target) using stamp, then we can build target with stamps
        based on the limitation, if we can do this, we can do it in 10*len(target) iterations
        e.g.
        stamp = "abca"
        target = "aabcaca"
        => a????ca
        => ?????ca
        => ???????
        """
        def check(i):
            changed = False
            for j in range(len_s):
                if target[i + j] == '?':
                    continue
                if target[i + j] != stamp[j]:
                    return False 
                else:
                    changed = True
            if changed:
                target[i: i + len_s] = ['?'] * len_s
                res.append(i)
            return changed


        len_s, len_t = len(stamp), len(target)
        target = list(target)
        res = []
        changed = True
        while changed:
            changed = False
            for i in range(len_t - len_s + 1):
                changed |= check(i)
            if not changed:
                break
        return res[::-1] if target == ['?'] * len_t else []


S = Solution()
stamp = "abc"
target = "ababc"
print(S.movesToStamp(stamp, target))
stamp = "abca"
target = "aabcaca"
print(S.movesToStamp(stamp, target))