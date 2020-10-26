"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

 

Example:

Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:

 

Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that all directory names and file names only contain lower-case letters, and same names won't exist in the same directory.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-in-memory-file-system
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class FileSystem:

    def __init__(self):
        self.files = dict()

    def traverse(self, path):
        """
        traverse to the path
        """

        path_list = [s for s in path.split('/') if len(s) > 0 ]
        # print(path)
        # print('files:', self.files)
        directory = self.files
        index = 0
        while index < len(path_list) and path_list[index] in directory:
            if type(directory[path_list[index]]) is str: #  directory is a file
                break
            directory = directory[path_list[index]]
            index += 1
        print('info', directory, path_list[index:])
        return directory, path_list[index:]

    def ls(self, path: str):
        directory, rmd = self.traverse(path)
        # print('ls', path, directory.keys(), 'rmd', rmd, type(directory))
        if rmd and len(rmd[0]) > 0:
            return rmd
            # print(directory)
            # return directory
        # print(directory)
        return sorted(list(directory.keys()))

    def mkdir(self, path: str) -> None:

        directory, path_list = self.traverse(path)
        for path in path_list:
            directory[path] = dict()
            directory = directory[path]

    def addContentToFile(self, filePath: str, content: str) -> None:
        index = filePath.rfind('/')
        file, path = filePath[index+1:], filePath[:index]
        # print('info', file, path, content)
        directory, _ = self.traverse(path)
        # print('directory::', directory)
        if file not in directory:
            directory[file] = ''
        directory[file] += content


    def readContentFromFile(self, filePath: str) -> str:
        index = filePath.rfind('/')
        file, path = filePath[index+1:], filePath[:index]
        directory, _ = self.traverse(path)
        return directory[file]



class FileSystem:

    def __init__(self):
        self.files = dict()

    def traverse(self, path):
        """
        traverse to the path
        """
        path_list = [s for s in path.split('/') if len(s) > 0 ]
        directory = self.files
        index = 0
        while index < len(path_list) and path_list[index] in directory:
            if type(directory[path_list[index]]) is str: #  directory is a file
                break
            directory = directory[path_list[index]]
            index += 1
        return directory, path_list[index:]

    def ls(self, path: str):
        directory, rmd = self.traverse(path)
        if rmd:
            return rmd
        return sorted(list(directory.keys()))

    def mkdir(self, path: str) -> None:
        directory, path_list = self.traverse(path)
        for path in path_list:
            directory[path] = dict()
            directory = directory[path]

    def addContentToFile(self, filePath: str, content: str) -> None:
        index = filePath.rfind('/')
        file, path = filePath[index+1:], filePath[:index]
        directory, _ = self.traverse(path)
        if file not in directory:
            directory[file] = ''
        directory[file] += content


    def readContentFromFile(self, filePath: str) -> str:
        index = filePath.rfind('/')
        file, path = filePath[index+1:], filePath[:index]
        directory, _ = self.traverse(path)
        return directory[file]


# Your FileSystem object will be instantiated and called as such:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],[],[],[],["/"],[]]
fs = FileSystem()
print(fs.ls("/"))
print(fs.mkdir("/a/b/c"))
print(fs.addContentToFile("/a/b/c/d", "hello"))
print(fs.readContentFromFile("/a/b/c/d"))
print(fs.addContentToFile("/a/b/c/d", "world"))
print(fs.readContentFromFile("/a/b/c/d"))

l1 = ["FileSystem","mkdir","ls","mkdir","ls","ls","ls","addContentToFile","ls","ls","ls"]
l2 = [[],["/m"],["/m"],["/w"],["/"],["/w"],["/"],["/dycete","emer"],["/w"],["/"],["/dycete"]]
for p,q in zip(l1, l2):
    print(p, q)

# AttributeError: 'str' object has no attribute 'keys'
#     return sorted(list(directory.keys()))
# Line 24 in ls (Solution.py)
#     result = obj.ls(
# Line 57 in __helper_select_method__ (Solution.py)
#     ret.append(__DriverSolution__().__helper_select_method__(method, params[index], obj))
# Line 112 in _driver (Solution.py)
#     _driver()
# Line 122 in <module> (Solution.py)

