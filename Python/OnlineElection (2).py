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
class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.persons = persons
        self.times = times

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        def find_t(t, left, right):
            if t == self.times[right]:
                return right
            if t == self.times[left] or right - left == 1:
                return left
            middle = (right - left)//2
            if t == self.times[middle]:
                return middle
            elif t <  self.times[middle]:
                return find_t(t, left, middle)
            else:
                return find_t(t, middle, right)
                
        index = find_t(t, 0, len(self.times)-1)
        votes_all = index + 1
        votes_1 = sum(self.persons[:index+1])
        if votes_1 > votes_all - votes_1:
            return 1
        elif votes_1 < votes_all - votes_1:
            return 0
        else:
            return self.persons[index] 




# Your TopVotedCandidate object will be instantiated and called as such:

# param_1 = obj.q(t)
t_s = [3, 12, 25, 15, 24, 8]
persons = [0,1,1,0,0,1,0]
times = [0,5,10,15,20,25,30]
obj = TopVotedCandidate(persons, times)
for t in t_s:
    print(obj.q(t))