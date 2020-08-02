"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit.
Example:
Input: [2,1,5,6,2,3]
Output: 10
"""
# Back to the problem, the current bar here is stack.pop(), i is the first bar in the right with height lower than current bar and stack[-1] is the first bar in the left with height not higher than current bar (here introduces the non strict maximum with replacing 'lower' to 'not higher', though it wouldn't influence the final result because we will reach that maximum through another bar). In this case, the maximum rectangular of each bar is not calculated one by one along the index, instead bar with peak-like shape will be calculated first. stack stores all the indexes of bars haven't got their maximum rectangular because r is not reached yet.
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
class Solution:
    def largestRectangleArea(self, heights) -> int:
        heights.append(0)
        stack = [-1]
        res = 0
        for i, v in enumerate(heights):
            # print(stack)
            while v < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                res = max(res, h * w)
            stack.append(i)
        return res

class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left = [1]*n
        right = [1]*n
        for i in range(1,n):
            j = i - 1
            while j>=0 and heights[j] >= heights[i]:
                j -= left[j]
            left[i] = i - j
        for i in range(n-2,-1,-1):
            j = i + 1
            while j < len(heights) and heights[i] <= heights[j]:
                j += right[j] 
            right[i] = j - i
        res = 0
        for i in range(n):
            res = max(res,heights[i]*(left[i]+right[i]-1))
        return res

        
S = Solution()
heights = [2,1,5,6,2,3]
print(S.largestRectangleArea(heights))