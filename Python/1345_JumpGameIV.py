"""
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
 

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
"""


from typing import List
from collections import defaultdict
debug = True
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # if debug:
        #     print(arr)
        #     for i,v in enumerate(arr):
        #         print(i, v)
        if len(arr) == 1:
            return 0
        arr2 = []
        pre = arr[0]
        counts = 1
        for num in arr[1:]:
            if num == pre:
                counts += 1
            else:
                arr2.extend([pre]*min(2, counts))
                pre = num
                counts = 1
        arr2.extend([pre]*min(2, counts))
        print(arr2)
        arr = arr2
        length = len(arr)

        edges = defaultdict(set)
        val_index = defaultdict(set)
        for i, v in enumerate(arr):
            val_index[v].add(i)

        for i in range(1, length-1):
            edges[i] |= set([i+1, i-1])
            edges[i] |= val_index[arr[i]]

        edges[0].add(1)
        edges[0] |= val_index[arr[0]]
        edges[length-1].add(length-2)
        edges[length-1] |= val_index[arr[length-1]]

        visited = [1] + [0]*(length-1)
        # print(edges)
        bfs = set([0])
        steps = 0
        while bfs:
            # print(bfs)
            if length-1 in bfs:
                return steps
            steps += 1
            bfs2 = set()
            for i in bfs:
                for j in edges[i]:
                    if visited[j] == 0:
                        bfs2.add(j)
                        visited[j] = 1
            bfs = bfs2
        return -1




S = Solution()

# arr = [100,-23,-23,404,100,23,23,23,3,404]
# print(S.minJumps(arr))
# arr = [7]
# print(S.minJumps(arr))
# arr = [7,6,9,6,9,6,9,7]
# print(S.minJumps(arr))
# arr = [6,1,9]
# print(S.minJumps(arr))
# arr = [11,22,7,7,7,7,7,7,7,22,13]
# print(S.minJumps(arr))
arr = [11,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]
print(S.minJumps(arr))