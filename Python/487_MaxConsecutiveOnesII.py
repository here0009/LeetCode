"""
Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-consecutive-ones-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        pre, curr = 0, 0
        res = 0
        for num in nums:
            if num == 1:
                curr += 1
            elif num == 0:
                pre = curr
                curr = 0
            # print(num, pre, curr)
            res = max(pre + curr + 1, res)
        return min(res, len(nums))

class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        gap, nogap, res = 0, 0, 0
        for num in nums:
            if num == 0:
                gap = nogap + 1
                nogap = 0
            elif num == 1:
                gap += 1
                nogap += 1
            res = max(res, gap)
        return res


S = Solution()
nums = [1,0,1,1,0,1,1,1,1]
print(S.findMaxConsecutiveOnes(nums))
nums = [0,0,0]
print(S.findMaxConsecutiveOnes(nums))
nums = [1]
print(S.findMaxConsecutiveOnes(nums))
# 输出：
# 4050
# 预期结果：
# 4432