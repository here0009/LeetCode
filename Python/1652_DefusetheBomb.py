"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

 

Example 1:

Input: code = [5,7,1,4], k = 3
Output: [12,10,16,13]
Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
Example 2:

Input: code = [1,2,3,4], k = 0
Output: [0,0,0,0]
Explanation: When k is zero, the numbers are replaced by 0. 
Example 3:

Input: code = [2,4,9,3], k = -2
Output: [12,5,6,13]
Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
 

Constraints:

n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
"""

from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        if k == 0:
            return [0]*length
        code = code + code
        # print(code)
        res = []
        if k > 0:
            tmp = sum(code[:k])
            for i in range(length):
                tmp -= code[i]
                tmp += code[i+k]
                res.append(tmp)
        else:
            tmp = sum(code[length+k-1:length-1])
            # print(tmp, code[length+k-1:length-1])
            for i in range(length-1, 2*length-1):
                tmp += code[i]
                tmp -= code[i+k]
                res.append(tmp)
                # print(i, i+k)
        return res
# https://leetcode.com/problems/defuse-the-bomb/discuss/935494/Python-3%3A-Time-O(n)-Space-O(n)-Sum-of-Window
from typing import List
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        res = [0]*length
        if k == 0:
            return res
        elif k > 0:
            tmp = sum(code[:k])
        else:
            tmp = sum(code[k:])
        for i,v in enumerate(code):
            if k > 0:
                tmp += code[(i+k)%length] - v
                res[i] = tmp
            else:
                res[i] = tmp
                tmp += v - code[i+k]
        return res



S = Solution()
code = [5,7,1,4]
k = 3
print(S.decrypt(code, k))
code = [1,2,3,4]
k = 0
print(S.decrypt(code, k))
code = [2,4,9,3]
k = -2
print(S.decrypt(code, k))

code = [10,5,7,7,3,2,10,3,6,9,1,6]
k = -4
print(S.decrypt(code, k))

# 输出：
# [22,29,32,29,33,30,23,32,29,25,29,23]
# 预期：
# [22,26,22,28,29,22,19,22,18,21,28,19]