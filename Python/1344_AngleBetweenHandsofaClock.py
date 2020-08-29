"""
Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
Example 1:

Input: hour = 12, minutes = 30
Output: 165
Example 2:



Input: hour = 3, minutes = 30
Output: 75
Example 3:



Input: hour = 3, minutes = 15
Output: 7.5
Example 4:

Input: hour = 4, minutes = 50
Output: 155
Example 5:

Input: hour = 12, minutes = 0
Output: 0
 

Constraints:

1 <= hour <= 12
0 <= minutes <= 59
Answers within 10^-5 of the actual value will be accepted as correct.
"""


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m = (minutes) * 6
        h = (hour + minutes/60) % 12 * 30
        # print(h, m)
        return min((h-m)% 360, (m-h)%360)

S = Solution()
hour = 12
minutes = 30
print(S.angleClock(hour, minutes))
hour = 3
minutes = 30
print(S.angleClock(hour, minutes))
hour = 3
minutes = 15
print(S.angleClock(hour, minutes))
hour = 4
minutes = 50
print(S.angleClock(hour, minutes))
hour = 12
minutes = 0
print(S.angleClock(hour, minutes))

hour = 1
minutes = 57
print(S.angleClock(hour, minutes))