"""
There is a hotel with n rooms. The rooms are represented by a 2D integer array rooms where rooms[i] = [roomIdi, sizei] denotes that there is a room with room number roomIdi and size equal to sizei. Each roomIdi is guaranteed to be unique.

You are also given k queries in a 2D array queries where queries[j] = [preferredj, minSizej]. The answer to the jth query is the room number id of a room such that:

The room has a size of at least minSizej, and
abs(id - preferredj) is minimized, where abs(x) is the absolute value of x.
If there is a tie in the absolute difference, then use the room with the smallest such id. If there is no such room, the answer is -1.

Return an array answer of length k where answer[j] contains the answer to the jth query.

 

Example 1:

Input: rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
Output: [3,-1,3]
Explanation: The answers to the queries are as follows:
Query = [3,1]: Room number 3 is the closest as abs(3 - 3) = 0, and its size of 2 is at least 1. The answer is 3.
Query = [3,3]: There are no rooms with a size of at least 3, so the answer is -1.
Query = [5,2]: Room number 3 is the closest as abs(3 - 5) = 2, and its size of 2 is at least 2. The answer is 3.
Example 2:

Input: rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
Output: [2,1,3]
Explanation: The answers to the queries are as follows:
Query = [2,3]: Room number 2 is the closest as abs(2 - 2) = 0, and its size of 3 is at least 3. The answer is 2.
Query = [2,4]: Room numbers 1 and 3 both have sizes of at least 4. The answer is 1 since it is smaller.
Query = [2,5]: Room number 3 is the only room with a size of at least 5. The answer is 3.
 

Constraints:

n == rooms.length
1 <= n <= 105
k == queries.length
1 <= k <= 104
1 <= roomIdi, preferredj <= 107
1 <= sizei, minSizej <= 107

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-room
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List
class Event:
    """
    op: 事件的类型，0 表示房间，1 表示询问
    size: 房间的 size 或者询问的 minSize
    idx: 房间的 roomId 或者询问的 preferred
    origin: 房间在数组 room 中的原始编号或者询问在数组 queries 中的原始编号
    """
    def __init__(self, op: int, size: int, idx: int, origin: int):
        self.op = op
        self.size = size
        self.idx = idx
        self.origin = origin

    """
    自定义比较函数，按照事件的 size 降序排序
    如果 size 相同，优先考虑房间
    """
    def __lt__(self, other: "Event") -> bool:
        return self.size > other.size or (self.size == other.size and self.op < other.op)

class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(queries)

        events = list()
        for i, (roomId, size) in enumerate(rooms):
            # 房间事件
            events.append(Event(0, size, roomId, i))

        for i, (minSize, preferred) in enumerate(queries):
            # 询问事件
            events.append(Event(1, preferred, minSize, i))

        events.sort()

        ans = [-1] * n
        # 存储房间 roomId 的有序集合
        # 需要导入 sortedcontainers 库
        valid = sortedcontainers.SortedList()
        for event in events:
            if event.op == 0:
                # 房间事件，将 roomId 加入有序集合
                valid.add(event.idx)
            else:
                # 询问事件
                dist = float("inf")
                # 查找最小的大于等于 preferred 的元素
                x = valid.bisect_left(event.idx)
                if x != len(valid) and valid[x] - event.idx < dist:
                    dist = valid[x] - event.idx
                    ans[event.origin] = valid[x]
                if x != 0:
                    # 查找最大的严格小于 preferred 的元素
                    x -= 1
                    if event.idx - valid[x] <= dist:
                        dist = event.idx - valid[x]
                        ans[event.origin] = valid[x]
            
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/closest-room/solution/zui-jin-de-fang-jian-by-leetcode-solutio-9ylf/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List
from sortedcontainers import SortedList
import heapq
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        q_idx = [(q[1], q[0], i) for i, q in enumerate(queries)]  # size, room_idx, query_idx
        q_idx.sort()
        pq = [(_s, _i) for _i, _s in rooms]  # size, room_idx
        heapq.heapify(pq)
        rooms.sort()
        rooms = SortedList((_i, _s) for _i, _s in rooms)
        # print(rooms)
        for size, room_idx, query_idx in q_idx:
            while pq and pq[0][0] < size:
                _s, _i = heapq.heappop(pq)
                rooms.remove((_i, _s))
            j = rooms.bisect_left((room_idx, 0))
            candi = [rooms[_j][0] for _j in [j - 1, j] if _j >= 0 and _j < len(rooms)]
            if not candi:
                continue
            candi.sort(key=lambda x: abs(x - room_idx))
            res[query_idx] = candi[0]
        return res


from typing import List
from sortedcontainers import SortedList
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [-1] * len(queries)
        q_idx = [(q[1], q[0], i) for i, q in enumerate(queries)]  # size, room_idx, query_idx
        q_idx.sort(reverse=True)
        rooms.sort(key=lambda x: x[1], reverse=True)
        room_idx = 0
        len_room = len(rooms)
        reserve = SortedList()
        # print(rooms)
        for size, _r, _q in q_idx:
            while room_idx < len_room and rooms[room_idx][1] >= size:
                reserve.add(rooms[room_idx])
                room_idx += 1
            j = reserve.bisect_left([_r, 0])
            candi = [reserve[_j][0] for _j in [j - 1, j] if _j >= 0 and _j < len(reserve)]
            if not candi:
                continue
            candi.sort(key=lambda x: abs(x - _r))
            res[_q] = candi[0]
        return res

S = Solution()
rooms = [[2,2],[1,2],[3,2]]
queries = [[3,1],[3,3],[5,2]]
print(S.closestRoom(rooms, queries))
rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]]
queries = [[2,3],[2,4],[2,5]]
print(S.closestRoom(rooms, queries))
rooms = [[23,22],[6,20],[15,6],[22,19],[2,10],[21,4],[10,18],[16,1],[12,7],[5,22]]
queries = [[12,5],[15,15],[21,6],[15,1],[23,4],[15,11],[1,24],[3,19],[25,8],[18,6]]
print(S.closestRoom(rooms, queries))




