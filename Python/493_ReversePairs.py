"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
from bisect import bisect_left
class Solution:
    def reversePairs(self, nums) -> int:
        """
        TLE
        """
        sort_n = sorted((v,i) for i,v in enumerate(nums))
        res = 0
        # print(sort_n)
        for i,n in enumerate(nums):
            start = bisect_left(sort_n, (2*n+1,0))
            # print(i,n,start)
            res += sum([1 for v,j in sort_n[start:] if j<i])
        return res

from collections import Counter
from bisect import bisect_left
class Solution:
    """
    TLE
    """
    def reversePairs(self, nums) -> int:
        n_counter = Counter(nums)
        n_counter_keys = sorted(list(n_counter.keys()))
        # print(n_counter_keys)
        res = 0
        for n in nums[::-1]:
            n_counter[n] -= 1
            # if n_counter[n] == 0:
            #     n_counter_keys.remove(n)
            index = bisect_left(n_counter_keys, 2*n+1)
            res += sum([n_counter[key] for key in n_counter_keys[index:]])
            # print(res)
        return res


from typing import List
from collections import Counter
class Solution:
    """
    Thoughts: try to use merge sort, keep the relative position information and use the already sorted information
    """
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(i, j):
            if i == j:
                return [nums[i]]
            mid = (i + j) // 2
            left = mergeSort(i, mid)
            right = mergeSort(mid + 1, j)
            len_right = len(right)
            l_index, r_index = 0, 0
            for l_index, l_num in enumerate(left):
                while r_index < len_right and l_num > 2 * right[r_index]:
                    r_index += 1
                self.res += r_index
            return sorted(left + right)

        self.res = 0
        if not nums:
            return self.res
        mergeSort(0, len(nums) - 1)
        return self.res

from typing import List
from collections import Counter
class Solution:
    """
    Thoughts: try to use merge sort, keep the relative position information and use the already sorted information
    """
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(i, j):
            if i >= j:
                return 0
            mid = (i + j) // 2
            res = mergeSort(i, mid) + mergeSort(mid + 1, j)
            right_index = mid + 1
            for left_index in range(i, mid + 1):
                while right_index <= j and nums[left_index] > 2 * nums[right_index]:
                    right_index += 1
                res += right_index - (mid + 1)
            nums[i: j + 1] = sorted(nums[i: j + 1])
            return res

        return mergeSort(0, len(nums) - 1)

# https://leetcode.com/problems/reverse-pairs/discuss/385371/Python-solutions
from typing import List
from collections import Counter
class BIT:

    def __init__(self, length):
        self.len = length
        self.counts = [0] * (length + 1)

    def update(self, idx):
        while idx <= self.len:
            self.counts[idx] += 1
            idx += idx & (-idx)

    def get_sum(self, idx):
        res = 0
        while idx > 0:
            res += self.counts[idx]
            idx -= idx & (-idx)
        return res


class Solution:
    """
    Thoughts: we can also use fenwick tree / bit tree to sovle the problem, just keep a tree of size nums + [2*num for num in nums], use rank index of num in nums to query it, rank of 2*num to update it.
    """
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums2 = sorted(list(set(nums + [num * 2 for num in nums])))
        len_n = len(nums2)
        bit_tree = BIT(len_n)
        ranks = {v: i for i, v in enumerate(nums2, 1)}
        res = 0
        for num in nums[::-1]:
            res += bit_tree.get_sum(ranks[num] - 1)
            bit_tree.update(ranks[2 * num])
        return res



S = Solution()
nums = [1,3,2,3,1]
print(S.reversePairs(nums))
nums = [2,4,3,5,1]
print(S.reversePairs(nums))
