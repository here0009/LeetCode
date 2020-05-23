"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
"""
import bisect
class Solution:
    def hIndex(self, citations) -> int:
        len_c = len(citations)
        citations = sorted(citations)
        for i in range(len_c-1, -1, -1):
            hIndex = i+1
            num = len_c - bisect.bisect_left(citations, hIndex)
            # print(hIndex, num)
            if num >= hIndex:
                return hIndex
        return 0

class Solution:
    def hIndex(self, citations) -> int:
        len_c = len(citations)
        citations = sorted(citations)
        for i in range(len_c):
            if citations[i] >= len_c-i: #from citations[i:], the min citation > len_c-i, lenc_i can be hIndex
                return len_c-i
        return 0


s = Solution()
citations = [3,0,6,1,5]
print(s.hIndex(citations))

citations = [5,5,5,5,5]
print(s.hIndex(citations))

citations = [100]
print(s.hIndex(citations))

citations = [4,4,0,0]
print(s.hIndex(citations))

citations = [2,3,2]
print(s.hIndex(citations))