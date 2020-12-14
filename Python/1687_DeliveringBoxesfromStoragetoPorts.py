"""
You have the task of delivering some boxes from storage to their ports using only one ship. However, this ship has a limit on the number of boxes and the total weight that it can carry.

You are given an array boxes, where boxes[i] = [ports​​i​, weighti], and three integers portsCount, maxBoxes, and maxWeight.

ports​​i is the port where you need to deliver the ith box and weights i is the weight of the ith box.
portsCount is the number of ports.
maxBoxes and maxWeight are the respective box and weight limits of the ship.
The boxes need to be delivered in the order they are given. The ship will follow these steps:

The ship will take some number of boxes from the boxes queue, not violating the maxBoxes and maxWeight constraints.
For each loaded box in order, the ship will make a trip to the port the box needs to be delivered to and deliver it. If the ship is already at the correct port, no trip is needed, and the box can immediately be delivered.
The ship then makes a return trip to storage to take more boxes from the queue.
The ship must end at storage after all the boxes have been delivered.

Return the minimum number of trips the ship needs to make to deliver all boxes to their respective ports.

 

Example 1:

Input: boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
Output: 4
Explanation: The optimal strategy is as follows: 
- The ship takes all the boxes in the queue, goes to port 1, then port 2, then port 1 again, then returns to storage. 4 trips.
So the total number of trips is 4.
Note that the first and third boxes cannot be delivered together because the boxes need to be delivered in order (i.e. the second box needs to be delivered at port 2 before the third box).
Example 2:

Input: boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
Output: 6
Explanation: The optimal strategy is as follows: 
- The ship takes the first box, goes to port 1, then returns to storage. 2 trips.
- The ship takes the second, third and fourth boxes, goes to port 3, then returns to storage. 2 trips.
- The ship takes the fifth box, goes to port 3, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.
Example 3:

Input: boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
Output: 6
Explanation: The optimal strategy is as follows:
- The ship takes the first and second boxes, goes to port 1, then returns to storage. 2 trips.
- The ship takes the third and fourth boxes, goes to port 2, then returns to storage. 2 trips.
- The ship takes the fifth and sixth boxes, goes to port 3, then returns to storage. 2 trips.
So the total number of trips is 2 + 2 + 2 = 6.
Example 4:

Input: boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7
Output: 14
Explanation: The optimal strategy is as follows:
- The ship takes the first box, goes to port 2, then storage. 2 trips.
- The ship takes the second box, goes to port 2, then storage. 2 trips.
- The ship takes the third and fourth boxes, goes to port 3, then storage. 2 trips.
- The ship takes the fifth box, goes to port 3, then storage. 2 trips.
- The ship takes the sixth and seventh boxes, goes to port 3, then port 4, then storage. 3 trips. 
- The ship takes the eighth and ninth boxes, goes to port 1, then port 5, then storage. 3 trips.
So the total number of trips is 2 + 2 + 2 + 2 + 3 + 3 = 14.
 

Constraints:

1 <= boxes.length <= 105
1 <= portsCount, maxBoxes, maxWeight <= 105
1 <= ports​​i <= portsCount
1 <= weights i <= maxWeight
"""


from typing import List
from functools import lru_cache
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        """
        TLE
        """
        @lru_cache(None)
        def dp(index):
            if index == len_b:
                return 0
            res = dp(index + 1)  # pack up, go to port of boxes[index][0], and go back
            b, w, pre_port = 0, 0, boxes[index][0]
            trips = 0
            while index < len_b and b + 1 <= maxBoxes and w + boxes[index][1] <= maxWeight:
                p, _w = boxes[index]
                b += 1
                w += _w
                trips += (p != pre_port)
                pre_port = p
                index += 1
                res = min(res, trips + dp(index))
            return res + 2

        len_b = len(boxes)
        return dp(0)


from typing import List
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        """
        TLE
        """
        def dp(index):
            # print(index, self.memo)
            if self.memo[index] != float('inf'):
                return self.memo[index]
            pre_i = index
            res = dp(index + 1)  # pack up, go to port of boxes[index][0], and go back
            b, w, pre_port = 0, 0, boxes[index][0]
            trips = 0
            while index < len_b and b + 1 <= maxBoxes and w + boxes[index][1] <= maxWeight:
                p, _w = boxes[index]
                b += 1
                w += _w
                trips += (p != pre_port)
                pre_port = p
                index += 1
                res = min(res, trips + dp(index))
            self.memo[pre_i] = res + 2
            return self.memo[pre_i]

        len_b = len(boxes)
        self.memo = [float('inf')] * len_b + [0]
        dp(0)
        # print(self.memo)
        return self.memo[0]


from typing import List
from functools import lru_cache
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        """
        take as much boxes as possible, only when the current log's last port == the next log's first port, when can try to combine them. it might -1 one trip in current log.
        """
        @lru_cache(None)
        def dp(index):
            if index == len_b:
                return 0
            j = index
            b, w, pre_port = 0, 0, boxes[j][0]
            trips = 0
            pre_j = j
            while j < len_b and b + 1 <= maxBoxes and w + boxes[j][1] <= maxWeight:
                p, _w = boxes[j]
                b += 1
                w += _w
                if p != pre_port:
                    trips += 1
                    pre_port = p
                    pre_j = j  # record the index that diff
                j += 1
            res = trips + dp(j)
            if pre_j != j and pre_j != index and pre_j != len_b - 1 and boxes[pre_j][0] == boxes[pre_j + 1][0]: 
                res = min(res, trips - 1 + dp(pre_j))  # divide from pre_j, so trip - 1
            # res = dp(j + 1)  # pack up, go to port of boxes[index][0], and go back
            return res + 2

        len_b = len(boxes)
        return dp(0)
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/discuss/969723/JavaC%2B%2BPython-Sliding-Window-O(N)-Solution
class Solution:
    def boxDelivering(self, A, portsCount, B, W):
        n = len(A)
        
        # need: needed trips from i to j for this shipment
        need = j = lastj = 0
        
        # dp records the minimal number of the trips to deliver i box
        # dp[1] means we delivered the first (0th) box
        dp = [0] + [float('inf')] * n
        
        # i is left pointer, j is the right pointer
        for i in range(n):
            
            # while we haven't run out of boxes and weight capacity
            # we can keep expanding the right pointer j
            while j < n and B > 0 and W >= A[j][1]:
                
                # we reduce the box and weight capacity
                B -= 1
                W -= A[j][1]
                
                # if the port is different from the previous port
                if j == 0 or A[j][0] != A[j - 1][0]:
                    # we need to add the number of needed trip by 1
                    # lastj moves to current position to mark the start of boxes with different ports
                    lastj = j
                    need += 1
                
                # keep expanding the right pointer when we can
                j += 1
            
            # greedies solution: if we keep loading as far right as we can
            dp[j] = min(dp[j], dp[i] + need + 1)  # one for goes back
            
            # second greedies solution: if we decide to sacrifice a little weight to save a trip
            dp[lastj] = min(dp[lastj], dp[i] + need)
            
            # now as we move the left pointer i forward (don't put the ith box in this trip), 
            # we increase the number of available boxes and available weights
            B += 1
            W += A[i][1]
            
            # if this box is different from the prior box
            # we removed the prior box, so the needed trip is reduced by 1.
            if i == n - 1 or A[i][0] != A[i + 1][0]:
                need -= 1
                
        return dp[-1]


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        start_from = 0
        port_count = 0
        cur_w = 0
        cur_b = 0
        DP = [0] * (n+1)

        for i in range(n):
            cur_w += boxes[i][1]
            cur_b += 1
            if i == 0 or boxes[i][0] != boxes[i-1][0]:
                port_count += 1
            while cur_b > maxBoxes or cur_w > maxWeight or (start_from < i and DP[start_from] == DP[start_from+1]):
                cur_b -= 1
                cur_w -= boxes[start_from][1]
                if boxes[start_from][0] != boxes[start_from+1][0]:
                    port_count -= 1
                start_from += 1
            DP[i+1] = DP[start_from]+port_count+1
        return DP[n]      

S = Solution()
boxes = [[1,1],[2,1],[1,1]]
portsCount = 2
maxBoxes = 3
maxWeight = 3
print(S.boxDelivering(boxes, portsCount, maxBoxes, maxWeight))
boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]]
portsCount = 3
maxBoxes = 3
maxWeight = 6
print(S.boxDelivering(boxes, portsCount, maxBoxes, maxWeight))
boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]]
portsCount = 3
maxBoxes = 6
maxWeight = 7
print(S.boxDelivering(boxes, portsCount, maxBoxes, maxWeight))
boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]]
portsCount = 5
maxBoxes = 7
print(S.boxDelivering(boxes, portsCount, maxBoxes, maxWeight))