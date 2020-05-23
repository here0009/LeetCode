"""
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
 

Constraints:

1 <= hours.length <= 10000
0 <= hours[i] <= 16

"""
class Solution:
    def longestWPI(self, hours) -> int:
        """
        TLE, use a dict to store the tmp information
        """
        res = 0
        dp = [0]
        tmp = 0
        for hour in hours:
            if hour > 8:
                tmp += 1
            else:
                tmp -= 1
            dp.append(tmp)
        # print(dp)
        len_dp = len(dp)
        
        pre_start,pre_end = 0,0
        end = len_dp - 1
        while end > 0:
            if dp[end] > 0:
                pre_end = end
                break
            end -= 1
        res = pre_end - pre_start

        for start in range(1,len_dp):
            if dp[start] < dp[pre_start]:
                end = pre_end
                while end < len_dp - 1:
                    if dp[end] > dp[start]:
                        pre_end = end
                    end += 1
                if pre_end-start > res:
                        pre_start = start
                        res = pre_end-start
        return res

class Solution:
    def longestWPI(self, hours) -> int:
        total = 0
        res = 0
        total_dict = {0:-1}
        for i,hour in enumerate(hours):
            if hour > 8:
                total += 1
            else:
                total -= 1
            if total > 0:
                res = i+1
            elif total-1 in total_dict:
                res = max(res, i-total_dict[total-1])
            if total not in total_dict:
                total_dict[total] = i
            
        # print(total_dict)
        return res

s = Solution()
hours = [9,9,6,0,6,6,9]
print(s.longestWPI(hours))

hours = [9,6,9]
print(s.longestWPI(hours))

hours = [9,9,9]
print(s.longestWPI(hours))
