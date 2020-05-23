"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
 

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
 

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""
class Solution_1:
    def findRadius(self, houses, heaters) -> int:
        houses = sorted(houses)
        heaters = sorted(heaters)
        left, right = 0, len(heaters)-1
        def min_radius(pos, left, right):
            while left < right:
                middle = (left+right)//2
                res = abs(heaters[middle]-pos)
            return
        return

from bisect import bisect_left            
class Solution:
    def findRadius(self, houses, heaters) -> int:
        heaters = sorted(heaters)
        res, len_heaters = 0, len(heaters)
        for house in houses:
            index = bisect_left(heaters, house)
            if index == len_heaters:
                res = max(res, house-heaters[-1])
            elif index == 0:
                res = max(res, heaters[0]-house)
            else:
                res = max(res, min(house-heaters[index-1], heaters[index]-house))
        return res

s = Solution()
houses = [1,2,3]
heaters = [2]
print(s.findRadius(houses, heaters))

houses = [1,2,3,4]
heaters = [1,4]
print(s.findRadius(houses, heaters))