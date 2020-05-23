"""
Alice has a hand of cards, given as an array of integers.

Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.

Return true if and only if she can.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:

Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.
 

Note:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length
"""
from collections import Counter
from collections import deque
class Solution:
    def isNStraightHand(self, hand, W: int) -> bool:
        hand_counter = Counter(hand)
        n = len(hand)
        if n % W != 0:
            return False
        hand_vals = deque(sorted(hand_counter.keys()))
        while hand_vals:
            while hand_vals and  (hand_counter[hand_vals[0]] == 0): 
                hand_vals.popleft()
            if not hand_vals: #hand_vals is empty
                return True
            start, v = hand_vals[0], hand_counter[hand_vals[0]]
            for i in range(W):
                if start+i not in hand_counter or hand_counter[start+i] < v:
                    return False
                else:
                    hand_counter[start+i] -= v
        return True

from collections import Counter
class Solution:
    def isNStraightHand(self, hand, W: int) -> bool:
        hand_counter = Counter(hand)
        for i in sorted(hand_counter.keys()):
            if hand_counter[i] > 0:
                for j in range(W)[::-1]:
                    hand_counter[i+j] -= hand_counter[i]
                    if hand_counter[i+j] < 0:
                        return False
        return True


        
S = Solution()
hand = [1,2,3,6,2,3,4,7,8]
W = 3
print(S.isNStraightHand(hand,W))

hand = [1,2,3,4,5]
W = 4
print(S.isNStraightHand(hand,W))
