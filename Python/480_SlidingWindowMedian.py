
"""
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
"""


from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        use a fenwick tree to store sorted index based on the value of nums
        update the fenwick tree when the window slides
        query k//2 + 1 (and k // 2 if k is even) for median
        """
        def update(i, v):
            while i <= length:
                counts[i] += v
                i += i & -i
            pass

        def query(k):
            while counts[i] > k:
                pass


        length = len(nums)
        vals = sorted([(v, i) for i, v in enumerate(nums)])
        counts = [0] * (length + 1)
        index_convert = dict(zip(i, vals[i][1] + 1) for i in range(length))  # link the index in nums and counts


from bisect import insort
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        lst = sorted(nums[:k - 1])
        len_n = len(nums)
        half_k, rmd = divmod(k, 2)
        for i in range(k - 1, len_n):
            if i >= k:
                lst.remove(nums[i - k])
            insort(lst, nums[i])
            # print(i, nums[i], lst)
            if rmd == 1:
                res.append(lst[half_k])
            else:
                res.append((lst[half_k] + lst[half_k - 1]) / 2)
        return res


from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList(nums[:k])
        res = []
        half_k, rmd = divmod(k, 2)
        tmp = window[half_k] if rmd == 1 else (window[half_k] + window[half_k - 1]) / 2
        res.append(tmp)
        for i in range(k, len(nums)):
            window.remove(nums[i - k])
            window.add(nums[i])
            tmp = window[half_k] if rmd == 1 else (window[half_k] + window[half_k - 1]) / 2
            res.append(tmp)
        return res

# https://leetcode.com/problems/sliding-window-median/discuss/333240/Python-O(NlogN)-using-heap
import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        """
        use a upper heap and lower heap, keep the max and min part of the window respectively
        keep the length of the lower heap len_k//2 and the length of the upper heap len_k - len_k//2.
        iterate over the nums, keep the valid (in window) nums in upper and lower heap always to be len_k - len_k//2 and len_k//2.
        only delete the invalid nums if they are at the top of the heap
        """
        def poppush(h1, h2):
            """
            pop an element from h1, push it to h2, convert the sign
            """
            v, i = heapq.heappop(h1)
            heapq.heappush(h2, (-v, i))

        lower, upper = [], []
        res = []
        half_k, rmd = divmod(k, 2)
        len_n = len(nums)

        for i, v in enumerate(nums[:k]):
            heapq.heappush(upper, (v, i))
        for _ in range(half_k):
            poppush(upper, lower)
        res.append(upper[0][0] if rmd else (upper[0][0] - lower[0][0]) / 2)
        # print(lower, upper)
        for i in range(k, len_n):
            v = nums[i]
            j = i - k
            pre_v = nums[j]
            if v >= upper[0][0]:
                heapq.heappush(upper, (v, i))
                if pre_v <= upper[0][0]:  # if pre_v > upper[0][0] then it is in upper, so the valid nums in lower and upper are the same, we do nothing. but if the pre_v is in lower, we need to transfer an element to lower to keep the balance.
                # if (pre_v, j) is upper[0], we can transfer it to lower for removal, no loss for lower
                # if (pre_v, j) is not upper[0], it can compensate the loss of lower
                    poppush(upper, lower)
            else:
                heapq.heappush(lower, (-v, i))
                if pre_v >= upper[0][0]:
                    poppush(lower, upper)

            while lower and lower[0][1] <= j:
                heapq.heappop(lower)
            while upper and upper[0][1] <= j:
                heapq.heappop(upper)
            # print(lower, upper)
            res.append(upper[0][0] if rmd else (upper[0][0] - lower[0][0]) / 2)
        return res



S = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(S.medianSlidingWindow(nums, k))
nums = [1,4,2,3]
k = 4
print(S.medianSlidingWindow(nums, k))
