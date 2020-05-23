"""
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 

Note:

1 <= time.length <= 60000
1 <= time[i] <= 500
"""
class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        remainder = [t%60 for t in time]
        # print(remainder)
        remainder_dict = {}
        res = 0
        for r in remainder:
            cmp_r = (60 - r)%60
            res += remainder_dict.get(cmp_r,0)
            remainder_dict[r] = remainder_dict.get(r,0) + 1
        # print(remainder_dict)
        return res

s = Solution()
time = [30,20,150,100,40]
print(s.numPairsDivisibleBy60(time))

time = [60,60,60]
print(s.numPairsDivisibleBy60(time))

time = [60]
print(s.numPairsDivisibleBy60(time))