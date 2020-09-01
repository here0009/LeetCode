"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""


from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        """
        TLE
        """
        def editDistance(a, b):
            return sum(a[i]!=b[i] for i in range(len_w))

        def dfs(index, path):
            # print(index, path, self.res)
            word = wordList[index]
            path = path + [word]# we can not use path.append(word) here, because it will change path in other dfs functions
            if len(path) > self.min_len:
                return
            if word == endWord:
                if len(path) < self.min_len:
                    self.min_len = len(path)
                    self.res = [path]
                elif len(path) == self.min_len:
                    self.res.append(path)
                return
            for j in edges[index]:
                if not visited[j]:
                    visited[j] = 1
                    dfs(j, path)
                    visited[j] = 0


        edges = defaultdict(set)
        wordList = [beginWord] + wordList
        length = len(wordList)
        len_w = len(wordList[0])
        for i in range(length-1):
            for j in range(i+1, length):
                if editDistance(wordList[i], wordList[j]) == 1:
                    edges[i].add(j)
                    edges[j].add(i)

        # print(wordList)
        # print(edges)
        self.res = []
        self.min_len = float('inf')
        visited = [0]*length
        visited[0] = 1
        dfs(0, [])
        # print(self.min_len, self.res)
        # print()
        return self.res

from collections import defaultdict
class Solution:
    """
    still TLE
    """
    def findLadders(self, beginWord: str, endWord: str, wordList):
        def editDistance(a, b):
            return sum(a[i]!=b[i] for i in range(len_w))

        edges = defaultdict(set)
        wordList = [beginWord] + wordList
        length = len(wordList)
        len_w = len(wordList[0])
        for i in range(length-1):
            for j in range(i+1, length):
                if editDistance(wordList[i], wordList[j]) == 1:
                    edges[i].add(j)
                    edges[j].add(i)

        for i in range(length):
            if wordList[i] == endWord:
                target = i
                break
        else:
            return []
        # print(wordList)
        # print(edges)
        self.res = []
        bfs = [0]
        visited = [0]*length
        visited[0] = 1
        path_dict = defaultdict(set)
        path_dict[0].add(str(0))
        while bfs:
            if target in path_dict:
                break
            bfs2 = []
            path_dict2 = defaultdict(set)
            for i in bfs:
                for j in edges[i]:
                    if j not in path_dict:
                        bfs2.append(j)
                        for p in path_dict[i]:
                            path_dict2[j].add(p+' '+str(j))
            for k, v in path_dict2.items():
                path_dict[k] = v
            bfs = bfs2


        res = []
        # print(wordList)
        # print(path_dict)
        if target not in path_dict:
            return res
        for lst in path_dict[target]:
            res.append([wordList[int(i)] for i in lst.split()])
        return res


from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        len_w = len(beginWord)
        path_dict = defaultdict(list)
        path_dict[beginWord] = [[beginWord]] # record the path from begin to end
        visited = {beginWord} # record visited word
        bfs = {beginWord}

        while bfs:
            if endWord in bfs:
                break
            bfs2 = set()
            for word in bfs:
                for j in range(len_w):
                    for k in range(ord('a'), ord('a')+26): 
                        word2 = word[:j] + chr(k) + word[j+1:] # all possible words with one letter replaced
                        if word2 in word_set and word2 not in visited:
                            path_dict[word2].extend([p + [word2] for p in path_dict[word]])
                            bfs2.add(word2)
            visited |= bfs2
            bfs = bfs2

        if endWord not in path_dict:
            return []
        return path_dict[endWord]

S = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(S.findLadders(beginWord, endWord, wordList))

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print(S.findLadders(beginWord, endWord, wordList))
beginWord ="red"
endWord ="tax"
wordList = ["ted","tex","red","tax","tad","den","rex","pee"]
print(S.findLadders(beginWord, endWord, wordList))
# output :[["red","ted","tex","tax"],["red","rex","tex","tax"],["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
# expected : [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]

beginWord ="cet"
endWord = "ism"
wordList = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
print(S.findLadders(beginWord, endWord, wordList))