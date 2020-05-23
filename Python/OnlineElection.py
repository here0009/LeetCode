"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
 

Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""

from bisect import bisect_left
from bisect import bisect
from bisect import bisect_right
class TopVotedCandidate:
    def __init__(self, persons, times):
        votes = dict()
        self.times_dict = dict()
        self.times = times
        self.len = len(times)
        max_value, max_key = 0, None
        for i in range(self.len):
            t,p = times[i], persons[i]
            votes[p] = votes.get(p,0) + 1
            if votes[p] >= max_value:
                max_value = votes[p]
                max_key = p
            self.times_dict[t] = max_key
        # print(self.times)
        # print(self.times_dict)

    def q(self, t: int) -> int:
        # index_left = bisect_left(self.times,t)
        # index_right = bisect_right(self.times,t)
        # if index >= self.len or t != self.times[index]:
        #     index -= 1
        index = bisect(self.times,t)-1 #bisect equals to biscet_right, return the index which m[index] > query
        # print(t,index+1,index_left,index_right)
        return self.times_dict[self.times[index]]


# Your TopVotedCandidate object will be instantiated and called as such:
persons = [0,1,1,0,0,1,0]
times = [0,5,10,15,20,25,30]
obj = TopVotedCandidate(persons, times)

queries = [3,12,25,15,24,8,30,31]
for t in queries:
    print(t, obj.q(t))