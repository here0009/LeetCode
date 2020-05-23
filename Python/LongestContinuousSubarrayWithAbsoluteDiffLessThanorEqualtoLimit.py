"""
Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2

Explanation: All subarrays are:

[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.

[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.

Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4

Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3



Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
"""


from collections import deque


class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        dq = deque([nums[0]])
        # max_v, min_v = nums[0], nums[0]
        res = 1
        for num in nums:
            while dq and abs(dq[0] - num) > limit:
                dq.popleft()
            dq.append(num)
            res = max(res, len(dq))
        return res


import bisect
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        res = 1
        tmp = [(nums[0], 0)]
        # print(tmp)
        for i in range(1, len(nums)):
            v = nums[i]
            left = bisect.bisect_left(tmp, (v - limit, -1))
            right = bisect.bisect_right(tmp, (v + limit, i))
            index = max(tmp[left[1]], tmp[right[1]])
            tmp = tmp[left:right]
            bisect.insort(tmp, (v, i))
            res = max(res, len(tmp))
            print(i,v,res,tmp)
        return res


import heapq
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        res = 1
        max_v_i = [(-nums[0], 0)]
        min_v_i = [(nums[0], 0)]
        for num_i in range(1, len(nums)):
            v = nums[num_i]
            print(v)
            heapq.heappush(max_v_i, (-v,num_i))
            heapq.heappush(min_v_i, (v,num_i))
            print(max_v_i)
            print(min_v_i)
            while max_v_i and -(max_v_i[0][0]) > v + limit:
                max_v_i.pop()
            while min_v_i and min_v_i[0][0] < v - limit:
                min_v_i.pop()
            print(max_v_i)
            print(min_v_i)
            # max_v_i.append((-v, i))
            # min_v_i.append((v, i))
            index = max(max_v_i[0][1], min_v_i[0][1])
            print(v,index)
            res = max(res, num_i-index)
            max_v_i = heapq.heapify([(-v,i) for i,v in enumerate(nums[index:num_i+1])])
            min_v_i = heapq.heapify([(v,i) for i,v in enumerate(nums[index:num_i+1])])
        return res


class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        left = 0
        res = 1
        max_i, min_i = 0, 0
        for i, v in enumerate(nums):
            if nums[i] > nums[max_i]:
                max_i = i
            if nums[i] < nums[min_i]:
                min_i = i
            if nums[max_i] - v <= limit and v - nums[min_i] <= limit:
                res = max(res, i - left + 1)
            else:
                left = i
                max_i, min_i = i, i
                for j in range(i, left - 1, -1):
                    if nums[j] > nums[max_i]:
                        max_i = j
                    if nums[j] < nums[min_i]:
                        min_i = j
                    if abs(nums[i] - nums[j]) > limit:
                        break
                res = max(res, i - j + 1)
                left = j + 1
            print('left, max_i, min_i', i, v, nums[left], nums[max_i], nums[min_i])
        return res


from collections import deque
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        min_dq = deque()
        max_dq = deque()
        res = 0
        left = 0
        for right, v in enumerate(nums):
            while min_dq and v <= nums[min_dq[-1]]:
                # if v == nums[min_dq[-1]], the previous index was ignored
                min_dq.pop()
            while max_dq and v >= nums[max_dq[-1]]:
                max_dq.pop()
            min_dq.append(right)
            max_dq.append(right)
            while nums[max_dq[0]] - nums[min_dq[0]] > limit:
                left += 1
                if left > min_dq[0]:
                    min_dq.popleft()
                if left > max_dq[0]:
                    max_dq.popleft()
            res = max(res, right - left + 1)
        return res

import heapq
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        maxq, minq = [], []
        res = 0
        left, right = 0, 0
        for right, v in enumerate(nums):
            heapq.heappush(maxq, (-v, right))
            heapq.heappush(minq, (v, right))
            while -maxq[0][0] - minq[0][0] > limit:
                left = min(maxq[0][1], minq[0][1]) + 1
                # move on step to the right
                while maxq[0][1] < left:
                    heapq.heappop(maxq)
                while minq[0][1] < left:
                    heapq.heappop(minq)
            res = max(res, right - left + 1)
        return res


S = Solution()
# nums = [8,2,4,7]
# limit = 4
# print(S.longestSubarray(nums, limit))
nums = [10,1,2,4,7,2]
limit = 5
print(S.longestSubarray(nums, limit))
nums = [4,2,2,2,4,4,2,2]
limit = 0
print(S.longestSubarray(nums, limit))
nums = [4]
limit = 0
print(S.longestSubarray(nums, limit))
nums = [4,8,5,1,7,9]
limit = 6
print(S.longestSubarray(nums, limit))
# Output:
# 4
# Expected:
# 3
