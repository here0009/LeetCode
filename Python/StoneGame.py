class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        """
        Alex will always win because the sum of the odd or the sum of the even is definitly unequal, Alex can choose a larger one to win
        """
        return True