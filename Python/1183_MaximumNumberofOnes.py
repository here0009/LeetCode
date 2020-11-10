"""
Consider a matrix M with dimensions width * height, such that every cell has value 0 or 1, and any square sub-matrix of M of size sideLength * sideLength has at most maxOnes ones.

Return the maximum possible number of ones that the matrix M can have.

 

Example 1:

Input: width = 3, height = 3, sideLength = 2, maxOnes = 1
Output: 4
Explanation:
In a 3*3 matrix, no 2*2 sub-matrix can have more than 1 one.
The best solution that has 4 ones is:
[1,0,1]
[0,0,0]
[1,0,1]
Example 2:

Input: width = 3, height = 3, sideLength = 2, maxOnes = 2
Output: 6
Explanation:
[1,0,1]
[1,0,1]
[1,0,1]
 

Constraints:

1 <= width, height <= 100
1 <= sideLength <= width, height
0 <= maxOnes <= sideLength * sideLength

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-ones
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import heapq
from collections import defaultdict
from collections import Counter
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        """
        calculate how mansy squares each node belongs to
        """
        squares = Counter()
        nodes = defaultdict(set)
        pq = []
        matrix = [[0]*width for _ in range(height)]
        for i in range(height-sideLength+1):
            for j in range(width-sideLength+1):
                # i, j is the left most index of a square
                for ik in range(sideLength):
                    for jk in range(sideLength):
                        matrix[i+ik][j+jk] += 1
                        nodes[(i+ik, j+jk)].add((i,j))
        # print('nodes', nodes)
        for i in range(height):
            for j in range(width):
                heapq.heappush(pq, (matrix[i][j], i, j))

        # print('pq',pq)
        res = 0
        while pq:
            v, i, j = heapq.heappop(pq)
            # print(v,i,j)
            if all(squares[(si,sj)] < maxOnes for si,sj in nodes[(i,j)]):
                res += 1
                for si,sj in nodes[(i,j)]:
                    squares[(si,sj)] += 1
            # print('squares', squares)
        return res

import heapq
from collections import defaultdict
from collections import Counter
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        """
        calculate how mansy squares each node belongs to
        """
        squares = (height - sideLength + 1) * (width - sideLength + 1)
        matrix = [[0]*width for _ in range(height)]
        target = maxOnes*squares
        counts = Counter()
        for i in range(height-sideLength+1):
            for j in range(width-sideLength+1):
                # i, j is the left most index of a square
                for ik in range(sideLength):
                    for jk in range(sideLength):
                        matrix[i+ik][j+jk] += 1
        for i in range(height):
            for j in range(width):
                counts[matrix[i][j]] += 1

        tmp = 0
        res = 0
        print(counts, target)
        print([(k,counts[k]) for k in sorted(counts.keys())])
        for key in sorted(counts.keys()):
            if key*counts[key] <= target:
                target -= key*counts[key]
                res += counts[key]
            else:
                d = target//key
                res += d
                break
        return res




'''
只看第一个方块， 里面某位置(i, j)填写1，那跟这个位置两个维度上
坐标差是(sideLength, sideLength)的位置也同样填写1，枚举第一个
方块中所有位置，在该位置放1，记录该位置放1后，整个矩阵放1的个数，
选出maxOnes个个数最多的位置，将每一个位置的个数求和

作者：hao-shou-bu-juan
链接：https://leetcode-cn.com/problems/maximum-number-of-ones/solution/python-can-kan-bie-ren-si-lu-mei-ju-di-yi-ge-fang-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。   
'''

from queue import PriorityQueue
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        que = PriorityQueue()

        w = width // sideLength
        h = height // sideLength
        for i in range(sideLength):
            for j in range(sideLength):
                ww = w + 1 if j < width % sideLength else w
                hh = h + 1 if i < height % sideLength else h
                que.put(ww * hh)

                if que.qsize() > maxOnes:
                    que.get()

        ans = 0
        while que.qsize():
            ans += que.get()
        return ans

      
from math import ceil
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        counts = []
        for i in range(sideLength):
            for j in range(sideLength):
                ones = ceil((height-i)/sideLength) * ceil((width-j)/sideLength)
                counts.append(ones)
        return sum(sorted(counts, reverse=True)[:maxOnes])

S = Solution()
width = 3
height = 3
sideLength = 2
maxOnes = 1
print(S.maximumNumberOfOnes(width, height, sideLength, maxOnes))
width = 3
height = 3
sideLength = 2
maxOnes = 2
print(S.maximumNumberOfOnes(width, height, sideLength, maxOnes))

width = 10
height = 10
sideLength = 4
maxOnes = 5
print(S.maximumNumberOfOnes(width, height, sideLength, maxOnes))

# 输出：
# 40
# 预期结果：
# 42