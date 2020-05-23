"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""
class Solution_1:
    def dailyTemperatures(self, T):
        """
        Time Limit Error
        """
        index = 0
        bigger_index = 0
        res = []
        len_T = len(T)
        while index < len_T:
            bigger_index = index
            while bigger_index < len_T and T[bigger_index] <= T[index]:
                bigger_index += 1
            if bigger_index == len_T:
                res.append(0)
            else:
                res.append(bigger_index-index)
            index += 1
        return res

class Solution:
    def dailyTemperatures(self, T):
        index = 0
        len_T = len(T)
        res = [0]*len_T
        stack = []
        while index < len_T:
            while stack and T[stack[-1]] < T[index]:
                i = stack.pop()
                res[i] = index - i
            stack.append((index))
            index += 1
        return res
                


s = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures(T))

T = [73]
print(s.dailyTemperatures(T))