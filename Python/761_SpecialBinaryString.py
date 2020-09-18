"""
Special binary strings are binary strings with the following two properties:

The number of 0's is equal to the number of 1's.
Every prefix of the binary string has at least as many 1's as 0's.
Given a special string S, a move consists of choosing two consecutive, non-empty, special substrings of S, and swapping them. (Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.)

At the end of any number of moves, what is the lexicographically largest resulting string possible?

Example 1:
Input: S = "11011000"
Output: "11100100"
Explanation:
The strings "10" [occuring at S[1]] and "1100" [at S[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.
Note:

S has length at most 50.
S is guaranteed to be a special binary string as defined above.
"""


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        """
        two type of special string: 101010 and 111000, 101010 can be divided to 10, 10, 10, so one type
        110100 is also a special string
        wrong answer
        """
        def mergeIntervals(tmp):
            tmps, tmpe = tmp[0][0], tmp[-1][1]
            tmp = sorted(tmp, key=lambda x:x[1]-x[0], reverse=True)
            tmp_string = ''.join([(j-i)//2*'1'+ (j-i)//2*'0' for i,j in tmp])
            return (tmps, tmpe, tmp_string)

        c_ones, c_zeros = [0,0], [0,0]
        pre = '-1'
        postions = []
        length = len(S)
        # total and consecutive ones, zeros
        for i, v in enumerate(S):
            if v == '0':
                if pre == '0':
                    c_zeros[-1] = i+1
                else:
                    c_zeros = [i, i+1]
                if i == length-1 or S[i+1] == '1':
                    minlen = min(c_ones[1]-c_ones[0], c_zeros[1]-c_zeros[0])
                    postions.append((c_ones[1]-minlen, c_zeros[0]+minlen))
            elif v == '1':
                if pre == '1':
                    c_ones[-1] = i+1
                else:
                    c_ones = [i, i+1]
            pre = v
        intervals = []
        tmp = []
        for s, e in postions:
            if s == pre:
                tmp.append((s, e))
            else:
                if len(tmp) > 0:
                    intervals.append(mergeIntervals(tmp))
                tmp = [(s, e)]
            pre = e
        if tmp:
            intervals.append(mergeIntervals(tmp))
        # print(postions)
        # print(intervals)
        index = 0
        res = ''
        for i,j,string in intervals:
            res += S[index:i]
            res += string
            index = j
        res += S[index:]
        return res


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        """
        two type of special string: 101010 and 111000, 101010 can be divided to 10, 10, 10, so one type
        110100 is also a special string
        """
        pos_dict = dict()
        ones = 0
        intervals = []
        for i, v in enumerate(S):
            if v == '1':
                ones += 1
            elif v == '0':
                ones -= 1
            if ones > 0:
                if ones in pos_dict:
                    intervals.append((pos_dict[ones], i+1))
                pos_dict[ones] = i
        print(intervals)


class Solution:
    def makeLargestSpecial(self, S: str) -> str:
        count, i = 0, 0
        res = []
        for j, v in enumerate(S):
            if v == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i+1:j]) + '0')
                i = j+1
        return ''.join(sorted(res, reverse=True))

s = Solution()
S = "11011000"
print(s.makeLargestSpecial(S))
S = "110110100100"
A = "111010010100"
# Output
# "110110100100"
# Expected
# "111010010100"
print(s.makeLargestSpecial(S))