"""
We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return True if and only if Alice wins the game, assuming both players play optimally.

Example:
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.

Notes:

1 <= N <= 1000. 
0 <= nums[i] <= 2^16.
"""


from typing import List
from collections import Counter
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        """
        use counts to represent Counter(nums)
        even counts can be xor to 0,
        if the number of odd counts is even, such as [1, 2], then Alice wins
        else Bob wins.
        so either of them will try to make the number of odd counts to be even
        """
        counts = Counter(nums)
        odd = sum(v for v in counts.values() if v % 2 == 1)
        return odd % 2 == 0

from typing import List
from collections import Counter
from functools import reduce
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        """
        use counts to represent Counter(nums)
        even counts can be xor to 0,
        if the number of odd counts is even, such as [1, 2], then Alice wins
        else Bob wins.
        so either of them will try to make the number of odd counts to be even
        """
        total = reduce(lambda x, y: x ^ y, nums)
        # print(total)
        counts = Counter(nums)
        odd = sum(v for v in counts.values() if v % 2 == 1)
        return total == 0 or odd % 2 == 0


from typing import List
from collections import Counter
from functools import reduce
class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        """
        use counts to represent Counter(nums)
        even counts can be xor to 0,
        if the number with odd counts is even, such as [1, 2], then Alice wins
        else Bob wins.
        so either of them will try to make the number of odd counts to be even
        further more, because the number with even counts is always even
        so the total number of odd counts % 2 == len(nums) % 2

        https://leetcode.com/problems/chalkboard-xor-game/discuss/121696/C%2B%2BJavaPython-3-lines-Easy-Solution-with-Complaint-and-Explanation
        a more clear and simple explination
        if total_xor is zero, Alice wins
        if total_xor is not zero and len of nums is even, alice wins two
        because total_xor != 0 and len(nums) is even
        means there are a least 2 different num in nums(not paired with the same val)
        so alice can always remove a number did not equal to current total.
        """
        total = reduce(lambda x, y: x ^ y, nums)
        # print(total)
        return total == 0 or len(nums) == 0

S = Solution()
nums = [1, 1, 2]
print(S.xorGame(nums))
nums = [1,2,3]
print(S.xorGame(nums))