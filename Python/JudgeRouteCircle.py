class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        position = [0,0]
        #positon[0] for U and D, positon[1] for L and R
        if len(moves) == 0:
            return True
        if len(moves)%2 == 1:
            return False
        for s in moves:
            if s == 'U':
                position[0] += 1
            elif s == 'D':
                position[0] -= 1
            elif s == 'L':
                position[1] -= 1
            elif s == 'R':
                position[1] += 1

        if position[0] == 0 and position[1] == 0:
            return True
        else:
            return False

s = Solution()
test = "UD"
print(s.judgeCircle(test))

"""
The most fastest solution
"""
# class Solution:
    # def judgeCircle(self, moves):
    #     """
    #     :type moves: str
    #     :rtype: bool
    #     """
    #     return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')