"""
We have a sorted set of digits D, a non-empty subset of {'1','2','3','4','5','6','7','8','9'}.  (Note that '0' is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if D = {'1','3','5'}, we may write numbers such as '13', '551', '1351315'.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.

 

Example 1:

Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.
 

Note:

D is a subset of digits '1'-'9' in sorted order.
1 <= N <= 10^9
"""
class Solution:
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int 
        :rtype: int
        """
        res = 0
        len_D = len(D)
        if len_D == 1:
            return 1
        while N > 0:
            # print(N)
            N_digits = len(str(N))
            num = int(str(N)[0])
            # if N_digits == 1:
            #     pre_num = 0
            #     for D_num in D:
            #         if int(D_num) <= num:
            #             pre_num += 1
            #         else:
            #             break
            # else:
            pre_num = 1
            for D_num in D:
                if int(D_num) < num:
                    pre_num += 1
                else:
                    break
            # print("pre_num", pre_num)
            res += pre_num * self.smallThanN(len_D ,N_digits)
            # print(pre_num)
            # print(self.smallThanN(len_D ,N_digits))
            # print(res)
            # print(res)
            if N_digits > 1:
                N = int(str(N)[1:])
            else:
                break
        return res


    def smallThanN(self, len_list, N_digits):
        """
        return the numbers of len_list smaller than the number of 1E(N_digits)
        """
        if N_digits == 1:
            return 1
        n = len_list * (1-len_list ** (N_digits-1))/(1-len_list)
        return int(n)

s = Solution()

# len_list = 3
# for i in range(1,6):
#     print(i, s.smallThanN(len_list, i))

D = ["1","3","5","7"]
# N_list = [1,3,5,7]
# for N in N_list:
#     print(N, s.atMostNGivenDigitSet(D, N))
N_list = [10,20,30,40,50]
for N in N_list:
    print(N, s.atMostNGivenDigitSet(D, N))
# print(N, s.atMostNGivenDigitSet(D, N))
# N = 100
# print(s.atMostNGivenDigitSet(D, N))
# N = 250
# print(N, s.atMostNGivenDigitSet(D, N))
# N = 251
# print(N, s.atMostNGivenDigitSet(D, N))
# N = 253
# print(N, s.atMostNGivenDigitSet(D, N))

# N = 300
# print(N, s.atMostNGivenDigitSet(D, N))

# D = ["1","4","9"]
# N = 1000000000
# print(s.atMostNGivenDigitSet(D, N))
# D = ["9"]
# N = 55
# print(s.atMostNGivenDigitSet(D, N))
# D = ["3","5"]
# N = 4
# print(s.atMostNGivenDigitSet(D, N))

# D = ["3","4","8"]
# N = 4
# print(s.atMostNGivenDigitSet(D, N))

D = ["5","6"]
N = 19
print(s.atMostNGivenDigitSet(D, N))
