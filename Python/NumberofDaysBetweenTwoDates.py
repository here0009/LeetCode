"""
Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

 

Example 1:

Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
Example 2:

Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.

"""
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        print(date1.split('-'))
        y1,m1,d1 = [int(s) for s in date1.split('-')]
        y2,m2,d2 = [int(s) for s in date2.split('-')]
        c1 = datetime(y1,m1,d1)
        c2 = datetime(y2,m2,d2)
        return abs(c1-c2).days

S = Solution()
date1 = "2019-06-29"
date2 = "2019-06-30"
print(S.daysBetweenDates(date1, date2))
date1 = "2020-01-15"
date2 = "2019-12-31"
print(S.daysBetweenDates(date1, date2))