"""
Given an array A of integers, return the number of non-empty continuous subarrays that satisfy the following condition:

The leftmost element of the subarray is not larger than other elements in the subarray.

 

Example 1:

Input: [1,4,2,5,3]
Output: 11
Explanation: There are 11 valid subarrays: [1],[4],[2],[5],[3],[1,4],[2,5],[1,4,2],[2,5,3],[1,4,2,5],[1,4,2,5,3].
Example 2:

Input: [3,2,1]
Output: 3
Explanation: The 3 valid subarrays are: [3],[2],[1].
Example 3:

Input: [2,2,2]
Output: 6
Explanation: There are 6 valid subarrays: [2],[2],[2],[2,2],[2,2],[2,2,2].
 

Note:

1 <= A.length <= 50000
0 <= A[i] <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-valid-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def validSubarrays(self, nums) -> int:
        res = 0
        length = len(nums)
        # print(nums)
        for i in range(length):
            j = i + 1
            while j < length and nums[j] >= nums[i]:
                j += 1
            res += j - i
            # print(i, j, res)
        return res


from collections import deque
class Solution:
    def validSubarrays(self, nums) -> int:
        """
        decreasing queue
        """
        res = 0
        nums.append(-float('inf'))
        length = len(nums)
        dq = deque([])
        for i in range(length-1, -1, -1):
            v = nums[i]
            while dq and v <= dq[0][0]:
                dq.popleft()
            if dq:
                res += dq[0][1] - i
            dq.appendleft((v, i))
            # print(v, dq, res)
        return res


class Solution:
    def validSubarrays(self, nums) -> int:
        res = 0
        length = len(nums)
        stack = [(-float('inf'), length)]
        for i in range(length-1, -1, -1):
            v = nums[i]
            while v <= stack[-1][0]:
                stack.pop()
            res += stack[-1][1] - i
            stack.append((v, i))
        return res

# 作者：hao-shou-bu-juan
# 链接：https://leetcode-cn.com/problems/number-of-valid-subarrays/solution/python-dan-diao-zhan-ying-yong-zhao-xiao-yu-dang-q/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for i, val in enumerate(nums):
            while len(stack) > 0 and val < stack[-1][1]:
                ans += i - stack.pop()[0] # the nodes that start with stack[-1]
            stack.append((i, val))
            # print(i, val, stack, ans)

        # 还保存在栈里面的节点，右边没有比其小的节点，所以右边界是len(nums)
        # print(stack, ans)
        for pos, _ in stack:
            ans += len(nums) - pos
        return ans



S = Solution()
nums = [1,4,2,5,3]
print(S.validSubarrays(nums))
nums = [3,2,1]
print(S.validSubarrays(nums))
nums = [2,2,2]
print(S.validSubarrays(nums))
