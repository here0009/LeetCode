"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        res = []
        for i,v in enumerate(nums):
            while dq and dq[0][1] <= i-k:
                dq.popleft()
            tmp = nums[i]
            while dq and tmp >= dq[-1][0]:
                dq.pop()
            dq.append((tmp,i))
            res.append(dq[0][0])
        return res[k-1:]

"""
https://leetcode.com/problems/sliding-window-maximum/discuss/65885/This-is-a-typical-monotonic-queue-problem

What does Monoqueue do here:
It has three basic options:
push: push an element into the queue; O (1) (amortized)
pop: pop an element out of the queue; O(1) (pop = remove, it can't report this element)
max: report the max element in queue;O(1)
It takes only O(n) time to process a N-size sliding window minimum/maximum problem.
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        res = []
        for i,v in enumerate(nums):
            while dq and nums[dq[-1]] <= v:
                dq.pop()
            while dq and dq[0] == i-k:
                dq.popleft()
            dq.append(i)
            # print(dq)
            res.append(nums[dq[0]])
        return res[k-1:]

S = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(S.maxSlidingWindow(nums,k))
nums = [1,-1]
k = 1
print(S.maxSlidingWindow(nums,k))
# Output
# [1,1]
# Expected
# [1,-1]
nums = [7,2,4]
k = 2
print(S.maxSlidingWindow(nums,k))
