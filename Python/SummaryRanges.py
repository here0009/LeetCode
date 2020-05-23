"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""
class Solution_1:
    def summaryRanges(self, nums):
        def addRange(start, end):
            if start == end:
                res.append(str(start))
            else:
                res.append('{}->{}'.format(start,end))

        res = []
        start,end = None,None
        length = len(nums)
        for i,n in enumerate(nums):
            if start is None:
                start,end = n,n
            else:
                if n == end + 1:
                    end += 1
                else:
                    addRange(start, end)
                    start,end = n,n

        if start is not None:
            addRange(start,end)

        return res

class Solution:
    def summaryRanges(self, nums):
        res = []
        for n in nums:
            if res and res[-1][1] == n-1:
                res[-1][1] = n
            else:
                res.append([n,n])
            # print(n,res)
        return ['{}->{}'.format(i,j) if i != j else str(i) for i,j in res]

S = Solution()
nums = [0,1,2,4,5,7]
print(S.summaryRanges(nums))

nums = [0,2,3,4,6,8,9]
print(S.summaryRanges(nums))