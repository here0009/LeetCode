"""
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.

Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
 

Example 1:

Input: 
["FileSystem","createPath","get"]
[[],["/a",1],["/a"]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/a", 1); // return true
fileSystem.get("/a"); // return 1
Example 2:

Input: 
["FileSystem","createPath","createPath","get","createPath","get"]
[[],["/leet",1],["/leet/code",2],["/leet/code"],["/c/d",1],["/c"]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath("/leet", 1); // return true
fileSystem.createPath("/leet/code", 2); // return true
fileSystem.get("/leet/code"); // return 2
fileSystem.createPath("/c/d", 1); // return false because the parent path "/c" doesn't exist.
fileSystem.get("/c"); // return -1 because this path doesn't exist.
 

Constraints:

The number of calls to the two functions is less than or equal to 104 in total.
2 <= path.length <= 100
1 <= value <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-file-system
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



class TrieNode:
    def __init__(self):
        self.children = dict()


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        
        path_list = path.split('/')[1:]
        # print('create' ,path, value, path_list)
        node = self.root
        for word in path_list[:-1]:
            if word not in node.children:
                return False
            node = node.children[word]
        end_word = path_list[-1]
        if end_word in node.children:
            return False
        node.children[end_word] = TrieNode()
        node = node.children[end_word]
        node.children['$'] = value
        # print(end_word, node.children)
        return True

    def get(self, path: str) -> int:
        
        path_list = path.split('/')[1:]
        # print('get', path, path_list)
        node = self.root
        for word in path_list:
            if word not in node.children:
                return -1
            node = node.children[word]
        # print(node.children)
        if '$' in node.children:
            return node.children['$']
        return -1




# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
param_1 = obj.createPath(path,value)
param_2 = obj.get(path)