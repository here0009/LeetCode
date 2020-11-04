"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

 

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
 

Constraints:

1 <= schedule.length , schedule[i].length <= 50
0 <= schedule[i].start < schedule[i].end <= 10^8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/employee-free-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        working_time = []
        for lst in schedule:
            for time in lst:
                working_time.append((time.start, time.end))
        res = []
        working_time.sort()
        pre_start, pre_end = working_time[0]
        for start, end in working_time[1:]:
            if start > pre_end:
                res.append(Interval(pre_end, start))
            pre_end = max(end, pre_end)
        return res


# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/employee-free-time/solution/yuan-gong-kong-xian-shi-jian-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution(object):
    def employeeFreeTime(self, avails):
        OPEN, CLOSE = 0, 1

        events = []
        for emp in avails:
            for iv in emp:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))

        events.sort()
        ans = []
        prev = None
        bal = 0
        for t, cmd in events:
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, t))

            bal += 1 if cmd is OPEN else -1
            prev = t

        return ans

class Solution:
    def employeeFreeTime(self, avails):
        events = []
        for emp in avails:
            for iv in emp:
                events.append((iv.start, -1))
                events.append((iv.end, 1))

        events.sort()
        ans = []
        prev = None
        bal = 0
        for t, cmd in events:
            if bal == 0 and prev is not None:
                ans.append(Interval(prev, t))
            bal += cmd
            prev = t

        return ans

