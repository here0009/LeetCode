"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""
from collections import Counter
class Solution_1:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter_words = Counter(words)
        keys = sorted(counter_words.keys(), key = lambda x:(-counter_words[x],x))
        # print(keys)
        return keys[:k]

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counter_words = Counter(words)
        heap = [(-counts, word) for word, counts in counter_words.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2
print(s.topKFrequent(words, k))

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(s.topKFrequent(words, k))