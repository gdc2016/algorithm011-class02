#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        dic = {'A':'CGT','C':'AGT','G':'ACT','T':'ACG'}
        queue = deque([(0,start)])
        while queue:
            step,word = queue.popleft()
            if word == end:
                return step
            for i,n in enumerate(word):
                for s in dic[n]:
                    string = word[:i] + s + word[i+1:]
                    if string in bank:
                        queue.append((step+1,string))
                        bank.remove(string)
        return -1



    
        





        
# @lc code=end

