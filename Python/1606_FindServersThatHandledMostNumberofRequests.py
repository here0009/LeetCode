"""
You have k servers numbered from 0 to k-1 that are being used to handle multiple requests simultaneously. Each server has infinite computational capacity but cannot handle more than one request at a time. The requests are assigned to servers according to a specific algorithm:

The ith (0-indexed) request arrives.
If all servers are busy, the request is dropped (not handled at all).
If the (i % k)th server is available, assign the request to that server.
Otherwise, assign the request to the next available server (wrapping around the list of servers and starting from 0 if necessary). For example, if the ith server is busy, try to assign the request to the (i+1)th server, then the (i+2)th server, and so on.
You are given a strictly increasing array arrival of positive integers, where arrival[i] represents the arrival time of the ith request, and another array load, where load[i] represents the load of the ith request (the time it takes to complete). Your goal is to find the busiest server(s). A server is considered busiest if it handled the most number of requests successfully among all the servers.

Return a list containing the IDs (0-indexed) of the busiest server(s). You may return the IDs in any order.

 

Example 1:


Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
Output: [1] 
Explanation:
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
Example 2:

Input: k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
Output: [0]
Explanation:
The first 3 requests are handled by first 3 servers.
Request 3 comes in. It is handled by server 0 since the server is available.
Server 0 handled two requests, while servers 1 and 2 handled one request each. Hence server 0 is the busiest server.
Example 3:

Input: k = 3, arrival = [1,2,3], load = [10,12,11]
Output: [0,1,2]
Explanation: Each server handles a single request, so they are all considered the busiest.
Example 4:

Input: k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
Output: [1]
Example 5:

Input: k = 1, arrival = [1], load = [1]
Output: [0]
 

Constraints:

1 <= k <= 105
1 <= arrival.length, load.length <= 105
arrival.length == load.length
1 <= arrival[i], load[i] <= 109
arrival is strictly increasing.
"""


class Solution:
    def busiestServers(self, k, arrival, load):
        """
        TLE
        """
        servers = [[float('-inf')] for _ in range(k)]
        length = len(arrival)
        for i in range(length):
            time, duration = arrival[i], load[i]
            counts = 0
            j = i % k

            while counts < k:
                if servers[j][-1] <= time:
                    servers[j].append(time + duration)
                    break
                else:
                    counts += 1
                    j = (j+1) % k
        max_len = max(len(s) for s in servers)
        # print(servers)
        return [i for i in range(k) if len(servers[i]) == max_len]

class Solution:
    def busiestServers(self, k, arrival, load):
        servers_time = [0]*k
        length = len(arrival)
        servers_counts = [0]*k
        for i in range(length):
            time, duration = arrival[i], load[i]
            counts = 0
            j = i % k
            while counts < k:
                if servers_time[j] <= time:
                    servers_time[j] = time + duration
                    servers_counts[j] += 1
                    break
                else:
                    counts += 1
                    j = (j+1) % k
        max_len = max(servers_counts)
        # print(servers)
        return [i for i in range(k) if servers_counts[i] == max_len]


import heapq
class Solution:
    def busiestServers(self, k, arrival, load):
        end_time = []
        length = len(arrival)
        counts = [0]*k
        before = list(range(k))
        after = []
        for i in range(length):
            time, duration = arrival[i], load[i]
            servers_id = i % k
            if servers_id == 0:
                after = before
                before = []
            while end_time and end_time[0][0] <= time:
                node = heapq.heappop(end_time)[1]
                if node < servers_id:
                    heapq.heappush(before, node)
                else:
                    heapq.heappush(after, node)
            q = after if after else before
            # print(end_time, after, before, q)
            if not q:
                continue
            node = heapq.heappop(q)
            counts[node] += 1
            heapq.heappush(end_time, (time+duration, node)) #we do not have to push back the not using node in after/before to end_time, because if they are avilable now,  they can also be used nextround.(arrive time is in ascending order)

        max_len = max(counts)
        # print('counts',counts)
        return [i for i in range(k) if counts[i] == max_len]

S = Solution()
k = 3
arrival = [1,2,3,4,5]
load = [5,2,3,3,3] 
print(S.busiestServers(k, arrival, load))
k = 3
arrival = [1,2,3,4]
load = [1,2,1,2]
print(S.busiestServers(k, arrival, load))
k = 3
arrival = [1,2,3]
load = [10,12,11]
print(S.busiestServers(k, arrival, load))
k = 3
arrival = [1,2,3,4,8,9,10]
load = [5,2,10,3,1,2,2]
print(S.busiestServers(k, arrival, load))
k = 1
arrival = [1]
load = [1]
print(S.busiestServers(k, arrival, load))