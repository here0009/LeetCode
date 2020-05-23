"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""
import datetime
class Solution_1:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        d = datetime.date(year, month, day)
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        return days[d.weekday()]


#https://en.wikipedia.org/wiki/Zeller%27s_congruence
#Zellar fomular
class Solution:
    def dayOfTheWeek(self, d, m, y):
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if m < 3:
            m += 12
            y -= 1
        c, y = y//100, y % 100
        w = (c//4 - 2 * c + y + y//4 + 13*(m+1)//5 + d - 1) % 7
        print(w)
        return days[w]

s = Solution()
day = 31
month = 8
year = 2019
print(s.dayOfTheWeek(day, month, year))

day = 18
month = 7
year = 1999
print(s.dayOfTheWeek(day, month, year))

day = 15
month = 8
year = 1993
print(s.dayOfTheWeek(day, month, year))

day = 1
month = 1
year = 1
print(s.dayOfTheWeek(day, month, year))
#1,1,1 is Monday

day = 14
month = 10
year = 2019
print(s.dayOfTheWeek(day, month, year))
#1,1,1 is Monday