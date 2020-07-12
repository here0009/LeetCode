"""
A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:


Answers within 10^-5 of the actual value will be accepted.

 

Example 1:


Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
Example 2:


Input: positions = [[1,1],[3,3]]
Output: 2.82843
Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
Example 3:

Input: positions = [[1,1]]
Output: 0.00000
Example 4:

Input: positions = [[1,1],[0,0],[2,0]]
Output: 2.73205
Explanation: At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, but locating it at [1, 0] will make the sum of distances = 3.
Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
Be careful with the precision!
Example 5:

Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
Output: 32.94036
Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.
 

Constraints:

1 <= positions.length <= 50
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 100
"""

from math import sqrt
class Solution:
    def getMinDistSum(self, positions) -> float:
        def totalDist(i,j):
            res = 0
            for p,q in positions:
                res += sqrt((i - p)**2 + (j - q)**2)
            return res

        curr_i, curr_j = 0, 0
        length = len(positions)
        for i,j in positions:
            curr_i += i
            curr_j += j
        curr_i /= length
        curr_j /= length
        res = totalDist(curr_i, curr_j)
        lower_limit = 10**-7
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        walk = 100
        # print(curr_i,curr_j)
        while walk > lower_limit:
            # print(curr_i,curr_j)
            flag = -1
            for i in range(len(directions)):
                di, dj = directions[i]
                tmp = totalDist(curr_i+walk*di, curr_j+walk*dj)
                # print(walk, di, dj, tmp, res)
                if tmp < res:
                    flag = i
                    res = tmp
            if flag != -1:
                # print(flag, curr_i, walk)
                curr_i += walk*directions[flag][0]
                curr_j += walk*directions[flag][1]
            else:
                walk = walk/2
        return res
# https://leetcode.com/problems/best-position-for-a-service-centre/discuss/731599/Weiszfeld's-algorithm
import math
class Solution:
    def getMinDistSum(self, positions) -> float:
        n = len(positions)
        if n == 1: return 0.0
        preans = float('inf')
        ans = 0
        # Use mean point as the initial point
        x, y = [sum(i) for i in zip(*positions)]
        def distancesum(x, y):
            temp = 0
            for a, b in positions:
                temp += math.sqrt(abs(x - a) ** 2 + abs(y - b) ** 2)
            return temp
        
        def bottomsum(x, y):
            res = 0
            for a, b in positions:
                temp = math.sqrt(abs(x - a) ** 2 + abs(y - b) ** 2)
                # Handle 0 exception
                if temp == 0: continue
                res += 1 / temp 
            return res
        
        def uppersum(x, y):
            xx = 0
            yy = 0
            for a, b in positions:
                temp = math.sqrt(abs(x - a) ** 2 + abs(y - b) ** 2)
                # Handle 0 exception
                if temp == 0: continue
                xx += a / temp
                yy += b / temp
            return (xx, yy)
        
        def weis(x, y):
            xx, yy = uppersum(x, y)
            bottom = bottomsum(x, y)
            # Handle 0 exception
            if bottom == 0:
                return (x, y)
            return (xx / bottom, yy / bottom)
        
        # Iterate Weiszfeld until the improvement is insignificant
        while abs(ans - preans) > 1e-7:
            preans = ans
            x, y = weis(x, y)
            ans = distancesum(x, y)
        
        return ans

S = Solution()
positions = [[0,1],[1,0],[1,2],[2,1]]
print(S.getMinDistSum(positions))
positions = [[1,1],[3,3]]
print(S.getMinDistSum(positions))
positions = [[1,1]]
print(S.getMinDistSum(positions))
positions = [[1,1],[0,0],[2,0]]
print(S.getMinDistSum(positions))
positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]        
print(S.getMinDistSum(positions))

positions = [[4,4],[52,89],[76,60],[4,4],[4,4],[93,59],[50,92],[4,4],[76,14],[4,4],[46,41],[4,4],[4,4],[4,4],[4,4],[67,14],[73,71],[83,44],[4,4],[4,4],[4,4],[4,4],[30,29],[74,77],[4,4],[4,4],[4,4],[26,62],[4,4],[4,4],[50,30],[44,93]]
print(S.getMinDistSum(positions))