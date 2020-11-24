"""
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rank-transform-of-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        length = len(arr)
        res = [0]*length
        rank, pre = 0, -float('inf')
        arr2 = sorted([(v,i) for i,v in enumerate(arr)])
        for v,i in arr2:
            if v > pre:
                rank += 1
                pre = v
            res[i] = rank
        return res

# 作者：zbtzbt
# 链接：https://leetcode-cn.com/problems/rank-transform-of-an-array/solution/hashmap-dai-ma-you-ya-by-zbtzbt/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap={}
        L=sorted(list(set(arr)))
        for i,element in enumerate(L):
            hashmap[element]=i+1
        return [hashmap[i] for i in arr]



S = Solution()
arr = [40,10,20,30]
print(S.arrayRankTransform(arr))

arr = [100,100,100]
print(S.arrayRankTransform(arr))

arr = [37,12,28,9,100,56,80,5,12]
print(S.arrayRankTransform(arr))
