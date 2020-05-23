"""
There are n people, each person has a unique start between 0 and n-1. Given the arrays watchedVideos and friends, where watchedVideos[i] and friends[i] contain the list of watched videos and the list of friends respectively for the person with start = i.

Level 1 of videos are all watched videos by your friends, level 2 of videos are all watched videos by the friends of your friends and so on. In general, the level k of videos are all watched videos by people with the shortest path equal to k with you. Given your start and the level of videos, return the list of videos ordered by their frequencies (increasing). For videos with the same frequency order them alphabetically from least to greatest. 

 

Example 1:



Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], start = 0, level = 1
Output: ["B","C"] 
Explanation: 
You have start = 0 (green color in the figure) and your friends are (yellow color in the figure):
Person with start = 1 -> watchedVideos = ["C"] 
Person with start = 2 -> watchedVideos = ["B","C"] 
The frequencies of watchedVideos by your friends are: 
B -> 1 
C -> 2
Example 2:



Input: watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], start = 0, level = 2
Output: ["D"]
Explanation: 
You have start = 0 (green color in the figure) and the only friend of your friends is the person with start = 3 (yellow color in the figure).
 

Constraints:

n == watchedVideos.length == friends.length
2 <= n <= 100
1 <= watchedVideos[i].length <= 100
1 <= watchedVideos[i][j].length <= 8
0 <= friends[i].length < n
0 <= friends[i][j] < n
0 <= start < n
1 <= level < n
if friends[i] contains j, then friends[j] contains i
"""
# from collections import Counter
class Solution:
    def watchedVideosByFriends(self, watchedVideos, friends, start: int, level: int):
        bfs = [start]
        visited = {start}
        counter = dict()
        while level > 0:
            bfs2 = []
            for node in bfs:
                for f in friends[node]:
                    if f not in visited:
                        bfs2.append(f)
                        visited.add(f)
            level -= 1
            bfs = bfs2
        for node in bfs:
            videos = watchedVideos[node]
            for v in videos:
                counter[v] = counter.get(v,0) + 1
        c_keys = sorted(counter.keys(), key = lambda x: (counter[x],x))
        return c_keys

s = Solution()
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
start = 0
level = 1
print(s.watchedVideosByFriends(watchedVideos, friends, start, level))
watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
start = 0
level = 2
print(s.watchedVideosByFriends(watchedVideos, friends, start, level))

