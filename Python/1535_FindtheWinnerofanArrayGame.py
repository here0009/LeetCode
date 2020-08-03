"""
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.

 

Example 1:

Input: arr = [2,1,3,5,4,6,7], k = 2
Output: 5
Explanation: Let's see the rounds of the game:
Round |       arr       | winner | win_count
  1   | [2,1,3,5,4,6,7] | 2      | 1
  2   | [2,3,5,4,6,7,1] | 3      | 1
  3   | [3,5,4,6,7,1,2] | 5      | 1
  4   | [5,4,6,7,1,2,3] | 5      | 2
So we can see that 4 rounds will be played and 5 is the winner because it wins 2 consecutive games.
Example 2:

Input: arr = [3,2,1], k = 10
Output: 3
Explanation: 3 will win the first 10 rounds consecutively.
Example 3:

Input: arr = [1,9,8,2,3,7,6,4,5], k = 7
Output: 9
Example 4:

Input: arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
Output: 99
 

Constraints:

2 <= arr.length <= 10^5
1 <= arr[i] <= 10^6
arr contains distinct integers.
1 <= k <= 10^9
"""

from collections import deque
class Solution:
    def getWinner(self, arr, k: int) -> int:
        length = len(arr)
        if k >= length - 1:
            return max(arr)
        if k == 1:
            return max(arr[:2])
        dq = deque(arr)
        count = 0
        curr = dq.popleft()
        while dq:
            while curr > dq[0]:
                dq.append(dq.popleft())
                count += 1
                if count == k:
                    return curr
            dq.append(curr)
            curr = dq.popleft()
            count = 1 #bigger than the previous one


class Solution:
    def getWinner(self, arr, k: int) -> int:
        curr = arr[0]
        count = 0
        for i in range(1, len(arr)):
            if arr[i] > curr:
                count = 0
                curr = arr[i]
            count += 1
            if count == k:
                return curr
        return curr

S = Solution()
arr = [2,1,3,5,4,6,7]
k = 2
print(S.getWinner(arr, k))
arr = [3,2,1]
k = 10
print(S.getWinner(arr, k))
arr = [1,9,8,2,3,7,6,4,5]
k = 7
print(S.getWinner(arr, k))
arr = [1,11,22,33,44,55,66,77,88,99]
k = 1000000000
print(S.getWinner(arr, k))
arr = [2,1,3,5,4,6,7]
k = 2
print(S.getWinner(arr, k))
# Output:
# 2
# Expected:
# 5
arr = [1,25,35,42,68,70]
k = 1
print(S.getWinner(arr, k))