"""
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:




Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""
"""
Thoughts:
use a dict of dp, dp[t] store the max profit can be made till time t
update dp for every job
"""
from collections import defaultdict
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        """
        TLE, because in dp, i is increasing, we can use a list to store the information, and use bisect to find the insert point
        """
        dp = defaultdict(int)
        dp[1] = 0
        len_p = len(profit)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len_p)]
        jobs = sorted(jobs, key = lambda x:x[1]) #sort by start time
        for i in range(len_p):
            s,e,p = jobs[i]
            tmp = 0
            for t,v in dp.items():
                if s >= t :
                    tmp = max(tmp, v+p)
            dp[e] = max(dp.get(e,0), tmp) #sometime dp[e] will get smaller if you use dp[e] = tmp
        # print(dp)
        return max(dp.values())

from bisect import bisect
class Solution_1:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        dp = [[0,0]] #dp stores [time, profit], the max profit can be made by time. if a job can increase the max profit, we append it to dp, if not we do nothing
        len_p = len(profit)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(len_p)]
        jobs = sorted(jobs, key = lambda x:x[1]) #sort by start time
        for i in range(len_p):
            s,e,p = jobs[i]
            index = bisect(dp,[s+1]) - 1
            if dp[index][1] + p > dp[-1][1]:
                dp.append([e, dp[index][1] + p])
        # print(jobs)
        # print(dp)
        return dp[-1][1]



s = Solution()
startTime = [1,2,3,3]
endTime = [3,4,5,6]
profit = [50,10,40,70]
print(s.jobScheduling(startTime, endTime, profit))
startTime = [1,2,3,4,6]
endTime = [3,5,10,6,9]
profit = [20,20,100,70,60]
print(s.jobScheduling(startTime, endTime, profit))
startTime = [1,1,1]
endTime = [2,3,4]
profit = [5,6,4]
print(s.jobScheduling(startTime, endTime, profit))
startTime = [6,15,7,11,1,3,16,2]
endTime = [19,18,19,16,10,8,19,8]
profit = [2,9,1,19,5,7,3,19]
print(s.jobScheduling(startTime, endTime, profit))
# Output:
# 22
# Expected:
# 41


startTime = [43,13,36,31,40,5,47,13,28,16,2,11]
endTime = [44,22,41,41,47,13,48,35,48,26,21,39]
profit = [8,20,3,19,16,8,11,13,2,15,1,1]
# Output:
# 55
# Expected:
# 66
print(s.jobScheduling(startTime, endTime, profit))
