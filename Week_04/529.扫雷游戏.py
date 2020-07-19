#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = [1,-1,0]
        row,column = len(board),len(board[0])
        i,j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        self.helper(board,i,j,direction)
        return board

    def helper(self,board,i,j,direction):
        row,column = len(board),len(board[0])
        count = 0
        for d in direction:
            for L in direction:
                if d == 0 and L == 0:
                    continue
                if 0 <=i+d < row and 0 <=j+L< column and board[i+d][j+L] == 'M':
                    count += 1
        if count > 0:
            board[i][j] = str(count)
            return
        board[i][j] = 'B'
        for d in direction:
            for L in direction:
                if d == 0 and L == 0:
                    continue
                new_i,new_j= i+d,j+L
                if 0 <=new_i< row and 0 <=new_j< column and board[new_i][new_j] == 'E':
                    self.helper(board,new_i,new_j,direction)
        
        
                    


    
        
# @lc code=end

