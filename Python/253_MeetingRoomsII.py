"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20], [10,16]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        """
        interval include start, not end, pq stores the ends of previous intervals.
        sort intervals first, if start >= end, pop the end for the latter start will also >= end
        the minMeeting room is the max ends in pq
        """
        intervals = sorted(intervals)
        pq = []
        res = 0
        heapq.heapify(pq)
        for s, e in intervals:
            while pq and s >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, e)
            res = max(res, len(pq))
        return res


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if len(intervals) == 0:
            return 0
        # 根据会议开始时间排序
        intervals.sort()
        rooms = [intervals[0][0]]   # 房间内保存最早结束时间
        for s, e in intervals:
            if rooms[0] <= s:       # 有空余房间
                heapq.heapreplace(rooms, e)
            else:                   # 没有空余房间
                heapq.heappush(rooms, e)
        return len(rooms)           # 返回房间个数

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0
        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        end_pointer = 0
        start_pointer = 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1
            start_pointer += 1

        return used_rooms


import heapq
class Solution:
    def minMeetingRooms(self, intervals) -> int:
        """
        每次最多空出一间会议室，则最大会议室数不会减小
        """
        intervals = sorted(intervals)
        pq = []
        res = 0
        heapq.heapify(pq)
        for s, e in intervals:
            if pq and s >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, e)
        return len(pq)

S = Solution()
intervals = [[0, 30],[5, 10],[15, 20], [10,16]]
print(S.minMeetingRooms(intervals))
intervals = [[7,10],[2,4]]
print(S.minMeetingRooms(intervals))