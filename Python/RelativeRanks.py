"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.
Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
"""
class Solution:
    def findRelativeRanks(self, scores):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        sorted_scores_dict = {}
        for order,score in enumerate(sorted(scores, reverse = True)):
            if order <= 2:
                sorted_scores_dict[score] = medals[order]
            else:
                sorted_scores_dict[score] = str(order + 1)
        res = [sorted_scores_dict[score] for score in scores]
        return res

s = Solution()
scores = [5, 4, 3, 2, 1]
print(s.findRelativeRanks(scores))