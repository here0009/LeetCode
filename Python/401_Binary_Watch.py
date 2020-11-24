"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
# class Solution:
#     def readBinaryWatch(self, num: int):
#         vals = ['0']*10
#         #first 4 digits for hour, last 6 digits for minutes
#         res = []
#         def valid(vals):
            
            
#         def backtrack(n, vals):
#             if n == num:
#                 res.append(timeformat(vals))
#                 return
#             for i in range(11):
#                 if vals[i] == '0':
#                     vals[i] = '1'
#                     if valid(vals):
#                         backtrack(n+1, vals)
#                     vals[i] = '0'
#         return res


from itertools import combinations
class Solution:
    def readBinaryWatch(self, num: int):
        def generate(ones, total, threshold):
            """
            generate ones '1' in total postion, the number is valid if it is smaller than threshold
            """
            index = list(range(total))
            res = []
            for comb in combinations(index, ones):
                tmp = int(''.join(['1' if i in comb else '0' for i in list(range(total))]), 2)
                if tmp < threshold:
                    res.append(tmp)
            return res

        res = []
        for hour in range(5):
            minutes = num - hour
            if minutes < 0 or minutes > 6:
                continue
            h_list = generate(hour, 4, 12)
            m_list = generate(minutes, 6, 60)
            for h in h_list:
                for m in m_list:
                    res.append('{}:{:02}'.format(h, m))
        return res

# for lst in combinations(list(range(6)), 2):
#     print(lst)

S = Solution()
print(S.readBinaryWatch(1))