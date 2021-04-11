"""
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

 

Example 1:

Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.
Example 2:

Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]
 

Constraints:

1 <= cars.length <= 105
1 <= positioni, speedi <= 106
positioni < positioni+1
"""


from typing import List
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        """
        TLE:78 / 83 个通过测试用例
        """
        res = []
        speed_pos_time =[[float('inf')] * 3]
        while cars:
            curr_pos, curr_speed = cars.pop()
            # print(curr_pos, curr_speed)
            # print(speed_pos_time)
            # print(res[::-1])
            if curr_speed <= speed_pos_time[0][0]:  # current speed is slower than the most slow speed int speed_list
                res.append(-1)
                speed_pos_time = [[curr_speed, curr_pos, float('inf')]]
            else:
                for _s, _p, _t in speed_pos_time[::-1]:
                    if curr_speed <= _s:
                        continue
                    curr_time = (_p - curr_pos) / (curr_speed - _s)
                    if curr_time <= _t:
                        speed_pos_time.append([curr_speed, curr_pos, curr_time])
                        res.append(curr_time)
                        break
        return res[::-1]


from typing import List
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        res = []
        speed_pos_time =[[float('inf')] * 3]
        while cars:
            curr_pos, curr_speed = cars.pop()
            if curr_speed <= speed_pos_time[0][0]:  # current speed is slower than the most slow speed int speed_list
                res.append(-1)
                speed_pos_time = [[curr_speed, curr_pos, float('inf')]]
            else:
                while speed_pos_time:
                    _s, _p, _t = speed_pos_time[-1]
                    if curr_speed <= _s:
                        speed_pos_time.pop()
                        continue
                    curr_time = (_p - curr_pos) / (curr_speed - _s)
                    if curr_time > _t:
                        speed_pos_time.pop()
                    else:
                        speed_pos_time.append([curr_speed, curr_pos, curr_time])
                        res.append(curr_time)
                        break
        return res[::-1]

S = Solution()
cars = [[1,2],[2,1],[4,3],[7,2]]
print(S.getCollisionTimes(cars))
cars = [[3,4],[5,4],[6,3],[9,1]]
print(S.getCollisionTimes(cars))
