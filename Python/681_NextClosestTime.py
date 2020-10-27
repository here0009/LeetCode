"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-closest-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def nextClosestTime(self, time: str) -> str:
        def addOne(hour, minutes):
            """
            add one minute to time
            """
            h, rmd = divmod(minutes+1, 60)
            return (hour + h)%24, rmd

        hour, minutes = [int(s) for s in time.split(':')]
        digits = set(list(''.join(time.split(':'))))
        # print(time, digits)
        while True:
            hour, minutes = addOne(hour, minutes)
            string_time = '{:02d}{:02d}'.format(hour, minutes)
            tmp = set(list(string_time))
            # print(hour, minutes, tmp, string_time)
            if len(tmp - digits) == 0:
                return '{:02d}:{:02d}'.format(hour, minutes)
        return None

from itertools import product
class Solution:
    def nextClosestTime(self, time: str) -> str:
        def timDiff(lst):
            h, m = int(''.join(lst[:2])), int(''.join(lst[2:]))
            if h > 23 or m > 59:
                return float('inf')
            else:
                diff_time = (h - hour)*60 + m - minutes
                if diff_time <= 0:
                    diff_time += 24*60
                return diff_time

        diff = float('inf')
        hour, minutes = [int(s) for s in time.split(':')]
        digits = set(list(''.join(time.split(':'))))
        res = None
        for lst in product(digits, repeat=4):
            tmp = timDiff(lst)
            if tmp < diff:
                diff = tmp
                res = '{}:{}'.format(lst[0]+lst[1], lst[2]+lst[3])
        return res


S = Solution()
time = "19:34"
print(S.nextClosestTime(time))
time = "23:59"
print(S.nextClosestTime(time))
time = "01:32"
print(S.nextClosestTime(time))
time = "01:32"
print(S.nextClosestTime(time))