"""
In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

 

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
All integers in position are distinct.
2 <= m <= position.length
"""


import heapq
from bisect import bisect_left
class Solution:
    def maxDistance(self, position, m: int) -> int:
        position.sort()
        length = len(position)
        pq = [(position[0] - position[length-1], 0, length-1)]
        print(pq)
        m -= 2
        while m > 0 and pq:
            res, left, right = heapq.heappop(pq)
            if right - left <= 1:
                continue
            mid_num = (position[right] + position[left]) // 2
            mid = bisect_left(position, mid_num)
            if mid == right:
                mid -= 1
            elif mid == left:
                mid += 1
            print(pq, mid_num, mid, m)
            if mid > left:
                heapq.heappush(pq, (position[left]-position[mid],left, mid))
            if right > mid:
                heapq.heappush(pq, (position[mid]-position[right],mid, right))
            m -= 1
        print(pq)
        return min(-n for n, _, _ in pq)


class Solution:
    def maxDistance(self, position, m: int) -> int:
        def group(gap):
            target = position[0]
            res = 0
            for p in position:
                if p >= target:
                    res += 1
                    target = p + gap
            return res

        position.sort()
        left, right = 0, position[-1] - position[0]
        while left < right:
            mid = (left + right) // 2+1
            # print(left, right,mid)
            if group(mid) >= m:
                left = mid
            else:
                right = mid-1
        return left#, group(left)

# https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794070/Python-Binary-search-solution-with-explanation-and-similar-questions
# As a rule of thumb, use m = l + (r-l)//2 with l = m + 1 and r = m, and use m = r - (r-l)//2 with l = m and r = m - 1. This can prevent m from stucking at r (or l) after the updating step.
S = Solution()
position = [1,2,3,4,7]
m = 3
print(S.maxDistance(position, m))
position = [5,4,3,2,1,1000000000]
m = 2
print(S.maxDistance(position, m))
position = [1,2,3,4,5,6,7,8,9,10]
m = 4
print(S.maxDistance(position, m))
# Output:
# 2
# Expected:
# 3