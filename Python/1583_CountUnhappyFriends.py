"""
You are given a list of preferences for n friends, where n is always even.

For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.

All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.

However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:

x prefers u over y, and
u prefers x over v.
Return the number of unhappy friends.

 

Example 1:

Input: n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
Output: 2
Explanation:
Friend 1 is unhappy because:
- 1 is paired with 0 but prefers 3 over 0, and
- 3 prefers 1 over 2.
Friend 3 is unhappy because:
- 3 is paired with 2 but prefers 1 over 2, and
- 1 prefers 3 over 0.
Friends 0 and 2 are happy.
Example 2:

Input: n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
Output: 0
Explanation: Both friends 0 and 1 are happy.
Example 3:

Input: n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
Output: 4
 

Constraints:

2 <= n <= 500
n is even.
preferences.length == n
preferences[i].length == n - 1
0 <= preferences[i][j] <= n - 1
preferences[i] does not contain i.
All values in preferences[i] are unique.
pairs.length == n/2
pairs[i].length == 2
xi != yi
0 <= xi, yi <= n - 1
Each person is contained in exactly one pair.
"""


class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        pairs_dict = dict()
        for p, q in pairs:
            pairs_dict[p] = q
            pairs_dict[q] = p
        res = 0
        for p in range(n):
            p_list = preferences[p]
            # print('++++', p, p_list)
            for i in p_list:
                if i == pairs_dict[p]:
                    break
                j = pairs_dict[i]
                i_list = preferences[i]
                # print(i, j, i_list)
                if i_list.index(p) < i_list.index(j):
                    res += 1
                    break
            # print(p, res)
        return res

from collections import defaultdict
class Solution:
    def unhappyFriends(self, n: int, preferences, pairs) -> int:
        pre_friends = defaultdict(list) #preffered friend befor current pair
        for p,q in pairs:
            pre_friends[p] = preferences[p][:preferences[p].index(q)]
            pre_friends[q] = preferences[q][:preferences[q].index(p)]

        res = 0
        for p in pre_friends:
            for q in pre_friends[p]:
                if p in pre_friends[q]:
                    res += 1
                    break
        return res




S = Solution()

n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]
print(S.unhappyFriends(n, preferences, pairs))
n = 2
preferences = [[1], [0]]
pairs = [[1, 0]]
print(S.unhappyFriends(n, preferences, pairs))
n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]
print(S.unhappyFriends(n, preferences, pairs))