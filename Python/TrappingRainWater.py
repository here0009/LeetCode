"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height) -> int:
        stack = []
        res = 0
        for h in height:
            # print(h, stack, res)
            count = 1
            while len(stack) > 1 and h > stack[-1]:  # pop element between left and right
                res += min(stack[0], h) - stack.pop()
                if h < stack[0]:
                    count += 1  # left may be form new valley with higher right, count the gaps between them
                # stack.append(min_h)
            if stack and h > stack[0]:# pop left
                stack.pop()
            stack.extend([h]*count)
        return res

# https://leetcode.com/problems/trapping-rain-water/discuss/17528/Easy-to-understand-Python-10-line-60ms-O(n)
class Solution:
    def trap(self, height) -> int:
        waterLevel = []
        left = 0
        for h in height:
            left = max(left, h)
            waterLevel += [left]
        right = 0
        for i,h in reversed(list(enumerate(height))): #keep the index, while find the right max
            right = max(right, h)
            waterLevel[i] = min(waterLevel[i], right) - h
        return sum(waterLevel)


class Solution:
    def trap(self, height) -> int:
        length = len(height)
        leftMax, rightMax = [], []
        left, right = 0, 0
        for h in height:
            left = max(left, h)
            leftMax += [left]
        for h in reversed(height):
            right = max(right, h)
            rightMax += [right]
        rightMax = rightMax[::-1]
        # print(leftMax)
        # print(rightMax)
        res = sum(min(leftMax[i], rightMax[i])-height[i] for i in range(length))
        return res


class Solution:
    def trap(self, height) -> int:
        length = len(height)
        left, right = 0, length-1
        leftMax, rightMax = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < leftMax:
                    res += leftMax - height[left]
                else:
                    leftMax = height[left]
                left += 1
            else:
                if height[right] < rightMax:
                    res += rightMax - height[right]
                else:
                    rightMax = height[right]
                right -= 1
        return res

S = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(S.trap(height))

height = [4,2,0,3,2,5]
print(S.trap(height))
# Output
# 7
# Expected
# 9