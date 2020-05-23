"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 

Constraints:

1 <= arr.length <= 5 * 10^4
0 <= arr[i] < arr.length
0 <= start < arr.length
"""
class Solution:
    def canReach(self, arr, start) -> bool:
        def dfs(index):
            visited[index] = 1
            v = arr[index]
            # print(index, v)
            if v == 0:
                self.res = True
                return
            r = index + v
            if r >= 0 and r < len_arr and not visited[r]:
                dfs(r)
            l = index - v
            if l >= 0 and l < len_arr and not visited[l]:
                dfs(l)
        self.res = False
        len_arr = len(arr)
        visited = [0]*len_arr
        dfs(start)
        return self.res

S = Solution()
print("++++++++++++")
arr = [4,2,3,0,3,1,2]
start = 5
print(S.canReach(arr,start))
print("++++++++++++")
arr = [4,2,3,0,3,1,2]
start = 0
print(S.canReach(arr,start))
print("++++++++++++")
arr = [3,0,2,1,2]
start = 2
print(S.canReach(arr,start))
