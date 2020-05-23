"""
Given an array of integers arr and an integer d. In one step you can jump from index i to index:

i + x where: i + x < arr.length and 0 < x <= d.
i - x where: i - x >= 0 and 0 < x <= d.
In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).

You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.

Notice that you can not jump outside of the array at any time.

 

Example 1:


Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
Output: 4
Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
Example 2:

Input: arr = [3,3,3,3,3], d = 3
Output: 1
Explanation: You can start at any index. You always cannot jump to any index.
Example 3:

Input: arr = [7,6,5,4,3,2,1], d = 1
Output: 7
Explanation: Start at index 0. You can visit all the indicies. 
Example 4:

Input: arr = [7,1,7,1,7,1], d = 2
Output: 2
Example 5:

Input: arr = [66], d = 1
Output: 1
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 10^5
1 <= d <= arr.length
"""
from functools import lru_cache
class Solution:
    def maxJumps(self, arr, d: int) -> int:
        def inRange(index):
            return index >= 0 and index < length

        @lru_cache(None)
        def counts(index):           
            steps = 1
            for di in range(1,d):
                tmp = index+di
                if inRange(tmp) and arr[tmp] < arr[index]:
                    steps = max(steps, 1+counts(tmp))
                else:
                    break
            for di in range(1,d):
                tmp = index-di
                if inRange(tmp) and arr[tmp] < arr[index]:
                    steps = max(steps, 1+counts(tmp))
                else:
                    break
            # print('index', index, steps)
            return steps

        res = 1
        d = d+1
        length = len(arr)
        for start_index in range(length):
            # print('start_index' ,start_index,counts(start_index))
            res = max(res, counts(start_index))
        return res

S = Solution()
arr = [6,4,14,6,8,13,9,7,10,6,12] 
d = 2
print(S.maxJumps(arr, d))
arr = [3,3,3,3,3]
d = 3
print(S.maxJumps(arr, d))
arr = [7,6,5,4,3,2,1]
d = 1
print(S.maxJumps(arr, d))
arr = [7,1,7,1,7,1]
d = 2
print(S.maxJumps(arr, d))
arr = [66]
d = 1
print(S.maxJumps(arr, d))