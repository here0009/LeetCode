"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

Thoughts:
the sum of h and k is larger or equal than the previous one.
so sort sum(h+k), then sort k.

the thought is wrong because, if two people got the same h+k, it is very hard to decide how to sort them, you can not neither sort them on h nor on k. like the example: [7,0], [5,2], [6,1].
According to the hints, it is a good idea to insert the people to the right positon in the list from the shortest to the highest based on h and k.
For example, the height of the shortest one is 4, and there is 4 people in front of him, so him will be inserted to positon 4. 
The next one is [5, 0], it will be inserted to positon 0. So on...
"""
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        
        """
        people.sort(key = lambda x: x[0])
        people_recontruct = [0] * len(people)
        for p in people:
            
        return people

s = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(s.reconstructQueue(people))
        