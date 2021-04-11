"""
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

 

Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:



Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:



Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
 

Constraints:

1 <= k <= events.length
1 <= k * events.length <= 106
1 <= startDayi <= endDayi <= 109
1 <= valuei <= 106
"""


from typing import List
from functools import lru_cache
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(idx, num):

            if idx == length or num == k:
                return 0
            s, e, v = events[idx]
            res = max(dp(idx + 1, num), v)
            for j in range(idx + 1, length):
                if events[j][0] > e:
                    res = max(res, v + dp(j, num + 1))
            # print(idx, num, res)
            return res

        events.sort()
        length = len(events)
        # print(events)
        return dp(0, 0)


from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        def dp(idx, num):
            if (idx, num) in memo:
                return memo[(idx, num)]

            if idx == length or num == k:
                memo[(idx, num)] = 0
                return 0
            s, e, v = events[idx]
            res = max(dp(idx + 1, num), v)
            for j in range(idx + 1, length):
                if events[j][0] > e:
                    res = max(res, v + dp(j, num + 1))
            # print(idx, num, res)
            memo[(idx, num)] = res
            return res

        memo = dict()
        events.sort()
        length = len(events)
        # print(events)
        return dp(0, 0)


from typing import List
from bisect import bisect_left
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        events.sort()
        print(events)
        stack = [(0, 0)]
        res = 0
        for s, e, v in events:
            idx = bisect_left(stack, (e, v))
            if idx == len(stack) and idx < k:
                stack.append((e, v + stack[-1][1]))
            else:
                stack[idx] = (e, v + stack[idx - 1][1])
            print(idx, stack, res)
            res = max(res, stack[idx][1])
            
        return res


S = Solution()
events = [[1,2,4],[3,4,3],[2,3,1]]
k = 2
print(S.maxValue(events, k))
events = [[1,2,4],[3,4,3],[2,3,10]]
k = 2
print(S.maxValue(events, k))
events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]]
k = 3
print(S.maxValue(events, k))
events = [[21,77,43],[2,74,47],[6,59,22],[47,47,38],[13,74,57],[27,55,27],[8,15,8]]
k = 4
print(S.maxValue(events, k))
# 输出：
# 65
# 预期：
# 57