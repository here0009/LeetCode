"""
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
Example 4:

Input: data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
Output: 8
 

Constraints:

1 <= data.length <= 105
data[i] is 0 or 1.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-swaps-to-group-all-1s-together
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minSwaps(self, data) -> int:
        k = sum(data)
        zeros = k - sum(data[:k])
        res = zeros
        # print(k, zeros)
        length = len(data)
        for i in range(k, length):
            if data[i - k] == 0:
                zeros -= 1
            if data[i] == 0:
                zeros += 1
            res = min(res, zeros)
        return res

S = Solution()
data = [1,0,1,0,1]
print(S.minSwaps(data))
data = [0,0,0,1,0]
print(S.minSwaps(data))
data = [1,0,1,0,1,0,0,1,1,0,1]
print(S.minSwaps(data))
data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
print(S.minSwaps(data))