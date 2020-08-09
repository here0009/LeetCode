"""
Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
"""


class Solution:
    def splitIntoFibonacci(self, S: str):
        def getStart():
            res = []
            for i in range(1, length - 1):
                for j in range(i+1, length):
                    s1, s2 = S[:i], S[i:j]
                    if (s1[0] == '0' and len(s1) != 1) or (s2[0] == '0' and len(s2) != 1):
                        continue
                    res.append((int(s1), int(s2), j))
            return res

        def dfs(arr, i):
            if i == length:
                return arr
            total = arr[-2] + arr[-1]
            total_len = len(str(total))
            target = int(S[i: i + total_len])
            return target == total and 0 <= total <= max_val and dfs(arr + [target], i + total_len)

        length = len(S)
        start_list = getStart()
        max_val = 2**31 -1
        for p, q, i in start_list:
            seq = dfs([p, q], i)
            if seq:
                return seq
        return []


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def dfs(seq,ind):
            if ind==len(S):
                return seq
            summ=seq[-1]+seq[-2]
            l=len(str(summ))
            prob=int(S[ind:ind+l])
            return summ==prob and 0<=summ<=maxx and dfs(seq+[summ],ind+l)
        n,maxx=len(S),(2**31)-1
        for i in range(1,n-1):
            for j in range(i+1,n):
                s1,s2=S[:i],S[i:j]
                if (s1[0]=="0" and len(s1)>1) or (s2[0]=="0" and len(s2)>1):
                    continue
                ans=dfs([int(s1),int(s2)],j)
                if ans: return ans
        return []

        
s = Solution()
string = "123456579"
print(s.splitIntoFibonacci(string))
string = "11235813"
print(s.splitIntoFibonacci(string))
string = "112358130"
print(s.splitIntoFibonacci(string))
string = "0123"
print(s.splitIntoFibonacci(string))
string = "1101111"
print(s.splitIntoFibonacci(string))