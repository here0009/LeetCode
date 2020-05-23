"""
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
"""
class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        """
        wrong answer, the new speed is not the faster one, but the slower one
        """

        if not position or not speed or len(position) != len(speed):
            return 0
        p_s = sorted(zip(position, speed))
        time = [(target-p_s[i][0])/p_s[i][1] for i in range(len(p_s))]
        pre = time[0]
        print(p_s)
        print(time)
        res = 1
        index = 1
        for i in range(1,len(time)):
            if pre > time[i]:
                res += 1
                pre = time[i]
        return res


class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        if not position or not speed or len(position) != len(speed):
            return 0
        p_s = sorted(zip(position, speed))
        time = [(target-p_s[i][0])/p_s[i][1] for i in range(len(p_s))][::-1]
        pre = time[0]
        res = 1
        for i in range(1,len(time)):
            if pre < time[i]:
                res += 1
                pre = time[i]
        return res     


S = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(S.carFleet(target, position, speed))

target = 10
position = []
speed = []
print(S.carFleet(target, position, speed))  

target = 10
position = [0,4,2]
speed = [2,1,3]
print(S.carFleet(target, position, speed))
# Output
# 2
# Expected
# 1