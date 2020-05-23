"""
We have a set of items: the i-th item has value values[i] and label labels[i].

Then, we choose a subset S of these items, such that:

|S| <= num_wanted
For every label L, the number of items in S with label L is <= use_limit.
Return the largest possible sum of the subset S.

 

Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], num_wanted = 3, use_limit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth item.
Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third item.
Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1
Output: 16
Explanation: The subset chosen is the first and fourth item.
Example 4:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2
Output: 24
Explanation: The subset chosen is the first, second, and fourth item.
 

Note:

1 <= values.length == labels.length <= 20000
0 <= values[i], labels[i] <= 20000
1 <= num_wanted, use_limit <= values.length
"""
from collections import defaultdict
class Solution_2:
    def largestValsFromLabels(self, values, labels, num_wanted: int, use_limit: int) -> int:
        if use_limit >= num_wanted :
            return sum(sorted(values, reverse = True)[:num_wanted])
        n = num_wanted - use_limit #nums should be allocted to already existing labels
        lable_length = len(set(labels))
        dp = [[0]*num_wanted]*lable_length
        print(dp)
        label_dict = defaultdict(list)
        for i in range(len(values)):
            label_dict[labels[i]].append(values[i])
        for key in label_dict.keys():
            label_dict[key] = sorted(label_dict[key], reverse = True)
        print(label_dict)
        return 0

class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted: int, use_limit: int) -> int:
        res = 0
        labels_counts = dict()
        values_labels = sorted(zip(values, labels), reverse = True, key = lambda x:x[0])
        # values_labels = [(values[i],labels[i]) for i in range(len(values))]
        # values_labels = sorted(values_labels, key = lambda x:x[0], reverse = True)
        nums = 0
        # print(values_labels)
        for v,l in values_labels:
            labels_counts[l] = labels_counts.get(l,0) + 1
            if labels_counts[l] <= use_limit:
                res += v
                nums += 1
                if nums >= num_wanted:
                    return res
        return res


s = Solution()
values = [9,8,8,7,6]
labels = [0,0,0,1,1]
num_wanted = 3
use_limit = 2
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))
values = [5,4,3,2,1]
labels = [1,1,2,2,3]
num_wanted = 3
use_limit = 1
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))
values = [5,4,3,2,1]
labels = [1,3,3,3,2]
num_wanted = 3
use_limit = 2
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))
values = [9,8,8,7,6]
labels = [0,0,0,1,1]
num_wanted = 3
use_limit = 1
print(s.largestValsFromLabels(values, labels, num_wanted, use_limit))