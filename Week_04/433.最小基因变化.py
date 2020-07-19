#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not bank:
            return -1
        if not start or not end:
            return -1
        bank = set(bank)
        dic = {'A':'CGT','C':'AGT','G':'ACT','T':'ACG'}
        steps = []
        self.helper(0,start,end,bank,dic,steps)
        return min(steps) if steps else -1

    def helper(self,step,current,end,bank,dic,steps):
        if current == end:
            steps.append(step)
        if not bank:
            return 
        for i,s in enumerate(current):
            for c in dic[s]:
                new = current[:i] + c + current[i+1:]
                if new in bank:
                    bank.remove(new)
                    self.helper(step+1,new,end,bank,dic,steps)
                    bank.add(new)
        





        
# @lc code=end

