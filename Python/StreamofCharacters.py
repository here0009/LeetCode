"""
Implement the StreamChecker class as follows:

StreamChecker(words): Constructor, init the data structure with the given words.
query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.
 

Example:

StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the dictionary.
streamChecker.query('a');          // return false
streamChecker.query('b');          // return false
streamChecker.query('c');          // return false
streamChecker.query('d');          // return true, because 'cd' is in the wordlist
streamChecker.query('e');          // return false
streamChecker.query('f');          // return true, because 'f' is in the wordlist
streamChecker.query('g');          // return false
streamChecker.query('h');          // return false
streamChecker.query('i');          // return false
streamChecker.query('j');          // return false
streamChecker.query('k');          // return false
streamChecker.query('l');          // return true, because 'kl' is in the wordlist
 

Note:

1 <= words.length <= 2000
1 <= words[i].length <= 2000
Words will only consist of lowercase English letters.
Queries will only consist of lowercase English letters.
The number of queries is at most 40000.
"""
class StreamChecker_1:
    """
    Time Limit Error
    """
    
    def __init__(self, words):
        self.query_cache = ''
        self.words = words
        

    def query(self, letter: str) -> bool:
        self.query_cache += letter
        # print(self.query_cache)
        for word in self.words:
            if self.query_cache.endswith(word):
                return True
        return False
        

from collections import defaultdict
class StreamChecker:
    
    def __init__(self, words):
        self.query_cache = ''
        self.word_dict = defaultdict(set)
        for word in words:
            self.word_dict[word[-1]].add(word)
        
        

    def query(self, letter: str) -> bool:
        self.query_cache += letter
        # print(self.query_cache)

        for word in self.word_dict[letter]:
            if self.query_cache.endswith(word):
                return True
        return False


class StreamChecker:
    
    def __init__(self, words):
        self.trie = {}
        self.query_cache = ''
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['end'] = True

        
        

    def query(self, letter: str) -> bool:
        self.query_cache += letter
        node = self.trie
        print(node)
        for c in self.query_cache[::-1]:
            if c not in node:
                return False
            else:
                node = node[c]
            if 'end' in node:
                return True
        return False




# Your StreamChecker object will be instantiated and called as such:
words = ["cd","f","kl"]
obj = StreamChecker(words)
letters = 'abcdefghijkl'
for letter in letters:
    print(obj.query(letter))
