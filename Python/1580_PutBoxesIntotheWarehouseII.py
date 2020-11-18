"""
You are given two arrays of positive integers, boxes and warehouse, representing the heights of some boxes of unit width and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labeled from 0 to n - 1 from left to right where warehouse[i] (0-indexed) is the height of the ith room.

Boxes are put into the warehouse by the following rules:

Boxes cannot be stacked.
You can rearrange the insertion order of the boxes.
Boxes can be pushed into the warehouse from either side (left or right)
If the height of some room in the warehouse is less than the height of a box, then that box and all other boxes behind it will be stopped before that room.
Return the maximum number of boxes you can put into the warehouse.

 

Example 1:


Input: boxes = [1,2,2,3,4], warehouse = [3,4,1,2]
Output: 4
Explanation:

We can store the boxes in the following order:
1- Put the yellow box in room 2 from either the left or right side.
2- Put the orange box in room 3 from the right side.
3- Put the green box in room 1 from the left side.
4- Put the red box in room 0 from the left side.
Notice that there are other valid ways to put 4 boxes such as swapping the red and green boxes or the red and orange boxes.
Example 2:


Input: boxes = [3,5,5,2], warehouse = [2,1,3,4,5]
Output: 3
Explanation:

It's not possible to put the two boxes of height 5 in the warehouse since there's only 1 room of height >= 5.
Other valid solutions are to put the green box in room 2 or to put the orange box first in room 2 before putting the green and red boxes.
Example 3:

Input: boxes = [1,2,3], warehouse = [1,2,3,4]
Output: 3
Example 4:

Input: boxes = [4,5,6], warehouse = [3,3,3,3,3]
Output: 0
 

Constraints:

n == warehouse.length
1 <= boxes.length, warehouse.length <= 105
1 <= boxes[i], warehouse[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse = True)
        from_left, from_right = [], []
        length = len(warehouse)
        tmp = float('inf')
        for w in warehouse:
            tmp = min(w, tmp)
            from_left.append(tmp)
        tmp = float('inf')
        for w in warehouse[::-1]:
            tmp = min(w, tmp)
            from_right.append(tmp)
        from_right = from_right[::-1]
        warehouse2 = [float('inf')] + [max(from_left[i], from_right[i]) for i in range(length)] + [float('inf')]
        # print('+++++++++++++')
        # print(boxes, warehouse)
        # print(from_left, from_right)
        # print(warehouse2)
        left = warehouse2.index(min(warehouse2))
        right = left + 1
        res = 0
        while boxes and (left > 0 or right < length+1):
            # print(boxes, left, right)
            if left > 0 and warehouse2[left] <= warehouse2[right]:
                curr = warehouse2[left]
                left -= 1
            elif right < length+1:
                curr = warehouse2[right]
                right += 1
            if curr >= boxes[-1]:
                # print(curr, boxes[-1])
                res += 1
                boxes.pop()
        return res


# 作者：intoloop
# 链接：https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-ii/solution/python-by-intoloop-18/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        warehouseLeft=warehouse[::]
        warehouseRight=warehouse[::]
        n=len(warehouse)
        for i in range(1,n):
            if warehouseLeft[i]>warehouseLeft[i-1]:
                warehouseLeft[i]=warehouseLeft[i-1]
            if warehouseRight[n-1-i]>warehouseRight[n-1-i+1]:
                warehouseRight[n-1-i]=warehouseRight[n-i]
        
        for i in range(n):
            warehouse[i]=max(warehouseRight[i],warehouseLeft[i])
        boxes.sort(reverse=True)
        
        i,j,k=0,n-1,0
        res=0 
        while i<=j and k<len(boxes):  #先尝试放大的box，会简单很多
            if warehouse[i]>=boxes[k]:
                i+=1
                res+=1
            elif warehouse[j]>=boxes[k]:
                j-=1
                res+=1
            k+=1
        return res
        



S = Solution()
# boxes = [1,2,2,3,4]
# warehouse = [3,4,1,2]
# print(S.maxBoxesInWarehouse(boxes, warehouse))
# boxes = [3,5,5,2]
# warehouse = [2,1,3,4,5]
# print(S.maxBoxesInWarehouse(boxes, warehouse))
# boxes = [1,2,3]
# warehouse = [1,2,3,4]
# print(S.maxBoxesInWarehouse(boxes, warehouse))
# boxes = [4,5,6]
# warehouse = [3,3,3,3,3]
# print(S.maxBoxesInWarehouse(boxes, warehouse))

boxes = [5,21,11,2,5,8,30,8,35,19,28,16,3,5,12,7,30,24,18]
warehouse =  [31,18,9,20,13,14,16,29,34,13,18,21]
print(S.maxBoxesInWarehouse(boxes, warehouse))
# 输出：
# 13
# 预期结果：
# 12