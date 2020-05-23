"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?

 

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
 

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""
from collections import Counter
class Solution:
    def numSubarraysWithSum(self, A, S: int) -> int:
        pre_Sum = [0]
        tmp = 0
        for num in A:
            tmp += num
            pre_Sum.append(tmp)
        pre_Sum_counter = Counter(pre_Sum)
        res = 0
        # print(pre_Sum_counter)
        if S == 0:
            for k,v in pre_Sum_counter.items():
                if v > 1:
                    res += (v-1)*v//2 #Eliminate the 1st one, v-1 is the num of continous 0s, total subarry of v-1 0s is (v-1)*v//2
        else:
            for k,v in pre_Sum_counter.items():
                target = k + S
                if target in pre_Sum_counter:
                    res += v * pre_Sum_counter[target]
        return res

s = Solution()
A = [1,0,1,0,1]
S = 2
print(s.numSubarraysWithSum(A,S))

A = [0,0,0,0,0]
S = 0
print(s.numSubarraysWithSum(A,S))

A = [0,0,0,0,0,0,1,0,0,0]
S = 0
print(s.numSubarraysWithSum(A,S))
"""
Output:
31
Expected:
27
"""