"""
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

 

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true
 

Note:

1 <= N <= 10^9
"""
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """
        wrong
        """
        print(N)
        if N == 1:
            return False
        while N > 1:
            print(N)
            if N % 2 == 0:
                N = N //2
            else:
                preN = N
                str_N = str(N)
                for i in range(len(str_N)-1):
                    v = int(str_N[i])
                    if v % 2 == 0:
                        N = int(str_N[:i]+str_N[i+1:]+str(v))
                if N == preN:
                    return False
        return True


from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """
        use a set of dict to record the combinations of power 2 from 2**1 ~ 2**30
        """
        def dict_to_str(counter):
            return ''.join([str(counter[str(i)]) if str(i) in counter else str(0) for i in range(10)])
        # print(N)
        num = 1
        power2_set = set()
        for i in range(30):
            power2_set.add(dict_to_str(Counter(str(num))))
            num = num*2
        # print(power2_set)
        # print(dict_to_str(Counter(str(N))))
        return dict_to_str(Counter(str(N))) in power2_set

s = Solution()
N_list = [1,10,16,24,46]
for N in N_list:
    print(s.reorderedPowerOf2(N))

# N_list = [812,4021]
# for N in N_list:
#     print(s.reorderedPowerOf2(N))