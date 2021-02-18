"""
You are given an integer array, nums, and an integer k. nums comprises of only 0's and 1's. In one move, you can choose two adjacent indices and swap their values.

Return the minimum number of moves required so that nums has k consecutive 1's.

 

Example 1:

Input: nums = [1,0,0,1,0,1], k = 2
Output: 1
Explanation: In 1 move, nums could be [1,0,0,0,1,1] and have 2 consecutive 1's.
Example 2:

Input: nums = [1,0,0,0,0,0,1,1], k = 3
Output: 5
Explanation: In 5 moves, the leftmost 1 can be shifted right until nums = [0,0,0,0,0,1,1,1].
Example 3:

Input: nums = [1,1,0,1], k = 2
Output: 0
Explanation: nums already has 2 consecutive 1's.
 

Constraints:

1 <= nums.length <= 105
nums[i] is 0 or 1.
1 <= k <= sum(nums)
"""


from typing import List
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        """
        Thoughts:
        pos = [index]
        """
        pos = [i for i, v in enumerate(nums) if v == 1]  # index of ones
        pos = [i - j for j, i in enumerate(pos)]  # the moves that we need to put i and i + 1 is pos[i + 1] - pos[i]
        med, rmd = divmod(k, 2)
        res = 0
        # print(pos)
        for i in range(k):
            res += abs(pos[i] - pos[med])
        # print(pos, res)
        # print(res, len(pos) - k + 1)
        curr = res
        for i in range(1, len(pos) - k + 1):
            if rmd == 0:  # if k is odd, the median value of two sides will vanish to 0, so we do not need to update it. if k is even, there will be an extra median value on the right, so we need to update it.
                curr += pos[med + 1] - pos[med]
            # only record the nums that their sign changed
            curr -= pos[med] + pos[med + 1]  # the old med new med both shift to left
            curr += pos[i + k - 1] + pos[i - 1]  # add pos[i-1] that is minused, pos[i + k - 1] slippe in
            res = min(res, curr)
            med += 1
        return res


class Solution_1:
    def minMoves(self, nums: List[int], k: int) -> int:
        # we use a rolling window, which keeps indices of consecutive k appearences of 1s
        # lets say the index of 1s in current window is A = [a0, a1, ... ak-1]
        # then we are trying to find an index x, such that
        # we transform A to consecutive indices [x, x+1, ... x+k-1].
        # Notice the moves needed is |a0 - x| + |a1 - (x+1)| + ... + |a(k-1) - (x+k-1)|
        # do a little transformation -> |a0-x| + |(a1-1) - x| + |(a(k-1) - (k-1)) - x|
        # it is obvious that when x is the median of [a0, a1-1, a2-2, ... a(k-1) - (k-1)]
        # the solution reach the minimum
        # Also, notice that if we shift A for any constant, that is for each i, ai -> ai+a,
        # the median x changes but the summation does not change
        # therefore, for ith occurence of 1, we subtract its index with k, ai -> ai-i.
        # To find the rolling maximum value of c = |a0-x| + |(a1-1) - x| + |(a(k-1) - (k-1)) - x|
        # we just need to update the value instead of recalculating. 
        # When we update the median from x -> y, for the first
        # half A we add (y-x) to each of them, for the second half of A we subtract (y-x)
        # and we need to remove |a0-x| and include |ak-y| where ak is the next index of 1
        
        ones = []
        for i in range(len(nums)):
            if nums[i] == 1:
                ones.append(i - len(ones))
                
        # rolling window
        cur = 0
        # calculate initial summation
        
        med = k//2
        for i in range(k):
            cur += abs(ones[i] - ones[med])
        print(ones, cur)
        res = cur
        # rolling window update 
        for i in range(1, len(ones) - k + 1):
            # find median of ones[i:i+k]
            new_med = k//2+i
            if k%2==0:
                # if k is odd, the sum of abs difference will not change excluding the first value
                cur += ones[new_med] - ones[med] 
            # update first value and last value
            cur -= ones[med] - ones[i-1]
            cur += ones[i+k-1] - ones[new_med]
            med = new_med
            res = min(res, cur)
        return res
        

S = Solution()
nums = [1,0,0,1,0,1]
k = 2
print(S.minMoves(nums, k))
nums = [1,0,0,0,0,0,1,1]
k = 3
print(S.minMoves(nums, k))
nums = [1,1,0,1]
k = 2
print(S.minMoves(nums, k))
nums = [1,0,0,1,0,1,1,1,0,1,1]
k = 7
print(S.minMoves(nums, k))
# Output
# 4
# Expected
# 6