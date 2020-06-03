"""
A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

 

Example 1:



Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
 

Constraints:

1 <= n <= 10^9
1 <= reservedSeats.length <= min(10*n, 10^4)
reservedSeats[i].length == 2
1 <= reservedSeats[i][0] <= n
1 <= reservedSeats[i][1] <= 10
All reservedSeats[i] are distinct.
"""


from collections import defaultdict
class Solution:
    """
    TLE
    """
    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        def fourseats(i,j):
            if all((j+k) not in reservedSeats_dict[i] for k in range(4)):
                self.res += 1
                return True
            return False

                
        self.res = 0
        reservedSeats_dict = defaultdict(set)
        for i,j in reservedSeats:
            reservedSeats_dict[i].add(j)
        print(reservedSeats_dict)
        for row in range(1, n+1):
            if row not in reservedSeats_dict:
                self.res += 2
                continue
            if fourseats(row,2):
                fourseats(row,6)
            else:
                if not fourseats(row, 4):
                    fourseats(row, 6)
        return self.res


from functools import lru_cache
from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats) -> int:
        @lru_cache(None)
        def numofSeats(seats):
            n = 0
            if fourseats(seats,2):
                n += 1
                if fourseats(seats,6):
                    n += 1
            else:
                if fourseats(seats, 4):
                    n += 1
                else:
                    if fourseats(seats, 6):
                        n += 1
            # print(seats, n)
            return n

        def fourseats(seats,j):
            if all((j+k) not in seats for k in range(4)):
                return True
            return False

        res = 0
        reservedSeats_dict = defaultdict(list)
        for i,j in reservedSeats:
            reservedSeats_dict[i].append(j)
        # print(reservedSeats_dict)
        res = 2*n
        for row in reservedSeats_dict:
            seats = tuple(sorted(reservedSeats_dict[row]))
            res -= 2 - numofSeats(seats)
            # print(row, res)
        return res


S = Solution()
n = 3
reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
print(S.maxNumberOfFamilies(n, reservedSeats))
n = 2
reservedSeats = [[2,1],[1,8],[2,6]]
print(S.maxNumberOfFamilies(n, reservedSeats))
n = 4
reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
print(S.maxNumberOfFamilies(n, reservedSeats))