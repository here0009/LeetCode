"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""
class Solution_1:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        #trim S, remove the beginning 0s and ending 1s
        def trim(string):
            i = 0
            j = len(string)-1
            while i < len(string)-1:
                if string[i] == '0':
                    i+=1
                else:
                    break
            while j > 0:
                if string[j] == '1':
                    j-=1
                else:
                    break
            # string[j] == '1' and j >0:
            #     j-=1
            if j-i >= 2:
                return string[i:j+1]
            else:
                return ''

        flips = 0
        while True:
            trimmed_S = trim(S)
            print("trimmed_S")
            print(trimmed_S)
            start_ones = 0
            end_zeros = 0
            start = 0
            end = len(trimmed_S)-1
            if len(trimmed_S) == 0:
                return flips 
            while trimmed_S[start] == '1' and start < len(trimmed_S)-1:
                start_ones += 1
                start += 1
            while trimmed_S[end] == '0' and end > 0:
                end_zeros += 1
                end -= 1
            if end_zeros >= start_ones:
                flips += start_ones
                trimmed_S = start_ones*'0'+trimmed_S[start:]
            else:
                flips += end_zeros
                trimmed_S = trimmed_S[:end] + end_zeros*'1'
            S = trimmed_S


        return "Wrong"

class Solution_2:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        """
        Thoughts:
        Solution_1 totoaly overthink it, we just need to trim S, and calculate the 0s and 1s in the trimmed sequence, that's the number needs to be flips
        """
        def trim(string):
            i = 0
            j = len(string)-1
            while i < len(string)-1:
                if string[i] == '0':
                    i+=1
                else:
                    break
            while j > 0:
                if string[j] == '1':
                    j-=1
                else:
                    break
            # string[j] == '1' and j >0:
            #     j-=1
            if j-i >= 2:
                return string[i:j+1]
            else:
                return ''

        flips = 0
        ones = 0
        S = trim(S)
        print(S)
        for letter in S:
            if letter == '1':
                ones += 1
        zeros = len(S)-ones
        flips += min(zeros, ones)
        return flips

class Solution_3:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        """
        Thoughts:
        Solution_1 totoaly overthink it, we just need to trim S, and calculate the 0s and 1s in the trimmed sequence, that's the number needs to be flips
        Solution_2 is not right neither, because when you1 have an input like "10011111110010111011", the first 1 should be changed to zero, but Solution_2 change all zeros to ones.
        I came up with a new method by this test.
        first, trim the input as usual. then the squence should begins with ones and ends with zeros, calculate two values:
        * a: continouse ones
        * b: total zeros
        
        if a>=b, then all zeros change to ones, flips = b
        else if a<b, change a to zeros, trim it again.
        continue the process, until S all trimmed.
        """
        def trim(string):
            i = 0
            j = len(string)-1
            while i < len(string)-1:
                if string[i] == '0':
                    i+=1
                else:
                    break
            while j > 0:
                if string[j] == '1':
                    j-=1
                else:
                    break
            # string[j] == '1' and j >0:
            #     j-=1
            if j-i >= 2:
                return string[i:j+1]
            else:
                return ''

        def zeros_in_string(string):
            return len(string) - sum([int(i) for i in string])

        flips = 0
        
        S = trim(S)
        print(S)
        while len(S)>0:
            coninouse_ones = 0
            for letter in S:
                if letter == '1':
                    coninouse_ones += 1
                else:
                    break
            total_zeros = zeros_in_string(S)
            if total_zeros <= coninouse_ones:
                flips += total_zeros
                return flips
            else:
                flips += coninouse_ones
                S = S[coninouse_ones:] 
                S = trim(S)
                print(S)
        return flips

class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        """
        Thoughts:
        Solution_3还是不对，使用递归的方法解决此问题较为困难， 可以才用穷举的方法。
        选择一个分界点1， 将1左侧的1变成0， 将1右侧的0变成1， 这样找出flips数最小的分解点即可， 最开始从第一个数的左侧开始， 即将所有的0变成1
        最后一个数在所有数的最右侧， 将所有1变成0
        flips初始化为1的个数， 这样对于全0数字，flips初始值为0
        对于全1值， flips第一轮之后也为0
        如果flips初始化为0的个数， 对于全0值
        """
        len_S = len(S)
        ones = 0 #record the ones need to flip
        total_ones = sum([int(i) for i in S])
        zeros = len_S - total_ones #record the zeros need to flip
        # flips = total_ones
        flips = zeros
        if zeros == len_S or zeros == 0:
            return 0
        for letter in S:
            if letter == '0':
                zeros -= 1
            elif letter == '1':
                #new break point
                flips = min(flips, ones+zeros)
                ones += 1
            # print(flips)
        return flips




s = Solution()
# S = "00110"
# print(S)
# print(s.minFlipsMonoIncr(S))

# S = "010110"
# print(S)
# print(s.minFlipsMonoIncr(S))

S = "00011000"
print(S)
print(s.minFlipsMonoIncr(S))

# S = "00011000111"
# print(S)
# print(s.minFlipsMonoIncr(S))

# S = "11111111"
# print(S)
# print(s.minFlipsMonoIncr(S))


# S = "000000"
# print(S)
# print(s.minFlipsMonoIncr(S))

# S = "000000111111"
# print(S)
# print(s.minFlipsMonoIncr(S))

# S = "111000"
# print(S)
# print(s.minFlipsMonoIncr(S))

# S = "11011011010010110011"
# print(S)
# print(s.minFlipsMonoIncr(S))

# S = "10011111110010111011"
# print(S)
# print(s.minFlipsMonoIncr(S))