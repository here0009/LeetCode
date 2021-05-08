"""
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

 

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:

1 <= intervals.length <= 105
1 <= queries.length <= 105
queries[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107
"""


# from typing import List
# class Solution:
#     def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:


#         length = len(intervals)
#         left = [(intervals[i][0], i, 0) for i in range(length)]
#         right = [(intervals[i][1], i, 1) for i in range(length)]
#         idx_lst = left + right
#         idx_lst.sort()

#         queries.sort()
#         idx = 0
#         stack = []
#         for q in queries:
#             while idx_lst[0][0] < q:
#                 idx += 1


from typing import List
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        queries_idx = [(v, i) for i, v in enumerate(queries)]
        queries_idx.sort()
        length = len(intervals)
        intervals_idx = [(inter[0], inter[1]) for inter in intervals]
        intervals_idx.sort()
        res = [-1] * len(queries)
        i_idx = 0
        pq = []
        for q, qi in queries_idx:
            while i_idx < length and intervals_idx[i_idx][0] <= q:
                start, end = intervals_idx[i_idx]
                heapq.heappush(pq, (end - start + 1, start, end))
                i_idx += 1
            while pq and pq[0][2] < q:
                heapq.heappop(pq)
            if pq:
                res[qi] = pq[0][0]
        return res


S = Solution()
intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
print(S.minInterval(intervals, queries))
intervals = [[2,3],[2,5],[1,8],[20,25]]
queries = [2,19,5,22]
print(S.minInterval(intervals, queries))
