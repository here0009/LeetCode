"""
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.

 

Example 1:

Input: [9,4,2,10,7,8,8,1,9]
[9,2,7,8,9]
[4,10,8,1]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
 

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
"""
class Solution:
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2:
            return 1
        sign_list = []
        res = 1
        non_zero_num_flag = False
        for i in range(len(A)-1):
            num = A[i+1]-A[i]
            if not non_zero_num_flag and num != 0:
                res += 1
                non_zero_num_flag = True
            sign_list.append(num)

        # print(sign_list)
        
        start_flag, end_flag = False, False
        len_sign_list = len(sign_list)
        for i in range(1,len_sign_list):
            if not start_flag and  sign_list[i-1]*sign_list[i] < 0:
                start_flag = True
                start_index = i-1
            if start_flag and sign_list[i-1]*sign_list[i]>= 0 :
                end_flag = True
                end_index = i-1
            if end_flag:
                # print(sign_list[start_index:end_index+1])
                res = max(end_index - start_index + 2, res)
                start_flag, end_flag = False, False
            if start_flag and i == len_sign_list-1:
                # print(sign_list[start_index:i+1])
                res = max(i-start_index+2, res)


        return res

s = Solution()
A = [9,4,2,10,7,8,8,1,9]
print(s.maxTurbulenceSize(A))

A = [4,8,12,16]
print(s.maxTurbulenceSize(A))

A = [100]
print(s.maxTurbulenceSize(A))

A = [0,0,0,0,0,0]
print(s.maxTurbulenceSize(A))

A = [0,8,45,88,48,68,28,55,17,24]
print(s.maxTurbulenceSize(A))