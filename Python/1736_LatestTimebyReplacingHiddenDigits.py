"""
You are given a string time in the form of hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

 

Example 1:

Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
Example 2:

Input: time = "0?:3?"
Output: "09:39"
Example 3:

Input: time = "1?:22"
Output: "19:22"
 

Constraints:

time is in the format hh:mm.
It is guaranteed that you can produce a valid time from the given string.
"""


class Solution:
    def maximumTime(self, time: str) -> str:
        hour, minute = time.split(':')
        res_hour, res_minute = list(hour), list(minute)

        if hour == '??':
            res_hour = list('23')
        elif hour[0] == '?':
            if ord(hour[1]) <= ord('3'):
                res_hour[0] = '2'
            else:
                res_hour[0] = '1'
        elif hour[1] == '?':
            if hour[0] == '2':
                res_hour[1] = '3'
            else:
                res_hour[1] = '9'

        # if minute == '??':
        #     res_minute = list('59')
        if minute[0] == '?':
            res_minute[0] = '5'
        if minute[1] == '?':
            res_minute[1] = '9'
        return ':'.join([''.join(res_hour), ''.join(res_minute)])

S = Solution()
time = "2?:?0"
print(S.maximumTime(time))
time = "0?:3?"
print(S.maximumTime(time))
time = "1?:22"
print(S.maximumTime(time))
time = "10:53"
print(S.maximumTime(time))
time = "?0:15"
print(S.maximumTime(time))
