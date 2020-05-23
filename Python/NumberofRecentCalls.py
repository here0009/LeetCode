"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

 

Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]
 

Note:

Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
"""
from collections import deque
class RecentCounter_1:
    """
    Thoughts: time exceeded
    """
    def __init__(self):
        self.records = queue.Queue()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.records.put(t)
        counts = 0
        new_queue = queue.Queue()
        while not self.records.empty():
            record = self.records.get()
            # print(t, record)
            if t - record <= 3000 :
                counts += 1
                new_queue.put(record)
        self.records = new_queue

        # self.records = records_copy
        return counts


class RecentCounter_2:
    """
    Thoughts: time exceeded
    """
    def __init__(self):
        self.records = []
        self.start = None

    def ping(self, t):
        self.records.append(t)
        if not self.start:
            self.start = 0
        counts = 0
        for index, record in enumerate(self.records[self.start:]):
            if t - record <= 3000:
                counts += 1
            else:
                self.start = index
        return counts

class RecentCounter:

    def __init__(self):
        self.records = deque()


    def ping(self, t):
        self.records.append(t)
        while t - self.records[0] > 3000 :
            self.records.popleft()
        return len(self.records)
     


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
t_list = [1,100,3001,3002]
for t in t_list:
    print(obj.ping(t))


# t_list = [39187,45399,50662,70693,72666,84380,105653,129301,156166,156423,158304,211387,277101,299683,315559,476340,599798,603055,754499,763079,770210,784063,827501,832252,885804,915659,925527,931410,948409,991628]
# for t in t_list:
#     print(obj.ping(t))