"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: [[7,10],[2,4]]
Output: true
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/meeting-rooms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals = sorted(intervals)
        pre_e = -1
        for s, e in intervals:
            if s < pre_e:
                return False
            pre_e = e
        return True


S = Solution()
intervals = [[0,30],[5,10],[15,20]]
print(S.canAttendMeetings(intervals))
intervals = [[7,10],[2,4]]
print(S.canAttendMeetings(intervals))