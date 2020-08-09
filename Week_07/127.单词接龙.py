#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from collections import deque,defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue,res = deque([(1,beginWord)]),[]
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        dic = defaultdict(list)
        visited = {beginWord:True}
        for word in wordList:
            for i in range(len(word)):
                string = word[:i] + '*' + word[i+1:]
                dic[string].append(word)
        while queue:
            step,word = queue.popleft()
            for i in range(len(word)):
                new_string = word[:i] + '*' + word[i+1:]
                for s in dic[new_string]:
                    if s == endWord:
                        return step+1
                    if word not in visited:
                        visited[word] = True
                    queue.append((step+1,s))
                dic[new_string] = []
        return 0


# @lc code=end

