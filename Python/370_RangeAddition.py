"""
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-addition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getModifiedArray(self, length: int, updates):
        """
        Thoughts: merge the updates first, the update the array
        """
        res = [0]*length
        for i, j, num in updates:
            if i >= length:
                continue
            res[i] += num
            if j + 1 < length:
                res[j+1] -= num
        for i in range(1, length):
            res[i] += res[i-1]
        return res

S = Solution()
length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
print(S.getModifiedArray(length, updates))
length = 0
updates = []
print(S.getModifiedArray(length, updates))