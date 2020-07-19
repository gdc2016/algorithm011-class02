#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from collections import deque,defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                string = word[:i] + '*' + word[i+1:]
                dic[string].append(word)

        queue = deque([(beginWord,1)])
        visited = {beginWord:True}
        while queue:
            node,count = queue.popleft()
            for i in range(len(node)):
                current = node[:i] + '*' + node[i+1:]
                for word in dic[current]:
                    if word == endWord:
                        return count+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word,count+1))
                dic[current] = []
        return 0


# @lc code=end

