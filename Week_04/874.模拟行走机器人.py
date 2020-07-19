#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dic = {'up':[0,1,'left','right'],
                'down':[0,-1,'right','left'],
                'left':[-1,0,'down','up'],
                'right':[1,0,'up','down']}
        current = 'up'
        path = [0,0]
        obst = {tuple(obj) for obj in obstacles}
        res = 0
        for route in commands:
            if route > 0:
                for _ in range(route):
                    if (path[0]+dic[current][0],path[1]+dic[current][1]) not in obst:
                        path[0] += dic[current][0]
                        path[1] += dic[current][1]
                        res = max(res,path[0]*path[0] + path[1]*path[1])
                    else:
                        break
            elif route == -1:
                current = dic[current][3]
            else:
                current = dic[current][2]
        return res

        
# @lc code=end

