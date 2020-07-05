#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stack,res = [root],[]
        if not root:
            return res
        while stack:
            p = stack.pop()
            res.append(p.val)
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return res[::-1]

        
# @lc code=end

