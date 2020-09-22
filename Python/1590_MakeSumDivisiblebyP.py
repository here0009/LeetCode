"""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.

 

Example 1:

Input: nums = [3,1,4,2], p = 6
Output: 1
Explanation: The sum of the elements in nums is 10, which is not divisible by 6. We can remove the subarray [4], and the sum of the remaining elements is 6, which is divisible by 6.
Example 2:

Input: nums = [6,3,5,2], p = 9
Output: 2
Explanation: We cannot remove a single element to get a sum divisible by 9. The best way is to remove the subarray [5,2], leaving us with [6,3] with sum 9.
Example 3:

Input: nums = [1,2,3], p = 3
Output: 0
Explanation: Here the sum is 6. which is already divisible by 3. Thus we do not need to remove anything.
Example 4:

Input: nums = [1,2,3], p = 7
Output: -1
Explanation: There is no way to remove a subarray in order to get a sum divisible by 7.
Example 5:

Input: nums = [1000000000,1000000000,1000000000], p = 3
Output: 0
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= p <= 109
"""


class Solution:
    def minSubarray(self, nums, p: int) -> int:
        """
        TLE
        """
        tmp, preSum = 0, [0]
        length = len(nums)
        for num in nums:
            tmp = (tmp + num) % p
            preSum.append(tmp)
        total = preSum[-1]
        # print(preSum)
        for l in range(length):
            for i in range(length-l+1):
                if (total - (preSum[i+l] - preSum[i])) % p == 0:
                    return l
        return -1

class Solution:
    def minSubarray(self, nums, p: int) -> int:
        tmp, length = 0, len(nums)
        total = sum(nums)
        if total < p:
            return -1
        elif total % p == 0:
            return 0
        else:
            total = total % p
        pos_dict = {0: 0}
        res = length
        for i in range(1, length+1):
            tmp = (tmp + nums[i-1]) % p
            target = (tmp - total) % p
            if target in pos_dict:
                res = min(res, i - pos_dict[target])
            pos_dict[tmp] = i
        return res if res != length else -1

class Solution:
    def minSubarray(self, A, p):
        need = sum(A) % p
        dp = {0: -1}
        cur = 0
        res = n = len(A)
        for i, a in enumerate(A):
            cur = (cur + a) % p
            dp[cur] = i
            if (cur - need) % p in dp:
                res = min(res, i - dp[(cur - need) % p])
        return res if res < n else -1
S = Solution()
nums = [3,1,4,2]
p = 6
print(S.minSubarray(nums, p))
nums = [6,3,5,2]
p = 9
print(S.minSubarray(nums, p))
nums = [1,2,3]
p = 3
print(S.minSubarray(nums, p))
nums = [1,2,3]
p = 7
print(S.minSubarray(nums, p))
nums = [1000000000,1000000000,1000000000]
p = 3
print(S.minSubarray(nums, p))
nums = [4,4,2]
p = 7
print(S.minSubarray(nums, p))
nums =[8,32,31,18,34,20,21,13,1,27,23,22,11,15,30,4,2]
p = 148
print(S.minSubarray(nums, p))