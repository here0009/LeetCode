"""
We will use a file-sharing system to share a very large file which consists of m small chunks with IDs from 1 to m.

When users join the system, the system should assign a unique ID to them. The unique ID should be used once for each user, but when a user leaves the system, the ID can be reused again.

Users can request a certain chunk of the file, the system should return a list of IDs of all the users who own this chunk. If the user receive a non-empty list of IDs, they receive the requested chunk successfully.


Implement the FileSharing class:

FileSharing(int m) Initializes the object with a file of m chunks.
int join(int[] ownedChunks): A new user joined the system owning some chunks of the file, the system should assign an id to the user which is the smallest positive integer not taken by any other user. Return the assigned id.
void leave(int userID): The user with userID will leave the system, you cannot take file chunks from them anymore.
int[] request(int userID, int chunkID): The user userID requested the file chunk with chunkID. Return a list of the IDs of all users that own this chunk sorted in ascending order.
 

Follow-ups:

What happens if the system identifies the user by their IP address instead of their unique ID and users disconnect and connect from the system with the same IP?
If the users in the system join and leave the system frequently without requesting any chunks, will your solution still be efficient?
If all each user join the system one time, request all files and then leave, will your solution still be efficient?
If the system will be used to share n files where the ith file consists of m[i], what are the changes you have to do?
 

Example:

Input:
["FileSharing","join","join","join","request","request","leave","request","leave","join"]
[[4],[[1,2]],[[2,3]],[[4]],[1,3],[2,2],[1],[2,1],[2],[[]]]
Output:
[null,1,2,3,[2],[1,2],null,[],null,1]
Explanation:
FileSharing fileSharing = new FileSharing(4); // We use the system to share a file of 4 chunks.

fileSharing.join([1, 2]);    // A user who has chunks [1,2] joined the system, assign id = 1 to them and return 1.

fileSharing.join([2, 3]);    // A user who has chunks [2,3] joined the system, assign id = 2 to them and return 2.

fileSharing.join([4]);       // A user who has chunk [4] joined the system, assign id = 3 to them and return 3.

fileSharing.request(1, 3);   // The user with id = 1 requested the third file chunk, as only the user with id = 2 has the file, return [2] . Notice that user 1 now has chunks [1,2,3].

fileSharing.request(2, 2);   // The user with id = 2 requested the second file chunk, users with ids [1,2] have this chunk, thus we return [1,2].

fileSharing.leave(1);        // The user with id = 1 left the system, all the file chunks with them are no longer available for other users.

fileSharing.request(2, 1);   // The user with id = 2 requested the first file chunk, no one in the system has this chunk, we return empty list [].

fileSharing.leave(2);        // The user with id = 2 left the system.

fileSharing.join([]);        // A user who doesn't have any chunks joined the system, assign id = 1 to them and return 1. Notice that ids 1 and 2 are free and we can reuse them.
 

Constraints:

1 <= m <= 10^5
0 <= ownedChunks.length <= min(100, m)
1 <= ownedChunks[i] <= m
Values of ownedChunks are unique.
1 <= chunkID <= m
userID is guaranteed to be a user in the system if you assign the IDs correctly. 
At most 10^4 calls will be made to join, leave and request.
Each call to leave will have a matching call for join.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-a-file-sharing-system
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import defaultdict
import heapq
class FileSharing:

    def __init__(self, m: int):
        self.files = defaultdict(set)
        self.users = defaultdict(set)
        self.ids = []
        self.index = 1

    def join(self, ownedChunks) -> int:
        if not self.ids:
            userID = self.index
            self.index += 1
        else:
            userID = heapq.heappop(self.ids)
        self.users[userID] = set(ownedChunks)
        for file in ownedChunks:
            self.files[file].add(userID)
        return userID

    def leave(self, userID: int) -> None:
        for file in self.users[userID]:
            self.files[file].remove(userID)
        heapq.heappush(self.ids, userID)

    def request(self, userID: int, chunkID: int):
        if not self.files[chunkID]:
            return []
        res = sorted(list(self.files[chunkID]))
        self.files[chunkID].add(userID)
        self.users[userID].add(chunkID)
        return res





# Your FileSharing object will be instantiated and called as such:

a =["FileSharing","join","join","join","join","join","request","request","request","request","request","request","request","request","request","request","request","request","request","request","request"]
b = [[40],[[35,20,14,40,3,24,10,7,4,31,12,5,39,27,17,36,2,32,37,1,23,30,15,22]],[[33,35,23,15,8,24,3,34,28,19,36,31]],[[]],[[27,18,37,16,9,31,13,22,4,34,36,10,28,26,38]],[[40,39,35,30,16,7,33,32,18,15,25,23,11,22,36,4,8,2,1,29,17,28,3,10,20,37,38,24]],[4,1],[4,27],[2,28],[2,30],[2,26],[3,29],[3,19],[4,6],[4,6],[4,38],[1,33],[5,29],[4,19],[4,26],[5,16]]

c =[None,1,2,3,4,5,[1,5],[1,4],[2,4,5],[1,5],[4],[5],[2],[],[4],[4,5],[2,5],[3,5],[2,3],[2,4],[4,5]]
d = [None,1,2,3,4,5,[1,5],[1,4],[2,4,5],[1,5],[4],[5],[2],[],[],[4,5],[2,5],[3,5],[2,3],[2,4],[4,5]]
for i in range(len(a)):
    print(a[i], b[i], c[i], d[i])