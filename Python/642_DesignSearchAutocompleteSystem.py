"""
Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#'). For each character they type except '#', you need to return the top 3 historical hot sentences that have prefix the same as the part of sentence already typed. Here are the specific rules:

The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). If several sentences have the same degree of hot, you need to use ASCII-code order (smaller one appears first).
If less than 3 hot sentences exist, then just return as many as you can.
When the input is a special character, it means the sentence ends, and in this case, you need to return an empty list.
Your job is to implement the following functions:

The constructor function:

AutocompleteSystem(String[] sentences, int[] times): This is the constructor. The input is historical data. Sentences is a string array consists of previously typed sentences. Times is the corresponding times a sentence has been typed. Your system should record these historical data.

Now, the user wants to input a new sentence. The following function will provide the next character the user types:

List<String> input(char c): The input c is the next character typed by the user. The character will only be lower-case letters ('a' to 'z'), blank space (' ') or a special character ('#'). Also, the previously typed sentence should be recorded in your system. The output will be the top 3 historical hot sentences that have prefix the same as the part of sentence already typed.

 
Example:
Operation: AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
The system have already tracked down the following sentences and their corresponding times:
"i love you" : 5 times
"island" : 3 times
"ironman" : 2 times
"i love leetcode" : 2 times
Now, the user begins another search:

Operation: input('i')
Output: ["i love you", "island","i love leetcode"]
Explanation:
There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.

Operation: input(' ')
Output: ["i love you","i love leetcode"]
Explanation:
There are only two sentences that have prefix "i ".

Operation: input('a')
Output: []
Explanation:
There are no sentences that have prefix "i a".

Operation: input('#')
Output: []
Explanation:
The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.

 
Note:

The input sentence will always start with a letter and end with '#', and only one blank space will exist between two words.
The number of complete sentences that to be searched won't exceed 100. The length of each sentence including those in the historical data won't exceed 100.
Please use double-quote instead of single-quote when you write test cases even for a character input.
Please remember to RESET your class variables declared in class AutocompleteSystem, as static/class variables are persisted across multiple test cases. Please see here for more details.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/design-search-autocomplete-system
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from collections import Counter
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(list)
    def __repr__(self):
        return ' '.join(self.children.keys())


class AutocompleteSystem:

    def __init__(self, sentences, times):
        self.root = TrieNode()
        self.curr = self.root
        self.search_word = ""
        self.dict = Counter()
        for s, t in zip(sentences, times):
            self.dict[s] += t
            self.insert(s)
        print(self.dict)

    def traverse(self, node):
        res = []
        for nc in node.children:
            if nc == '#':
                res.append(node.children["#"])
            else:
                res.extend(self.traverse(node.children[nc]))
        return res

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.children['#'] = word

    def search(self, c):
        # print(c, self.curr)
        if self.curr and c in self.curr.children:
            self.curr = self.curr.children[c]
            return self.traverse(self.curr)
        else:
            self.curr = None
            return []

    def input(self, c: str):
        if c == "#":
            self.dict[self.search_word] += 1
            self.insert(self.search_word)
            self.search_word = ""
            self.curr = self.root
            return []
        else:
            self.search_word += c
            lst = sorted([(-self.dict[key], key) for key in self.search(c)])
            return [k for v, k in lst[:3]]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
aps = AutocompleteSystem(["i love you", "island","ironman", "i love leetcode"], [5,3,2,2])
print(aps.input('i'))
print(aps.input(' '))
print(aps.input('a'))
print(aps.input('#'))


from collections import defaultdict
from collections import deque
import heapq


class TrieNode:
    def __init__(self, is_word=False, count=0):
        self.count = count  # 用来存当前word被查询过的次数，默认为0
        self.word = ""  # 用来存当前节点代表的word，默认为空，也就是不是单独的word
        self.next = defaultdict(TrieNode)  # 用来存下一个字母对应的节点
    
    def insert(self, word, time):  # 将word插入到当前的节点中
        curr = self
        for ch in word:
            curr = curr.next[ch]  # 用了defaultdict，所以不用做其它的判断初始化之类的
        
        curr.word = word
        curr.count = time
    
    def __lt__(self, other):  # 这里是给TrieNode可比较的特性，不然的话排序的时候要另外加东西辅助
        if self.count < other.count: return True
        elif self.count > other.count: return False
        return self.word > other.word
    
    def get_words(self):  # 搜索从当前节点往下的所有单词，不一定是叶子节点
        ans, queue = list(), deque([self, ])
        while queue:  # 深搜广搜都行，我用了广搜
            curr = queue.popleft()
            if curr.count:  # 只有当前的count不为0，才代表一个单词
                heapq.heappush(ans, curr)  # 用一个大小为3的堆来筛选最终频率高、字典序小的单词
                if len(ans) > 3: heapq.heappop(ans)  # 维护堆的大小
            
            for node in curr.next.values():
                queue.append(node)

        ans.sort(reverse=True)  # 把堆排个序就是答案了，注意要逆序
        return [node.word for node in ans]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
# 作者：cra2yk
# 链接：https://leetcode-cn.com/problems/design-search-autocomplete-system/solution/python-triemo-ni-by-cra2yk/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()  # Trie的根节点
        self.curr = self.root  # 当前遍历到的节点
        self.word = ""  # 当前查询的句子
        # 初始化Trie
        for word, time in zip(sentences, times):
            self.root.insert(word, time)

    def input(self, c: str) -> List[str]:  # 三种情况：1. 结束 2. 没这个前缀 3. 有这个前缀
        if c == '#': return self.process_end(c)
        if c not in self.curr.next: return self.process_not_in(c)
        return self.process_in(c)
    
    def process_end(self, c):  # 结束
        self.curr.word = self.word  # 把到目前为止的查询记录插到Trie里去
        self.curr.count += 1
        self.curr = self.root  # 初始化当前查询的节点和单词，curr and word
        self.word = ""
        return list()
    
    def process_not_in(self, c):  # 没有找到这个前缀
        self.curr = self.curr.next[c]  # 创建新的节点，defaultdict不用额外初始化
        self.word += c  # 维护当前的查询记录
        return list()
    
    def process_in(self, c):  # 有这个前缀
        self.curr = self.curr.next[c]  # 走到具有这个前缀的下一个节点
        self.word += c  # 维护当前的查询记录

        return self.curr.get_words()  # 按频率和字典序返回结果



