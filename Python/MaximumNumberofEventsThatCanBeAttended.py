"""
Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
Example 4:

Input: events = [[1,100000]]
Output: 1
Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
 

Constraints:

1 <= events.length <= 10^5
events[i].length == 2
1 <= events[i][0] <= events[i][1] <= 10^5
"""
class Solution_1:
    def maxEvents(self, events) -> int:
        events = sorted(events, key = lambda x:(x[1]-x[0],x[0],x[1]))
        print(events)
        res = 0
        curr = events[0][0]
        for start,end in events:
            curr = max(curr,start)
            if curr <= end:
                res += 1
                curr += 1
            # print(start,end)
            # print('res:',curr,res)
        return res

import heapq
class Solution:
    def maxEvents(self, events) -> int:
        """
        sort events based on the start date, the end date of events that got the same date are pushed into a priority queue, the events that end sooner will be taken first
        """
        events = sorted(events, reverse = True)
        # print('events:',events)
        q = []
        res, d = 0, 0 #use d to record current day
        while events or q:
            # print(events)

            if not q:
                d = events[-1][0]
            while events and events[-1][0] <= d: #start date of the event <=  current day, can still attend
                heapq.heappush(q, events.pop()[1])
            #     print('q:',q)
            # print('d:',d)
            # print('q:',q)
            heapq.heappop(q) #q can not be empty, because if so we push d in it, pop the event the got the most early end date

            res += 1
            d += 1 #attend 1 event, take one day
            
            while q and q[0] < d: #current day already larger than the close day of the event, so the events can not be taken any longer
                heapq.heappop(q)
        return res




S = Solution()


events = [[1,2],[2,3],[3,4]]
print(S.maxEvents(events))

events = [[1,2],[2,3],[3,4],[1,2]]
print(S.maxEvents(events))

events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
print(S.maxEvents(events))

events = [[1,100000]]
print(S.maxEvents(events))

events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
print(S.maxEvents(events))

events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
print(S.maxEvents(events))
