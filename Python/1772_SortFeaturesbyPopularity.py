"""
You are given a string array features where features[i] is a single word that represents the name of a feature of the latest product you are working on. You have made a survey where users have reported which features they like. You are given a string array responses, where each responses[i] is a string containing space-separated words.

The popularity of a feature is the number of responses[i] that contain the feature. You want to sort the features in non-increasing order by their popularity. If two features have the same popularity, order them by their original index in features. Notice that one response could contain the same feature multiple times; this feature is only counted once in its popularity.

Return the features in sorted order.

 

Example 1:

Input: features = ["cooler","lock","touch"], responses = ["i like cooler cooler","lock touch cool","locker like touch"]
Output: ["touch","cooler","lock"]
Explanation: appearances("cooler") = 1, appearances("lock") = 1, appearances("touch") = 2. Since "cooler" and "lock" both had 1 appearance, "cooler" comes first because "cooler" came first in the features array.
Example 2:

Input: features = ["a","aa","b","c"], responses = ["a","a aa","a a a a a","b a"]
Output: ["a","aa","b","c"]
 

Constraints:

1 <= features.length <= 104
1 <= features[i].length <= 10
features contains no duplicates.
features[i] consists of lowercase letters.
1 <= responses.length <= 102
1 <= responses[i].length <= 103
responses[i] consists of lowercase letters and spaces.
responses[i] contains no two consecutive spaces.
responses[i] has no leading or trailing spaces.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-features-by-popularity
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
from collections import Counter
class Solution:
    def sortFeatures(self, features: List[str], responses: List[str]) -> List[str]:

        counts = Counter()
        for rsp in responses:
            lst = list(set(rsp.split(' ')))
            counts.update(Counter(lst))
        idx_dict = dict(zip(features, list(range(len(features)))))
        # print(counts)
        # print(idx_dict)
        features.sort(key=lambda x: (-counts[x], idx_dict[x]))
        return features


S = Solution()
features = ["cooler","lock","touch"]
responses = ["i like cooler cooler","lock touch cool","locker like touch"]
print(S.sortFeatures(features, responses))
features = ["a","aa","b","c"]
responses = ["a","a aa","a a a a a","b a"]
print(S.sortFeatures(features, responses))