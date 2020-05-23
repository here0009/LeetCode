"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
"""
class Solution:
    def dayOfYear(self, date: str) -> int:
        m_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        year, months, days = [int(s) for s in date.split('-')]
        if( year % 4 == 0 and year  % 100 != 0) or year % 400 == 0:
            m_days[1] += 1
        res = sum(m_days[:months-1]) + days
        return res

s = Solution()

date = "2019-01-09"
print(s.dayOfYear(date))

date = "2019-02-10"
print(s.dayOfYear(date))

date = "2003-03-01"
print(s.dayOfYear(date))

date = "2004-03-01"
print(s.dayOfYear(date))

date = "2016-02-29"
print(s.dayOfYear(date))
