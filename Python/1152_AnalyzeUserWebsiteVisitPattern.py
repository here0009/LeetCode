"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: 
The tuples in this example are:
["joe", 1, "home"]
["joe", 2, "about"]
["joe", 3, "career"]
["james", 4, "home"]
["james", 5, "cart"]
["james", 6, "maps"]
["james", 7, "home"]
["mary", 8, "home"]
["mary", 9, "about"]
["mary", 10, "career"]
The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
 

Note:

3 <= N = username.length = timestamp.length = website.length <= 50
1 <= username[i].length <= 10
0 <= timestamp[i] <= 10^9
1 <= website[i].length <= 10
Both username[i] and website[i] contain only lowercase characters.
It is guaranteed that there is at least one user who visited at least 3 websites.
No user visits two websites at the same time.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/analyze-user-website-visit-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
from collections import defaultdict
from itertools import combinations
class Solution_1:
    def mostVisitedPattern(self, username, timestamp, website):
        info = sorted(zip(username, timestamp, website))
        # print(info)
        # info = zip(username, timestamp, website)

        record = defaultdict(list)
        counts = Counter()
        for u, t, w in info:
            record[u].append(w)
        for _, lst in record.items():
            visited = set()
            for comb in combinations(lst, 3):
                comb = tuple(comb)
                if comb not in visited:
                    counts[comb] += 1
                    visited.add(comb)
        # print(counts)
        max_v, max_key = 0, ''
        for key, v in counts.items():
            if v > max_v or (v == max_v and key < max_key):
                max_v = v
                max_key = key
        return list(max_key)


# 作者：hanghangblackcat
# 链接：https://leetcode-cn.com/problems/analyze-user-website-visit-pattern/solution/python-dict-by-hanghangblackcat-2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
from typing import List
import itertools
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        data = [[username[i], timestamp[i], website[i]] for i in range(len(username))]
        data.sort()
        d = defaultdict(list)
        for u, t, w in data:
            d[u].append(w)
        print(data)
        res = defaultdict(set)
        for i, v in d.items():
            for j in itertools.combinations(v, 3):
                res[j].add(i)
        print(res)
        return sorted(res.items(), key=lambda a:(-len(a[1]), a[0]))[0][0]


S = Solution_1()
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
print(S.mostVisitedPattern(username, timestamp, website))

username =["zkiikgv","zkiikgv","zkiikgv","zkiikgv"]
timestamp =[436363475,710406388,386655081,797150921]
website = ["wnaaxbfhxp","mryxsjc","oz","wlarkzzqht"]
print(S.mostVisitedPattern(username, timestamp, website))


# 输出：
# ["oz","wnaaxbfhxp","mryxsjc"]
# 预期结果：
# ["oz","mryxsjc","wlarkzzqht"]