"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

 

Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:

The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""

from collections import Counter
class Solution:
    """
    either need to insert idle based on the occurrance of the most common values, or we do not need to inset idle at all, so it is len(tasks)
    """
    def leastInterval(self, tasks, n: int) -> int:
        c_tasks = Counter(tasks)
        max_v = max(c_tasks.values())
        max_v_counts = sum([1 for v in c_tasks.values() if v == max_v])
        return max(len(tasks),(max_v-1)*(n+1) + max_v_counts)


from collections import deque

s = Solution()
tasks = ["A","A","A","B","B","B"]
n = 2
print(s.leastInterval(tasks,n))

tasks = ["A","A","A","B","B","B"]
n = 0
print(s.leastInterval(tasks,n))