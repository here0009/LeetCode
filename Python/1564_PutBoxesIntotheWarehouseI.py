"""
You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labelled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes cannot be stacked.
You can rearrange the insertion order of the boxes.
Boxes can only be pushed into the warehouse from left to right only.
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
Return the maximum number of boxes you can put into the warehouse.

 

Example 1:


Input: boxes = [4,3,4,1], warehouse = [5,3,3,4,1]
Output: 3
Explanation: 

We can first put the box of height 1 in room 4. Then we can put the box of height 3 in either of the 3 rooms 1, 2, or 3. Lastly, we can put one box of height 4 in room 0.
There is no way we can fit all 4 boxes in the warehouse.
Example 2:


Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
Output: 3
Explanation: 

Notice that it's not possible to put the box of height 4 into the warehouse since it cannot pass the first room of height 3.
Also, for the last two rooms, 2 and 3, only boxes of height 1 can fit.
We can fit 3 boxes maximum as shown above. The yellow box can also be put in room 2 instead.
Swapping the orange and green boxes is also valid, or swapping one of them with the red box.
Example 3:

Input: boxes = [1,2,3], warehouse = [1,2,3,4]
Output: 1
Explanation: Since the first room in the warehouse is of height 1, we can only put boxes of height 1.
Example 4:

Input: boxes = [4,5,6], warehouse = [3,3,3,3,3]
Output: 0
 

Constraints:

n == warehouse.length
1 <= boxes.length, warehouse.length <= 10^5
1 <= boxes[i], warehouse[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse) -> int:
        """
        TLE
        """
        boxes.sort()
        print(boxes)
        res = 0
        w = len(warehouse)
        for b in boxes:
            iw = 0
            while iw < w and b <= warehouse[iw]:
                iw += 1
            if iw != 0:
                res += 1
                w = iw-1
            else:
                break
            # print(b, w, res)
        return res


from bisect import bisect_left
from collections import Counter
from collections import deque
class Solution:
    def maxBoxesInWarehouse(self, boxes, warehouse) -> int:
        """
        warehouse can be seen as a decreasing(non-increasing) sequence
        """
        # len_w = len(warehouse)
        boxes.sort()
        warehouse2 = Counter()
        tmp = warehouse[0]
        for w in warehouse:
            tmp = min(w, tmp)
            warehouse2[tmp] += 1

        dq = sorted(warehouse2.keys())
        res = 0
        for b in boxes:
            index = bisect_left(dq, b)
            if index == len(dq):
                break
            else:
                res += 1
                warehouse2[dq[index]] -= 1
                if warehouse2[dq[index]] == 0:
                    dq = dq[index+1:]
        return res


# 作者：AIResearcherJHM
# 链接：https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-i/solution/pythonpai-xu-tan-xin-by-airesearcherjhm/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True)
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i-1], warehouse[i])
        j = len(boxes)-1
        res = 0
        for i in range(len(warehouse)-1, -1, -1):
            if j < 0:
                break
            if warehouse[i] >= boxes[j]:
                res += 1
                j -= 1
        return res


S = Solution()
boxes = [4,3,4,1]
warehouse = [5,3,3,4,1]
print(S.maxBoxesInWarehouse(boxes, warehouse))
boxes = [1,2,2,3,4]
warehouse = [3,4,1,2]
print(S.maxBoxesInWarehouse(boxes, warehouse))
boxes = [1,2,3]
warehouse = [1,2,3,4]
print(S.maxBoxesInWarehouse(boxes, warehouse))
boxes = [4,5,6]
warehouse = [3,3,3,3,3]
print(S.maxBoxesInWarehouse(boxes, warehouse))