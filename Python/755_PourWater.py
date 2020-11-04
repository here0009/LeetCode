"""
We are given an elevation map, heights[i] representing the height of the terrain at that index. The width at each index is 1. After V units of water fall at index K, how much water is at each index?

Water first drops at index K and rests on top of the highest terrain or water at that index. Then, it flows according to the following rules:

If the droplet would eventually fall by moving left, then move left.
Otherwise, if the droplet would eventually fall by moving right, then move right.
Otherwise, rise at it's current position.
Here, "eventually fall" means that the droplet will eventually be at a lower level if it moves in that direction. Also, "level" means the height of the terrain plus any water in that column.
We can assume there's infinitely high terrain on the two sides out of bounds of the array. Also, there could not be partial water being spread out evenly on more than 1 grid block - each unit of water has to be in exactly one block.

Example 1:
Input: heights = [2,1,1,2,1,2,2], V = 4, K = 3
Output: [2,2,2,3,2,2,2]
Explanation:
#       #
#       #
##  # ###
#########
 0123456    <- index

The first drop of water lands at index K = 3:

#       #
#   w   #
##  # ###
#########
 0123456    

When moving left or right, the water can only move to the same level or a lower level.
(By level, we mean the total height of the terrain plus any water in that column.)
Since moving left will eventually make it fall, it moves left.
(A droplet "made to fall" means go to a lower height than it was at previously.)

#       #
#       #
## w# ###
#########
 0123456    

Since moving left will not make it fall, it stays in place.  The next droplet falls:

#       #
#   w   #
## w# ###
#########
 0123456  

Since the new droplet moving left will eventually make it fall, it moves left.
Notice that the droplet still preferred to move left,
even though it could move right (and moving right makes it fall quicker.)

#       #
#  w    #
## w# ###
#########
 0123456  

#       #
#       #
##ww# ###
#########
 0123456  

After those steps, the third droplet falls.
Since moving left would not eventually make it fall, it tries to move right.
Since moving right would eventually make it fall, it moves right.

#       #
#   w   #
##ww# ###
#########
 0123456  

#       #
#       #
##ww#w###
#########
 0123456  

Finally, the fourth droplet falls.
Since moving left would not eventually make it fall, it tries to move right.
Since moving right would not eventually make it fall, it stays in place:

#       #
#   w   #
##ww#w###
#########
 0123456  

The final answer is [2,2,2,3,2,2,2]:

    #    
 ####### 
 ####### 
 0123456 
Example 2:
Input: heights = [1,2,3,4], V = 2, K = 2
Output: [2,3,3,4]
Explanation:
The last droplet settles at index 1, since moving further left would not cause it to eventually fall to a lower height.
Example 3:
Input: heights = [3,1,3], V = 5, K = 1
Output: [4,4,4]
Note:

heights will have length in [1, 100] and contain integers in [0, 99].
V will be in range [0, 2000].
K will be in range [0, heights.length - 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pour-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



class Solution:
    def pourWater(self, heights, V: int, K: int):
        def flow(lst):
            """
            two pointer
            """
            start, end = 0, 1
            while end < len(lst):
                if lst[end] < lst[start]:
                    start = end
                    end += 1
                elif lst[end] == lst[start]:
                    end += 1
                else:
                    break
            if start > 0:
                lst[start] += 1
                return True
            return False

        left_h = heights[:K+1][::-1] + [float('inf')]
        right_h = heights[K:] + [float('inf')]

        while V > 0:
            if not flow(left_h):
                if not flow(right_h):
                    left_h[0] += 1
                    right_h[0] += 1
            V -= 1
        return left_h[1:-1][::-1] + right_h[:-1]



# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/pour-water/solution/dao-shui-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def pourWater(self, H, V, K):
        while V > 0:
            for d in (-1, 1):
                i = best = K
                while 0 <= i+d < len(H) and H[i+d] <= H[i]:
                    if H[i+d] < H[i]:
                        best = i+d
                    i += d
                if best != K:
                    H[best] += 1
                    break
            else:
                H[K] += 1
            V -= 1
        return H

# 作者：intoloop
# 链接：https://leetcode-cn.com/problems/pour-water/solution/python-xian-zuo-hou-you-by-intoloop/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        n=len(heights)
        while V:
            curPos=K
            for i in range(K-1,-1,-1):
                if heights[i]<heights[curPos]:
                    curPos=i 
                elif heights[i]>heights[curPos]:
                    break
            if curPos==K:
                for i in range(K+1,n):
                    if heights[i]<heights[curPos]:
                        curPos=i 
                    elif heights[i]>heights[curPos]:
                        break
            heights[curPos]+=1
            V-=1
        return heights



heights = [2,1,1,2,1,2,2]
V = 4
K = 3
S = Solution()
print(S.pourWater(heights, V, K))
heights = [1,2,3,4]
V = 2
K = 2
print(S.pourWater(heights, V, K))
heights = [3,1,3]
V = 5
K = 1
print(S.pourWater(heights, V, K))