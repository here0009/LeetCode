"""
A conveyor belt has packages that must be shipped from one port to another within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed. 
Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
 

Note:

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500
"""
class Solution_1:
    def shipWithinDays(self, weights, D: int) -> int:
        res_min = max(weights)
        comb_days_min = 1
        comb_days_max = len(weights) - D + 1
        pre_sum = []
        tmp = 0
        for w in weights:
            tmp += w
            pre_sum.append(tmp)

        print(pre_sum)
        total = sum(weights)
        remain_sum = [total - w for w in pre_sum]
        print(remain_sum)
        return 0

class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        min_cap = max(weights) #the days needed can be caluculated
        max_cap = sum(weights) #1 day all the packages will be shipped

        low, high = min_cap, max_cap
        while low < high:
            mid = (low + high) // 2
            total = 0
            days = 1
            for weight in weights:
                if total + weight > mid:
                    days += 1
                    total = weight
                else:
                    total += weight
            if days <= D:
                high = mid # mid meet the requirment, try a number between low and mid, but do not drop mid, becuase mid-1 may not meet he requirment.
            else:
                low = mid + 1
        return low


s = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
print(s.shipWithinDays(weights,D))

weights = [3,2,2,4,1,4]
D = 3
print(s.shipWithinDays(weights,D))

weights = [1,2,3,1,1]
D = 4
print(s.shipWithinDays(weights,D))