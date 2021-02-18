"""
There is a special kind of apple tree that grows apples every day for n days. On the ith day, the tree grows apples[i] apples that will rot after days[i] days, that is on day i + days[i] the apples will be rotten and cannot be eaten. On some days, the apple tree does not grow any apples, which are denoted by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the maximum number of apples you can eat.

 

Example 1:

Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7
Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.
Example 2:

Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
Output: 5
Explanation: You can eat 5 apples:
- On the first to the third day you eat apples that grew on the first day.
- Do nothing on the fouth and fifth days.
- On the sixth and seventh days you eat apples that grew on the sixth day.
 

Constraints:

apples.length == n
days.length == n
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
days[i] = 0 if and only if apples[i] = 0.
"""


from typing import List
import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        day_app = sorted([(days[i] + i, i, apples[i]) for i in range(N)])  # start, end, apple
        print(day_app)
        pre_end = 0
        for end, start, app in day_app:
            pre_end = max(pre_end, start)
            pre_end += min(app, end - pre_end)
        return pre_end


from typing import List
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        end_day = 0
        res = 0
        for i in range(N):  # i is the day
            app, day = apples[i], i + days[i]
            if day <= end_day:
                continue
            if i > end_day:
                end_day = i
            end_day += min(day - end_day, app)
            print(app, day, end_day)
        return end_day


from typing import List
import heapq
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        N = len(apples)
        res = 0
        pq = []   # store (day, apple number)
        index = 0
        while index < N or pq:
            if index < N:
                heapq.heappush(pq, [index + days[index], apples[index]])
            while pq and (pq[0][0] <= index or pq[0][1] == 0):
                heapq.heappop(pq)
            if pq:
                res += 1
                pq[0][1] -= 1
            index += 1
        return res

S = Solution()
apples = [1,2,3,5,2]
days = [3,2,1,4,2]
print(S.eatenApples(apples, days))
apples = [3,0,0,0,0,2]
days = [3,0,0,0,0,2]
print(S.eatenApples(apples, days))
apples = [0,19,19,19,11,14,33,0,28,7,0,28,7,0,21,16,0,22,0,13,8,0,19,0,0,2,26,2,22,0,8,0,0,27,19,16,24,0,20,26,20,7,0,0,29,0,0,16,19,0,0,0,29,30,17,0,23,0,0,26,24,13,3,0,21,0,18,0]
days = [0,5,1,16,7,10,54,0,40,2,0,23,4,0,20,18,0,40,0,22,8,0,35,0,0,3,24,1,8,0,10,0,0,2,38,8,4,0,36,33,14,9,0,0,56,0,0,21,27,0,0,0,14,20,18,0,42,0,0,44,3,8,3,0,10,0,27,0]
print(S.eatenApples(apples, days))
# 输出：
# 103
# 预期：
# 102