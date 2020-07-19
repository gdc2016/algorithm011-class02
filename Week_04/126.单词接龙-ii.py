#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from collections import defaultdict,deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        res,dic = [],defaultdict(list)
        queue1,queue2 = deque([(beginWord,[beginWord])]),deque()
        visited = set()
        for word in wordList:
            for i in range(len(word)):
                string = word[:i] + '*' + word[i+1:]
                dic[string].append(word)
        while queue1:
            while queue1:
                word,path = queue1.popleft()
                if word == endWord:
                    res.append(path)
                visited.add(word)
                for i in range(len(word)):
                    string = word[:i] + '*' + word[i+1:]
                    for w in dic[string]:
                        if w not in visited:
                            queue2.append((w,path+[w]))
            if res:
                return res
            queue1,queue2 = queue2,queue1
        return []



# @lc code=end

