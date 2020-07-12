#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left_tree = self.lowestCommonAncestor(root.left,p,q)
        right_tree = self.lowestCommonAncestor(root.right,p,q)
        if left_tree and right_tree:
            return root
        #当p为q的祖先节点时，搜索一侧子树只能返回p，这时候搜另一边是搜不到q的，但节点又一定在树中，所以一定是p是q的祖先的情况，直接返回p即为答案
        if left_tree:
            return left_tree
        else:
            return right_tree
    
        
# @lc code=end

