"""
In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].
"""

class Solution:
    def numRabbits(self, answers) -> int:
        """
        wrong for test case [0,0,1,1,1]
        expected ans is 6
        """
        ans_set = set(answers) - {0}
        zeros = 0
        for n in answers:
            if n == 0:
                zeros += 1
        return sum(ans_set) + len(ans_set) + zeros

from collections import Counter
class Solution:
    def numRabbits(self, answers) -> int:
        """

        """
        a_counter = Counter(answers)
        res = 0
        for k,v in a_counter.items():
            if k == 0:
                res += v
            else:
                if v <= k+1:
                    res += k+1
                else:
                    res += v//(k+1)*(k+1)
                    if v%(k+1) != 0:
                        res += k+1
        return res

from collections import Counter
class Solution:
    def numRabbits(self, answers) -> int:
        a_counter = Counter(answers)
        res = 0
        for k,v in a_counter.items():
            res += v//(k+1)*(k+1)
            if v%(k+1) != 0:
                res += k+1
        return res

s = Solution()
answers = [1, 1, 2]
print(s.numRabbits(answers))

answers = [10, 10, 10]
print(s.numRabbits(answers))

answers = []
print(s.numRabbits(answers))

answers = [1,0,1,0,0]
print(s.numRabbits(answers))

answers = [0,0,1,1,1]
print(s.numRabbits(answers))