"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flip-game-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from functools import lru_cache
class Solution:
    def canWin(self, s: str) -> bool:
        
        @lru_cache(None)
        def dp(string):
            # print(string)
            for i in range(1, length):
                if string[i-1:i+1] == '++':
                    if not dp(string[:i-1] + '--' + string[i+1:]):
                        return True
            return False

        length = len(s)
        return dp(s)

S = Solution()
s = "++++"
print(S.canWin(s))