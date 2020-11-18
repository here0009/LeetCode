"""
In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

Then, a value from arr was removed that was not the first or last value in the array.

Return the removed value.

 

Example 1:

Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].
Example 2:

Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].
 

Constraints:

3 <= arr.length <= 1000
0 <= arr[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number-in-arithmetic-progression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def missingNumber(self, arr) -> int:
        length = len(arr)
        diff = (arr[-1] - arr[0])// length
        if diff == 0:
            return arr[0]
        for i in range(1, length):
            if arr[i] - arr[i-1] != diff:
                return arr[i-1] + diff
        return None

S = Solution()
arr = [5,7,11,13]
print(S.missingNumber(arr))
arr = [15,13,12]
print(S.missingNumber(arr))