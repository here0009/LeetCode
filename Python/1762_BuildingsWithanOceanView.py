"""
There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

 

Example 1:

Input: heights = [4,2,3,1]
Output: [0,2,3]
Explanation: Building 1 (0-indexed) does not have an ocean view because building 2 is taller.
Example 2:

Input: heights = [4,3,2,1]
Output: [0,1,2,3]
Explanation: All the buildings have an ocean view.
Example 3:

Input: heights = [1,3,2,4]
Output: [3]
Explanation: Only building 3 has an ocean view.
Example 4:

Input: heights = [2,2,2,2]
Output: [3]
Explanation: Buildings cannot see the ocean if there are buildings of the same height to its right.
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/buildings-with-an-ocean-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        res = []
        max_height = -float('inf')
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                res.append(i)
            max_height = max(heights[i], max_height)
        return res[::-1]

S = Solution()
heights = [4,2,3,1]
print(S.findBuildings(heights))
heights = [4,3,2,1]
print(S.findBuildings(heights))
heights = [1,3,2,4]
print(S.findBuildings(heights))
heights = [2,2,2,2]
print(S.findBuildings(heights))