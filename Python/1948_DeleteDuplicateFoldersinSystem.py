"""
Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.

For example, ["one", "two", "three"] represents the path "/one/two/three".
Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.

For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
/a
/a/x
/a/x/y
/a/z
/b
/b/x
/b/x/y
/b/z
However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.

Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.

 

Example 1:


Input: paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
Output: [["d"],["d","a"]]
Explanation: The file structure is as shown.
Folders "/a" and "/c" (and their subfolders) are marked for deletion because they both contain an empty
folder named "b".
Example 2:


Input: paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
Output: [["c"],["c","b"],["a"],["a","b"]]
Explanation: The file structure is as shown. 
Folders "/a/b/x" and "/w" (and their subfolders) are marked for deletion because they both contain an empty folder named "y".
Note that folders "/a" and "/c" are identical after the deletion, but they are not deleted because they were not marked beforehand.
Example 3:


Input: paths = [["a","b"],["c","d"],["c"],["a"]]
Output: [["c"],["c","d"],["a"],["a","b"]]
Explanation: All folders are unique in the file system.
Note that the returned array can be in a different order as the order does not matter.
Example 4:


Input: paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]
Output: []
Explanation: The file structure is as shown.
Folders "/a/x" and "/b/x" (and their subfolders) are marked for deletion because they both contain an
empty folder named "y".
Folders "/a" and "/b" (and their subfolders) are marked for deletion because they both contain an empty
folder "z" and the folder "x" described above.
Example 5:


Input: paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"],["b","w"]]
Output: [["b"],["b","w"],["b","z"],["a"],["a","z"]]
Explanation: This has the same structure as the previous example, except with the added "/b/w".
Folders "/a/x" and "/b/x" are still marked, but "/a" and "/b" are no longer marked because "/b" has the
empty folder named "w" and "/a" does not.
Note that "/a/z" and "/b/z" are not marked because the set of identical subfolders must be non-empty, but these folders are empty.
 

Constraints:

1 <= paths.length <= 2 * 104
1 <= paths[i].length <= 500
1 <= paths[i][j].length <= 10
1 <= sum(paths[i][j].length) <= 2 * 105
path[i][j] consists of lowercase English letters.
No two paths lead to the same folder.
For any folder not at the root level, its parent folder will also be in the input.
"""

"""
class TreeNode:

    def __init__(self):
        self.children = dict()


class Tree:

    def __init__(self):
        self.root = TreeNode()

    def add_path(self, path):
        node = self.root
        for key in path:
            if key not in root.children:
                node.children[key] = TreeNode()
            node = node.children[key]

    def trimm_tree(self):
        node = self.root
        for key, val 



from typing import List
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        tree = Tree()
        for path in paths:
            tree.add_path(path)
        tree.trimm_tree()
        return tree.get_path()



from typing import List
from collections import defaultdict
class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        children = defaultdict(set)
        parent = defaultdict(set)
        # root0 as the root of folder tree
        all_nodes = set()
        for path in paths:
            parent[path[0]].add('root0')
            children['root0'].add(path[0])
            all_nodes |= set(path)
            for i in range(len(path) - 1):
                children[path[i]].add(path[i + 1])
                parent[path[i + 1]].add(path[i])
        leaves = all_nodes - children.keys()
        print(leaves)
"""


from typing import List
from collections import Counter
class Trie:
    # 当前节点结构的序列化表示
    serial: str = ""
    # 当前节点的子节点
    children: dict

    def __init__(self):
        self.children = dict()


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:

        # 基于深度优先搜索的后序遍历，计算每一个节点结构的序列化表示
        def construct(node: Trie) -> None:
            # 如果是叶节点，那么序列化表示为空字符串，无需进行任何操作
            if not node.children:
                return
            v = list()
            # 如果不是叶节点，需要先计算子节点结构的序列化表示
            for folder, child in node.children.items():
                construct(child)
                v.append(folder + "(" + child.serial + ")")
            
            # 防止顺序的问题，需要进行排序
            v.sort()
            node.serial = "".join(v)
            # 计入哈希表
            freq[node.serial] += 1


        def operate(node: Trie) -> None:
            # 如果序列化表示在哈希表中出现了超过 1 次，就需要删除
            if freq[node.serial] > 1:
                return
            # 否则将路径加入答案
            if path:
                ans.append(path[:])  # deep copy

            for folder, child in node.children.items():
                path.append(folder)
                operate(child)
                path.pop()

        
        # 根节点
        root = Trie()
        for path in paths:
            cur = root
            for node in path:
                if node not in cur.children:
                    cur.children[node] = Trie()
                cur = cur.children[node]

        # 哈希表记录每一种序列化表示的出现次数
        freq = Counter()
        construct(root)
        ans = list()
        # 记录根节点到当前节点的路径
        path = list()
        operate(root)
        return ans


# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/delete-duplicate-folders-in-system/solution/shan-chu-xi-tong-zhong-de-zhong-fu-wen-j-ic32/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Trie:
    def __init__(self):
        self.ss = ""
        self.child = dict()
    
    #----- 往Trie树中插入一个path
    def insert_path(self, path: List[str]) -> None:
        root = self
        for p in path:
            if p not in root.child:
                root.child[p] = Trie()
            root = root.child[p]
        

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        T = Trie()
        
        #---- （1）先把所有的path插入Trie树
        for path in paths:
            T.insert_path(path)
        

        #---- （2）求得每个结点对应的序列
        def dfs_LRN(node: Trie) -> None:
            if len(node.child) == 0:
                return
            ss = []
            for chi, child_trie in node.child.items():
                dfs_LRN(child_trie)
                ss.append(chi + '(' + child_trie.ss + ')')
            ss.sort()
            node.ss = ''.join(ss)
            ss_cnt[node.ss] += 1

        ss_cnt = defaultdict(int)   #每种序列，出现的次数
        dfs_LRN(T) 

        #---- （3）回溯算法，求res
        res = []
        path = []

        def backtrace_get_res(node: Trie) -> None:
            if ss_cnt[node.ss] >= 2:
                return 
            if path:
                res.append(path[:])
            for chi, child_trie in node.child.items():
                path.append(chi)
                backtrace_get_res(child_trie)
                path.pop(-1)
            
        backtrace_get_res(T)
        return res

# 作者：Hanxin_Hanxin
# 链接：https://leetcode-cn.com/problems/delete-duplicate-folders-in-system/solution/cpython3java-trieshu-dfs_lrnha-xi-tong-j-9me5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

S = Solution()
paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
print(S.deleteDuplicateFolder(paths))
paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
print(S.deleteDuplicateFolder(paths))
paths = [["a","b"],["c","d"],["c"],["a"]]
print(S.deleteDuplicateFolder(paths))
paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]
print(S.deleteDuplicateFolder(paths))
paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"],["b","w"]]
print(S.deleteDuplicateFolder(paths))

