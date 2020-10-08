"""
Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rearrange-string-k-distance-apart
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
class Solution:
    def rearrangeString(self, string: str, k: int) -> str:
        """
        this solution did not work
        """
        counter = Counter(string)
        total = length = len(string)
        res = [0]*total
        keys = sorted(counter.keys(), key=lambda x:counter[x], reverse=True)
        print(keys, counter)
        r_i, k_i = 0, 0 # the index of res and key
        while total > 0:
            print(res)
            key, val = keys[k_i], counter[keys[k_i]]
            gap = (total - val)//(val - 1)+1
            if gap + 1 < k:
                return ''
            else:
                gap = k
            for j in range(r_i, length, gap):
                res[j] = key
            k_i += 1
            total -= val
            while r_i < length and res[r_i] != 0:
                r_i += 1

        return res

# https://leetcode-cn.com/problems/rearrange-string-k-distance-apart/solution/lc-358-k-ju-chi-jian-ge-zhong-pai-zi-fu-chuan-dui-/
import heapq
from collections import Counter, deque
class Solution:
    def rearrangeString(self, string: str, k: int) -> str:
        if k <= 1:
            return string
        counter = Counter(string)
        dq = deque([])
        max_heap = []
        for key,val in counter.items():  # make sure do not use k,v in  this statement and others key, val below, for k is an argument
            heapq.heappush(max_heap, (-val, key))
        res = ''
        while max_heap:
            val, key = heapq.heappop(max_heap)
            res += key
            dq.append((val+1, key))

            if len(dq) == k:
                val, key = dq.popleft()
                if val < 0:
                    heapq.heappush(max_heap, (val, key))
        return res if len(res) == len(string) else ''



S = Solution()
string = "aabbcc"
k = 3
print(S.rearrangeString(string, k))
string = "aaabc"
k = 3
print(S.rearrangeString(string, k))
string = "aaadbbcc"
k = 2
print(S.rearrangeString(string, k))
string = "aa"
k = 0
print(S.rearrangeString(string, k))