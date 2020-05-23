"""
In a deck of cards, every card has a unique integer.  You can order the deck in any order you want.

Initially, all the cards start face down (unrevealed) in one deck.

Now, you do the following steps repeatedly, until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck, put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1.  Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

The first entry in the answer is considered to be the top of the deck.

 

Example 1:

Input: [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
We get the deck in the order [17,13,11,2,3,5,7] (this order doesn't matter), and reorder it.
After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
We reveal 13, and move 17 to the bottom.  The deck is now [17].
We reveal 17.
Since all the cards revealed are in increasing order, the answer is correct.
 
[2,3,5,7,11,13,17]
Note:

1 <= A.length <= 1000
1 <= A[i] <= 10^6
A[i] != A[j] for all i != j
"""
class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck = sorted(deck)
        n = len(deck)
        res = []
        res_index_list = []
        for i in range(n):
            res.append(0)
            res_index_list.append(i)

        res_index = 0
        while len(deck) > 0 and len(res_index_list) > 0:
            # print(res_index_list)
            # print(res_index)
            res[res_index_list[res_index]] = deck.pop(0)
            res_index_list.pop(res_index)
            res_index += 1
            if len(res_index_list) != 0:
                res_index = res_index % len(res_index_list)
        return res

s = Solution()
deck = [17,13,11,2,3,5,7]
print(s.deckRevealedIncreasing(deck))
deck = [1]
print(s.deckRevealedIncreasing(deck))
deck = [1,2,3,4,5,6]
print(s.deckRevealedIncreasing(deck))
