"""
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

 

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
 

Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
"""
class Solution:
    """
    TLE
    """
    def corpFlightBookings(self, bookings, n: int):
        res = [0]*n
        for start, end, seats  in bookings:
            for i in range(start-1, end):
                res[i] += seats
        return res

class Solution:
    """
    record the day seats were added and the day it was removed, then accumulate the sequence
    """
    def corpFlightBookings(self, bookings, n: int):
        res = [0]*(n+2)
        for start,end,seats in bookings:
            res[start] += seats
            res[end+1] -= seats
        for i in range(1,len(res)):
            res[i] += res[i-1]
        return res[1:-1]

s = Solution()
bookings = [[1,2,10],[2,3,20],[2,5,25]]
n = 5
print(s.corpFlightBookings(bookings, n))


