"""
There are n engineers numbered from 1 to n and two arrays: speed and efficiency, where speed[i] and efficiency[i] represent the speed and efficiency for the i-th engineer respectively. Return the maximum performance of a team composed of at most k engineers, since the answer can be a huge number, return this modulo 10^9 + 7.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. 

 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 

Constraints:

1 <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8
1 <= k <= n
"""

import heapq
class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        """
        sort by speed, descending order.
        try to replace the engineer if its efficiency > min_efficiency in the current dict
        at most k, do not need exactly k workers, should modify it
        """
        M = 10**9+7
        n = len(speed)
        if k == 1:
            return max(efficiency[i]*speed[i] for i in range(n))%M

        engineers = sorted([i for i in range(n)], key = lambda x:(speed[x], efficiency[x]), reverse = True)
        print(engineers)
        selected = [(efficiency[eng],speed[eng]) for eng in engineers[:k]]
        heapq.heapify(selected) #sort by efficiency
        print(selected)
        eff1, spd1 = selected[0]
        total_speed = sum([spd for eff,spd in selected])
        for i in range(k,n):
            spd2, eff2 = speed[engineers[i]], efficiency[engineers[i]]
            if eff2 > eff1:
                next_eff, next_speed = heapq.nsmallest(2,selected)[-1] #second smallest eff
                perform1 = total_speed*eff1
                total_speed2 = total_speed-spd1+spd2
                perform2 = next_eff*total_speed2
                if perform2 >= perform1:
                    total_speed = total_speed2
                    heapq.heappushpop(selected,(eff2,spd2))
                    eff1, spd1 = selected[0] #min efficiency and the corresponding speed

        return total_speed*eff1

import heapq
class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        """
        hire people from most efficiency to least efficiency
        the performance is current_efficiency*total_speed
        """
        M = 10**9+7
        n = len(speed)
        engineers = sorted([(efficiency[i], speed[i]) for i in range(n)], reverse = True)
        total_speed = 0
        res = 0
        selected = []
        for eff,spd in engineers:
            heapq.heappush(selected, spd)
            total_speed += spd
            if len(selected) > k:
                total_speed -= heapq.heappop(selected) #lay off the min speed
            res = max(res, eff*total_speed)
        return res % M

S = Solution()
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
print(S.maxPerformance(n,speed, efficiency, k))
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3
print(S.maxPerformance(n,speed, efficiency, k))
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 4
print(S.maxPerformance(n,speed, efficiency, k))

n = 3
speed = [2,8,2]
efficiency =[2,7,1]
k = 2
print(S.maxPerformance(n,speed, efficiency, k))


