"""
You are given an integer array nums​​​ and an integer k. You are asked to distribute this array into k subsets of equal size such that there are no two equal elements in the same subset.

A subset's incompatibility is the difference between the maximum and minimum elements in that array.

Return the minimum possible sum of incompatibilities of the k subsets after distributing the array optimally, or return -1 if it is not possible.

A subset is a group integers that appear in the array with no particular order.

 

Example 1:

Input: nums = [1,2,1,4], k = 2
Output: 4
Explanation: The optimal distribution of subsets is [1,2] and [1,4].
The incompatibility is (2-1) + (4-1) = 4.
Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.
Example 2:

Input: nums = [6,3,8,1,3,1,2,2], k = 4
Output: 6
Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
Example 3:

Input: nums = [5,3,3,6,3,3], k = 3
Output: -1
Explanation: It is impossible to distribute nums into 3 subsets where no two elements are equal in the same subset.
 

Constraints:

1 <= k <= nums.length <= 16
nums.length is divisible by k
1 <= nums[i] <= nums.length
"""


from typing import List
from collections import Counter
import heapq
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        """
        wrong answer
        """
        counts = Counter(nums)
        len_n = len(nums)
        if max(counts.values()) > k:
            return -1
        lst = [(key, val) for key, val in counts.items()]
        heapq.heapify(lst)
        group = len_n // k
        res = 0
        print(lst)
        for _ in range(k):
            tmp_counts = 0
            tmp_lst = []
            while tmp_counts < group:
                # print(tmp_counts, k)
                key, val = heapq.heappop(lst)
                tmp_counts += 1
                val -= 1
                tmp_lst.append((key, val))
            print(tmp_lst)
            res += tmp_lst[-1][0] - tmp_lst[0][0]
            for key, val in tmp_lst:
                if val > 0:
                    heapq.heappush(lst, (key, val))
        return res


from typing import List
from collections import Counter
from itertools import combinations
from functools import lru_cache
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(status, group):
            if group == k:
                return 0
            avl = []
            for i,v in enumerate(status):
                if v < counts[keys[i]]:
                    avl.append(i)
            res = float('inf')
            for comb in combinations(avl, each_group):
                s2 = list(status)
                for c in comb:
                    s2[c] += 1
                tmp_lst = sorted(keys[c] for c in comb)
                tmp_val = tmp_lst[-1] - tmp_lst[0]
                res = min(res, tmp_val + dp(tuple(s2), group + 1))
            return res


        counts = Counter(nums)
        print(counts)
        len_n = len(nums)
        len_c = len(counts)
        each_group = len_n // k
        if max(counts.values()) > k:
            return -1
        keys = list(counts.keys())
        return dp(tuple([0] * len_c), 0)


from typing import List
from collections import Counter
from itertools import combinations
from functools import lru_cache
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        @lru_cache(None)
        def dp(status):
            if status == target:
                return 0
            avl = []  # store the index of the available keys
            for i, v in enumerate(status):
                if v < counts[keys[i]]:
                    avl.append(i)
            res = float('inf')
            for comb in combinations(avl, each_group):  # try all the combinations of the available keys
                s2 = list(status)
                max_v, min_v = float('-inf'), float('inf')
                for c in comb:
                    s2[c] += 1
                    max_v = max(max_v, keys[c])
                    min_v = min(min_v, keys[c])
                res = min(res, max_v - min_v + dp(tuple(s2)))
            return res

        len_n = len(nums)
        counts = Counter(nums)
        if max(counts.values()) > k:
            return -1
        target = tuple(counts.values())
        keys = list(counts.keys())
        len_c = len(counts)
        each_group = len_n // k

        return dp(tuple([0] * len_c))

S = Solution()
nums = [1,2,1,4]
k = 2
print(S.minimumIncompatibility(nums, k))

nums = [6,3,8,1,3,1,2,2]
k = 4
print(S.minimumIncompatibility(nums, k))

nums = [5,3,3,6,3,3]
k = 3

print(S.minimumIncompatibility(nums, k))

nums = [5,3,2,11,5,8,7,7,6,2,4,5]
k = 12
print(S.minimumIncompatibility(nums, k))
