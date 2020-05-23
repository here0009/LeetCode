"""
Implement the class TweetCounts that supports two methods:

1. recordTweet(string tweetName, int time)

Stores the tweetName at the recorded time (in seconds).
2. getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)

Returns the total number of occurrences for the given tweetName per minute, hour, or day (depending on freq) starting from the startTime (in seconds) and ending at the endTime (in seconds).
freq is always minute, hour or day, representing the time interval to get the total number of occurrences for the given tweetName.
The first time interval always starts from the startTime, so the time intervals are [startTime, startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ... , [startTime + delta*i, min(startTime + delta*(i+1), endTime + 1)> for some non-negative number i and delta (which depends on freq).  
 

Example:

Input
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

Output
[null,null,null,null,[2],[2,1],null,[4]]

Explanation
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // All tweets correspond to "tweet3" with recorded times at 0, 10 and 60.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // return [2]. The frequency is per minute (60 seconds), so there is one interval of time: 1) [0, 60> - > 2 tweets.
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // return [2, 1]. The frequency is per minute (60 seconds), so there are two intervals of time: 1) [0, 60> - > 2 tweets, and 2) [60,61> - > 1 tweet.
tweetCounts.recordTweet("tweet3", 120);                            // All tweets correspond to "tweet3" with recorded times at 0, 10, 60 and 120.
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // return [4]. The frequency is per hour (3600 seconds), so there is one interval of time: 1) [0, 211> - > 4 tweets.
 

Constraints:

There will be at most 10000 operations considering both recordTweet and getTweetCountsPerFrequency.
0 <= time, startTime, endTime <= 10^9
0 <= endTime - startTime <= 10^4
"""
import bisect
from collections import defaultdict
class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort(self.tweets[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int):
        res = []
        if freq == 'minute':
            gap = 60
        elif freq == 'hour':
            gap  = 60*60
        elif freq == 'day':
            gap = 24*60*60
        querries = self.tweets[tweetName]
        i = startTime
        res = []
        while i <= endTime:
            j = min(i + gap, endTime+1) #j was not included in the tweet counts
            res.append(bisect.bisect_left(querries, j) - bisect.bisect_left(querries, i))
            i += gap
        # print(res)
        return res
# import bisect       
# class TweetCounts:

#     def __init__(self):
#         self.a = defaultdict(list)

#     def recordTweet(self, tn: str, time: int) -> None:
#         bisect.insort(self.a[tn], time)
       
#     def getTweetCountsPerFrequency(self, freq: str, tn: str, startTime: int, endTime: int):
#         delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
#         i = startTime
#         res = []
#         while i <= endTime:
#             j = min(i + delta, endTime+1)
#             res.append(bisect_left(self.a[tn], j) - bisect_left(self.a[tn], i))
#             i += delta
#         print(res)
#         return res        


# Your TweetCounts object will be instantiated and called as such:
obj = TweetCounts()
obj.recordTweet("tweet3", 0)
obj.recordTweet("tweet3", 60)
obj.recordTweet("tweet3", 10)                             
obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 59) 
obj.getTweetCountsPerFrequency("minute", "tweet3", 0, 60) 
obj.recordTweet("tweet3", 120)                            
obj.getTweetCountsPerFrequency("hour", "tweet3", 0, 210)  