"""
There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
 

Note:

The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
"""

# https://leetcode.com/problems/course-schedule-iii/discuss/396812/Python-heap-que-explained?
# We start learning courses with earliest closing date first. If we find a course that can't fit into its close date, we can un-learn one of the previous course in order to fit it in. We can safely un-learn a previous course because it closes earlier and there is no way for it to be picked up again later. We pick up the one with longest learning time to un-learn, if the longest learning time happend to be the newly added course, then it is equivalent to not learning the newly added course.


import heapq
class Solution:
    def scheduleCourse(self, courses) -> int:
        courses.sort(key=lambda x:(x[1], x[0]))
        q, curr = [], 0
        for duration, end in courses:
            heapq.heappush(q, -duration)
            curr += duration
            if curr > end:
                curr += heapq.heappop(q)
        return len(q)


S = Solution()
courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
print(S.scheduleCourse(courses))