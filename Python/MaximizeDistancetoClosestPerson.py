"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        seats_string = ''.join([str(seat) for seat in seats])
        seats_split = seats_string.split('1')
        # print(seats_split)
        max_0s = max([len(seats_str) for seats_str in seats_split])*'0'
        return max(len(seats_split[0]), len(seats_split[-1]), int(len(max_0s)/2 + 0.5))
        # print(max_0s)
        # if seats_split[0] == max_0s or seats_split[-1] == max_0s:
        #     return len(max_0s)
        # else:
        #     return int(len(max_0s)/2 + 0.5)

# s = Solution()
# seats = [1,0,0,0,1,0,1]
# print(s.maxDistToClosest(seats))
# seats = [1,0,0,0]
# print(s.maxDistToClosest(seats))
# seats = [1,0,0,0,0,0,0,0,0,0]
# print(s.maxDistToClosest(seats))
# seats = [0,1]
# print(s.maxDistToClosest(seats))
# seats = [1,0,0,1]
# print(s.maxDistToClosest(seats))
# seats = [0,1,1,1,0,0,1,0,0]
# print(s.maxDistToClosest(seats))
seats = [0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,1]
# print(s.maxDistToClosest(seats))
# print(map(str,seats))
# l = map(str,seats)
# print(l)
# for i in l:
#     print (i)
print(list(map(str,seats)))
print(sum(map(lambda x: (x+1)*x, seats)))


