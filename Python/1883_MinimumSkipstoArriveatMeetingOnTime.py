"""
You are given an integer hoursBefore, the number of hours you have to travel to your meeting. To arrive at your meeting, you have to travel through n roads. The road lengths are given as an integer array dist of length n, where dist[i] describes the length of the ith road in kilometers. In addition, you are given an integer speed, which is the speed (in km/h) you will travel at.

After you travel road i, you must rest and wait for the next integer hour before you can begin traveling on the next road. Note that you do not have to rest after traveling the last road because you are already at the meeting.

For example, if traveling a road takes 1.4 hours, you must wait until the 2 hour mark before traveling the next road. If traveling a road takes exactly 2 hours, you do not need to wait.
However, you are allowed to skip some rests to be able to arrive on time, meaning you do not need to wait for the next integer hour. Note that this means you may finish traveling future roads at different hour marks.

For example, suppose traveling the first road takes 1.4 hours and traveling the second road takes 0.6 hours. Skipping the rest after the first road will mean you finish traveling the second road right at the 2 hour mark, letting you start traveling the third road immediately.
Return the minimum number of skips required to arrive at the meeting on time, or -1 if it is impossible.

 

Example 1:

Input: dist = [1,3,2], speed = 4, hoursBefore = 2
Output: 1
Explanation:
Without skipping any rests, you will arrive in (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 hours.
You can skip the first rest to arrive in ((1/4 + 0) + (3/4 + 0)) + (2/4) = 1.5 hours.
Note that the second rest is shortened because you finish traveling the second road at an integer hour due to skipping the first rest.
Example 2:

Input: dist = [7,3,5,5], speed = 2, hoursBefore = 10
Output: 2
Explanation:
Without skipping any rests, you will arrive in (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 hours.
You can skip the first and third rest to arrive in ((7/2 + 0) + (3/2 + 0)) + ((5/2 + 0) + (5/2)) = 10 hours.
Example 3:

Input: dist = [7,3,5,5], speed = 1, hoursBefore = 10
Output: -1
Explanation: It is impossible to arrive at the meeting on time even if you skip all the rests.
 

Constraints:

n == dist.length
1 <= n <= 1000
1 <= dist[i] <= 105
1 <= speed <= 106
1 <= hoursBefore <= 107
"""


import math
from typing import List
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:

        def calc(skip):
            pass
            

        min_time = sum([d/speed for d in dist])
        if min_time > hoursBefore:
            return -1
        left, right = 0, len(dist)
        while left < right:
            mid = (left + right) // 2
            if not calc(mid):
                left = mid + 1
            else:
                right = mid
        return left


# https://leetcode-cn.com/problems/minimum-skips-to-arrive-at-meeting-on-time/solution/minimum-skips-to-arrive-at-meeting-on-ti-dp7v/
from typing import List
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:

        length = len(dist)
        dp = [[float('inf')] * (length + 1) for _ in range(length + 1)]
        dp[0][0] = 0

        for i in range(1, length + 1):
            for j in range(i + 1):
                if j != 0:
                    dp[i][j] = min(dp[i - 1][j - 1] + dist[i - 1], dp[i][j])
                if j != i:
                    dp[i][j] = min(dp[i][j], math.ceil((dp[i - 1][j] + dist[i - 1]) / speed) * speed)
        # for row in dp:
        #     print(row)
        for j in range(length):
            if dp[-1][j] <= speed * hoursBefore:
                return j
        return -1


# https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time/discuss/1239772/Python-dp-O(n2)
class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n=len(dist)
        dp=[[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0]=0
            
        for i,d in enumerate(dist,1):
            dp[i][0]=(dp[i-1][0]+d+speed-1)//speed*speed
            for j in range(1,i+1):
                dp[i][j]=min(dp[i-1][j-1]+d,(dp[i-1][j]+d+speed-1)//speed*speed)
                
        for j,t in enumerate(dp[-1]):
            if t<=speed*hoursBefore:
                return j
        return -1

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        eps=1e-9
        
        n=len(dist)
        dp=[[10**10 for _ in range(n+1)] for _ in range(n+1)]
        dp[0][0]=0
            
        for i,d in enumerate(dist,1):
            dp[i][0]=ceil(dp[i-1][0]+d/speed-eps)
            for j in range(1,i+1):
                dp[i][j]=min(dp[i-1][j-1]+d/speed,ceil(dp[i-1][j]+d/speed-eps))
                
        for j,t in enumerate(dp[-1]):
            if t<=hoursBefore:
                return j
        return -1

S = Solution()
dist = [1,3,2]
speed = 4
hoursBefore = 2
print(S.minSkips(dist, speed, hoursBefore))
dist = [7,3,5,5]
speed = 2
hoursBefore = 10
print(S.minSkips(dist, speed, hoursBefore))
dist = [7,3,5,5]
speed = 1
hoursBefore = 10
print(S.minSkips(dist, speed, hoursBefore))
