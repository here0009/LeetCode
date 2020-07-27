"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:

Input: "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
Example 2:

Input: "/../"
Output: "/"
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.
Example 3:

Input: "/home//foo/"
Output: "/home/foo"
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.
Example 4:

Input: "/a/./b/../../c/"
Output: "/c"
Example 5:

Input: "/a/../../b/../c//.//"
Output: "/c"
Example 6:

Input: "/a//b////c/d//././/.."
Output: "/a/b/c"

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        # print(path_list)
        res_list = ['']
        index = 0
        for p in path_list:
            if not p or p == '.':
                continue
            if p == '..':
                index = max(0, index-1)
            else:
                index += 1
                if index >= len(res_list):
                    res_list.append(p)
                else:
                    res_list[index]  = p
        res = '/'.join(res_list[:index+1])
        if not res:
            res = '/'
        return res


class Solution:
    def simplifyPath(self, path):
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)
        return '/' + '/'.join(stack)
S = Solution()
path = "/home/"
print(S.simplifyPath(path))
path = "/../"
print(S.simplifyPath(path))
path = "/home//foo/"
print(S.simplifyPath(path))
path = "/a/./b/../../c/"
print(S.simplifyPath(path))
path = "/a/../../b/../c//.//"
print(S.simplifyPath(path))
path = "/a//b////c/d//././/.."
print(S.simplifyPath(path))