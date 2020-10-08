"""
Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-transformed-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
from collections import deque
class Solution:
    def sortTransformedArray(self, nums, a: int, b: int, c: int):
        """
        stack method did not work, try to use method of -b/2a
        """
        @lru_cache(None)
        def f(x):
            return a*x**2 + b*x + c

        def dist(x):
            return abs(-b/(2*a)-x)

        if a == 0:
            res = [f(x) for x in nums]
            if b < 0:
                return res[::-1]
            return res
        print(nums)
        print([f(x) for x in nums])
        res = []
        stack = deque([])  
        if a > 0: # y got a min value, using a decreasing stack
            for num in nums:
                f_num = f(num)
                while stack and f_num >= stack[-1]:
                    res.append(stack.pop())
                stack.append(f_num)
            while stack:
                res.append(stack.pop())
            return res
        else: # y got a max value, using a increasing stack
            for num in nums:
                f_num = f(num)
                while stack and f_num <= stack[-1]:
                    res.append(stack.pop())
                stack.append(f_num)
            while stack:
                res.append(stack.popleft())
            return res[::-1]


from functools import lru_cache
class Solution:
    def sortTransformedArray(self, nums, a: int, b: int, c: int):
        """
        if a == 0, rearrange nums according to b
        resort nums based on its distance to -b/2a
        if a < 0, y is decreasing with the distance
        if a > 0, y is increasing with the distance
        """
        @lru_cache(None)
        def f(x):
            return a*x**2 + b*x + c

        @lru_cache(None)
        def dist(x):
            return abs(-b/(2*a)-x)

        if a == 0:
            res = [f(x) for x in nums]
            if b < 0:
                return res[::-1]
            return res

        res = []  # resort nums based on its distance to -b/2a
        left, right = 0, len(nums)-1
        while left <= right:
            dl, dr = dist(nums[left]), dist(nums[right])
            if dl >= dr:
                res.append(f(nums[left]))
                left += 1
            else:
                res.append(f(nums[right]))
                right -= 1
        if a > 0:  # y got a min value at x == -b/2a, res is increasing
            return res[::-1]
        else:
            return res



S = Solution()
nums = [-4,-2,2,4]
a = 1
b = 3
c = 5
print(S.sortTransformedArray(nums, a, b, c))
nums = [-4,-2,2,4]
a = -1
b = 3
c = 5
print(S.sortTransformedArray(nums, a, b, c))
nums =[-99,-94,-90,-88,-84,-83,-79,-68,-58,-52,-52,-50,-47,-45,-35,-29,-5,-1,9,12,13,25,27,33,36,38,40,46,47,49,57,57,61,63,73,75,79,97,98]
a = -2
b = 44
c = -56
print(S.sortTransformedArray(nums, a, b, c))
# 输出：
# [-24014,-21864,-20216,-19416,-17864,-17486,-16014,-12296,-9336,-7752,-7752,-7256,-6542,-6086,-4046,-3014,-326,-102,178,-4046,-14952,-14606,-9062,-8006,-7502,-5222,-4814,-4046,-2702,-2406,-2264,-1496,-1272,-1064,-782,-326,-206,178,184]
# 预期：
# [-24014,-21864,-20216,-19416,-17864,-17486,-16014,-14952,-14606,-12296,-9336,-9062,-8006,-7752,-7752,-7502,-7256,-6542,-6086,-5222,-4814,-4046,-4046,-4046,-3014,-2702,-2406,-2264,-1496,-1272,-1064,-782,-326,-326,-206,-102,178,178,184]