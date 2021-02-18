"""
You are given an integer array jobs, where jobs[i] is the amount of time it takes to complete the ith job.

There are k workers that you can assign jobs to. Each job should be assigned to exactly one worker. The working time of a worker is the sum of the time it takes to complete all jobs assigned to them. Your goal is to devise an optimal assignment such that the maximum working time of any worker is minimized.

Return the minimum possible maximum working time of any assignment.


Example 1:

Input: jobs = [3,2,3], k = 3
Output: 3
Explanation: By assigning each person one job, the maximum time is 3.
Example 2:

Input: jobs = [1,2,4,7,8], k = 2
Output: 11
Explanation: Assign the jobs the following way:
Worker 1: 1, 2, 8 (working time = 1 + 2 + 8 = 11)
Worker 2: 4, 7 (working time = 4 + 7 = 11)
The maximum working time is 11.

Constraints:

1 <= k <= jobs.length <= 12
1 <= jobs[i] <= 107
"""


from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        def dp(idx, status):
            # print(idx, status)
            if max(status) >= self.res:
                return
            if idx == len_jobs:
                self.res = min(self.res, max(status))
                return
            s2 = list(status)
            for i in range(k):
                if i > 0 and status[i] == status[i - 1]:
                    continue
                s2[i] = status[i] + jobs[idx]
                dp(idx + 1, tuple(s2))
                s2[i] = status[i]

        status = tuple([0] * k)
        len_jobs = len(jobs)
        self.res = float('inf')
        dp(0, status)
        return self.res

S = Solution()
jobs = [3,2,3]
k = 3
print(S.minimumTimeRequired(jobs, k))
jobs = [1,2,4,7,8]
k = 2
print(S.minimumTimeRequired(jobs, k))
jobs = [9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202]
k = 9
print(S.minimumTimeRequired(jobs, k))
jobs = [9899456,8291115,9477657,9288480,5146275,7697968,8573153,3582365,3758448,9881935,2420271,4542202]
k = 9
print(S.minimumTimeRequired(jobs, k))
