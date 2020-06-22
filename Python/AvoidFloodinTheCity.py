"""
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. Your goal is to avoid the flood in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes. (see example 4)

 

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.
Example 4:

Input: rains = [69,0,0,0,69]
Output: [-1,69,1,1,-1]
Explanation: Any solution on one of the forms [-1,69,x,y,-1], [-1,x,69,y,-1] or [-1,x,y,69,-1] is acceptable where 1 <= x,y <= 10^9
Example 5:

Input: rains = [10,20,20]
Output: []
Explanation: It will rain over lake 20 two consecutive days. There is no chance to dry any lake.
 

Constraints:

1 <= rains.length <= 10^5
0 <= rains[i] <= 10^9
"""


# from collections import deque
import bisect
class Solution:
    def avoidFlood(self, rains):
        length = len(rains)
        res = [-1]*length
        dry = []
        rain_dict = dict()
        for index, rain in enumerate(rains):
            if rain <= 0:
                dry.append(index)
                res[index] = 1
            else:
                if rain not in rain_dict:
                    rain_dict[rain] = index
                else:
                    di = bisect.bisect_left(dry, rain_dict[rain])
                    # print(dry,di,k)
                    if di == len(dry):
                        return []
                    else:
                        res[dry.pop(di)] = rain
                        rain_dict[rain] = index
        return res


# https://leetcode.com/problems/avoid-flood-in-the-city/discuss/697703/python-greedy-with-a-heap
from collections import defaultdict
from collections import deque
import heapq
class Solution:
    def avoidFlood(self, rains):
        closest = []
        res = []
        locs = defaultdict(deque)
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        # print(rains)
        for i, lake in enumerate(rains):
            # print(i, lake, res)
            if closest and closest[0] == i:
                return []
            if lake == 0:
                if not closest:
                    res.append(1)
                    continue
                nxt = heapq.heappop(closest)
                res.append(rains[nxt])
            else:
                lst = locs[lake]
                lst.popleft()
                if lst:
                    nxt = lst[0]
                    heapq.heappush(closest, nxt)
                res.append(-1)
        return res


class Solution_1:
    def avoidFlood(self, rains):
        closest = []
        locs = defaultdict(deque)
        for i, lake in enumerate(rains):
            locs[lake].append(i)
        ret = []
        for i, lake in enumerate(rains):
            if closest and closest[0] == i:
                return []
            if not lake:
                if not closest:
                    ret.append(1) 
                    continue
                nxt = heapq.heappop(closest)
                ret.append(rains[nxt])
            else:
                l = locs[lake]
                l.popleft()
                if l:
                    nxt = l[0]
                    heapq.heappush(closest, nxt)
                ret.append(-1)
        return ret


S = Solution()
rains = [1,2,3,4]
print(S.avoidFlood(rains))
rains = [1,2,0,0,2,1]
print(S.avoidFlood(rains))
rains = [1,2,0,1,2]
print(S.avoidFlood(rains))
rains = [69,0,0,0,69]
print(S.avoidFlood(rains))
rains = [10,20,20]
print(S.avoidFlood(rains))

rains = [0,1,1]
print(S.avoidFlood(rains))
rains = [2,3,0,0,3,1,0,1,0,2,2]
print(S.avoidFlood(rains))
# Output:
# [-1,-1,3,2,-1,-1,1,-1,1,-1,-1]
# Expected:
# []