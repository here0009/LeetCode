"""
You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.
Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

 

Example 1:


Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.
Example 2:

Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7
Example 3:

Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3
 

Constraints:

1 <= heights.length <= 105
1 <= heights[i] <= 106
0 <= bricks <= 109
0 <= ladders <= heights.length
"""


class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        def check(n):
            lst = sorted([v for v, _ in gaps[:n]], reverse = True)
            return bricks >= sum(lst[ladders:])

        gaps = []
        length = len(heights)
        for i in range(1, length):
            if heights[i] > heights[i-1]:
                gaps.append((heights[i] - heights[i-1], i))
        if ladders >= len(gaps):
            return length
        left, right = 0, len(gaps)
        # print(heights, bricks, ladders, gaps)
        if check(right):
            return length-1
        # for i in range(0, right+1):
        #     print(i, check(i))
        while left < right:
            mid = (left + right)//2
            # print(left, right, mid)
            if check(mid):
                left = mid+1
            else:
                right = mid
        #  gas[left-1][1] is the postion can not reach
        # print(gaps, left, mid, right)
        if left == 0:
            return gaps[0][1]-1
        return gaps[left-1][1]-1
"""
1. 使用gaps数组储存可能遇到的上坡以及此时的index
2. check(n)函数验证使用bricks和ladders可否克服长度为n的gaps
3. left = 0, right = len(gaps), 使用check函数二分查找可以通过的最多gap， 返回结果
"""
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        def check(n):
            """
            return True if we can get over gaps[:n] else False
            """
            lst = sorted([v for v, _ in gaps[:n]], reverse=True)
            return bricks >= sum(lst[ladders:]) # lst[:ladders] is get over by ladders, lst[ladder:] is get over by bricks

        gaps = []
        length = len(heights)
        for i in range(1, length):
            if heights[i] > heights[i-1]:
                gaps.append((heights[i] - heights[i-1], i))
        left, right = 0, len(gaps)

        if right == 0 or check(right):
            return length-1

        while left < right:
            mid = (left + right)//2
            # print(left, right, mid)
            if check(mid):
                left = mid+1
            else:
                right = mid

        if left == 0:  # left is the min length of gaps we can not get over
            return gaps[0][1]-1
        return gaps[left-1][1]-1

import heapq
class Solution:
    def furthestBuilding(self, heights, bricks: int, ladders: int) -> int:
        length = len(heights)
        curr = 0
        pq = []
        for i in range(1, length):
            d = heights[i] - heights[i-1]
            if d > 0:
                heapq.heappush(pq, d)
                if len(pq) > ladders:
                    curr += heapq.heappop(pq)
                if curr > bricks:
                    return i-1
        return length-1


S = Solution()
heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1
print(S.furthestBuilding(heights, bricks, ladders))
heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2
print(S.furthestBuilding(heights, bricks, ladders))
heights = [14,3,19,3]
bricks = 17
ladders = 0
print(S.furthestBuilding(heights, bricks, ladders))

heights = [17,16,5,10,10,14,7]
bricks = 74
ladders =6
print(S.furthestBuilding(heights, bricks, ladders))

heights = [1,5,1,2,3,4]
bricks = 4
ladders = 1
print(S.furthestBuilding(heights, bricks, ladders))
