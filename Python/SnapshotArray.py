"""
Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
 

Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
 

Constraints:

1 <= length <= 50000
At most 50000 calls will be made to set, snap, and get.
0 <= index < length
0 <= snap_id < (the total number of times we call snap())
0 <= val <= 10^9
"""

class SnapshotArray_1:
    """
    MLE
    """
    def __init__(self, length: int):
        self.id = -1
        self.vals_dict = dict()
        self.root = dict()
        self.vals = [0]*length
        
    def findRoot(self,index):
        if self.root[index] != index:
            self.root[index] = self.findRoot(self.root[index])
        return self.root[index]

    def set(self, index: int, val: int) -> None:
        self.vals[index] = val
        

    def snap(self) -> int:
        if self.id >= 0 and self.vals == self.vals_dict[self.findRoot(self.id)]:
            self.root[self.id + 1] = self.findRoot(self.id)
            self.id += 1
        else:
            self.id += 1
            self.root[self.id] = self.id
            self.vals_dict[self.id] = self.vals[:]
        return self.id

        
    def get(self, index: int, snap_id: int) -> int:
        # print(self.findRoot(snap_id))
        # print(self.vals_dict)
        return self.vals_dict[self.findRoot(snap_id)][index]


class SnapshotArray:
    """
    use dict to store the changed vals, others will be zero
    """
    def __init__(self, length: int):
        self.id = -1
        self.vals_dict = dict()
        self.root = dict()
        self.vals = dict()
        

    def set(self, index: int, val: int) -> None:
        self.vals[index] = val
        

    def snap(self) -> int:
        self.id += 1
        self.vals_dict[self.id] = self.vals.copy()
        return self.id

        
    def get(self, index: int, snap_id: int) -> int:
        if index in self.vals_dict[snap_id]:
            return self.vals_dict[snap_id][index]
        else:
            return 0



s = SnapshotArray(3)
s.set(0,5)
print(s.vals)
s.snap()
print(s.vals)
print(s.vals_dict)
s.set(0,6)
print(s.vals)
print(s.get(0,0))
print(s.vals)
s.snap()
s.snap()
s.snap()
print(s.get(0,3))