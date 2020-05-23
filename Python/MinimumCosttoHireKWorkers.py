"""
There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.  When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
 

Note:

1 <= K <= N <= 10000, where N = quality.length = wage.length
1 <= quality[i] <= 10000
1 <= wage[i] <= 10000
Answers within 10^-5 of the correct answer will be considered correct.
"""
import heapq
class Solution:
    """
    sort the works by the qatio of wage_divde_qualtiy in ascending order, if curent worker is satisfied with the ratio, the workers before him is satisfied too.
    So if the number of worker is larger than k, we just need to remove the worker got the max quality to reduece the total wage.
    """
    def mincostToHireWorkers(self, quality, wage, K: int) -> float:
        N = len(quality)
        ratio_list = sorted([(wage[i]/quality[i],i) for i in range(N)]) #wage per quality
        # print(ratio_list)
        workers = [] #update workers with larger ratio and might be smaller quality
        q = 0
        res = float('inf')
        for r,i in ratio_list:
            q += quality[i]
            heapq.heappush(workers, -quality[i]) #we need to pop the max, so push in -quality[i]
            if len(workers) > K:
                q += heapq.heappop(workers) #pop the largest qualtiy, which will cost most
            if len(workers) == K:
                res = min(res, r*q)
        return res




        return

s = Solution()
quality = [10,20,5]
wage = [70,50,30]
K = 2
print(s.mincostToHireWorkers(quality, wage, K))

quality = [3,1,10,10,1]
wage = [4,8,2,2,7]
K = 3
print(s.mincostToHireWorkers(quality, wage, K))