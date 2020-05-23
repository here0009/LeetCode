"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
class Solution_1:
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x:x[1], reverse = True)
        people = sorted(people, key = lambda x:x[0])
        # print(people)
        res = [None]*len(people)
        for h, k in people:
            non_counts = 0
            index = 0
            while index < len(res) :
                if not res[index]:
                    non_counts += 1
                    if non_counts == k+1:
                        break
                index += 1
            res[index] = [h,k]
        return res

class Solution:
    def reconstructQueue(self, people):
        people = sorted(people, key = lambda x:(-x[0],x[1]))
        # print(people)
        res = []
        for h,k in people:
            res.insert(k, [h,k])
        return res

s = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(people))

people = [[5,0]]
print(s.reconstructQueue(people))
