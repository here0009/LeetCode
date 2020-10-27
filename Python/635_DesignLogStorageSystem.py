"""
You are given several logs, where each log contains a unique ID and timestamp. Timestamp is a string that has the following format: Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All domains are zero-padded decimal numbers.

Implement the LogSystem class:

LogSystem() Initializes the LogSystem object.
void put(int id, string timestamp) Stores the given log (id, timestamp) in your storage system.
int[] retrieve(string start, string end, string granularity) Returns the IDs of the logs whose timestamps are within the range from start to end inclusive. start and end all have the same format as timestamp, and granularity means how precise the range should be (i.e. to the exact Day, Minute, etc.). For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", and granularity = "Day" means that we need to find the logs within the inclusive range from Jan. 1st 2017 to Jan. 2nd 2017, and the Hour, Minute, and Second for each log entry can be ignored.
 

Example 1:

Input
["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]
Output
[null, null, null, null, [3, 2, 1], [2, 1]]

Explanation
LogSystem logSystem = new LogSystem();
logSystem.put(1, "2017:01:01:23:59:59");
logSystem.put(2, "2017:01:01:22:59:59");
logSystem.put(3, "2016:01:01:00:00:00");

// return [3,2,1], because you need to return all logs between 2016 and 2017.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year");

// return [2,1], because you need to return all logs between Jan. 1, 2016 01:XX:XX and Jan. 1, 2017 23:XX:XX.
// Log 3 is not returned because Jan. 1, 2016 00:00:00 comes before the start of the range.
logSystem.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour");
 

Constraints:

1 <= id <= 500
2000 <= Year <= 2017
1 <= Month <= 12
1 <= Day <= 31
0 <= Hour <= 23
0 <= Minute, Second <= 59
granularity is one of the values ["Year", "Month", "Day", "Hour", "Minute", "Second"].
At most 500 calls will be made to put and retrieve.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-log-storage-system
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import bisect
class LogSystem:
    """
    we can use dict or inordered list to store the time information, but the put and retrieve times is relatively small, we ty dict fist
    """
    def __init__(self):
        self.units = ["Year", "Month", "Day", "Hour", "Minute", "Second"]
        self.timeline = []
        self.length = 14

    def strToInt(self, timestamp):
        return int(''.join(timestamp.split(':')))

    def put(self, id: int, timestamp: str) -> None:
        timestamp = self.strToInt(timestamp)
        bisect.insort(self.timeline, (timestamp, id))
        # print(self.timeline)

    def retrieve(self, start: str, end: str, granularity: str):
        index = self.units.index(granularity)
        start_pre = ''.join(start.split(':')[:index+1])
        end_pre = ''.join(end.split(':')[:index+1])
        zeros = self.length - len(start_pre)
        start_time = int(start_pre + '0'*zeros)
        end_time = int(str(int(end_pre) + 1) + '0'*zeros)
        # print(start_time, end_time)
        left = bisect.bisect_left(self.timeline, (start_time, 0))
        right = bisect.bisect_left(self.timeline, (end_time, 0))
        return [v for _, v in self.timeline[left:right]]

# 作者：Alexhanbing
# 链接：https://leetcode-cn.com/problems/design-log-storage-system/solution/miao-chu-jie-guo-by-alexhanbing/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class LogSystem:
    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None:
        self.logs.append((id, timestamp))

    def retrieve(self, s: str, e: str, gra: str):
        bits_num_map = {"Year":4, "Month":7, "Day": 10, "Hour": 13, "Minute": 16, "Second":19}
        bits_num = bits_num_map.get(gra)
        s, e = s[:bits_num], e[:bits_num]
        res = []
        for id, time in self.logs:
            time = time[:bits_num]
            if s <= time <= e:
                res.append(id)
        return res



# Your LogSystem object will be instantiated and called as such:
obj = LogSystem()
print(obj.put(1, "2017:01:01:23:59:59"))
print(obj.put(2, "2017:01:01:22:59:59"))
print(obj.put(3, "2016:01:01:00:00:00"))
print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))
print(obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))