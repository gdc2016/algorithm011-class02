#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res,queue = [],deque([root])
        while queue:
            p = queue.popleft()
            if p:
                res.append(str(p.val))
                queue.append(p.left)
                queue.append(p.right)
            else:
                res.append("null")
        return ','.join(res)  

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(',')
        if lst[0] == "null":
            return
        root = TreeNode(int(lst[0]))
        queue = deque([root])
        i = 0
        while queue:
            node = queue.popleft()
            i += 1
            if lst[i] != "null":
                node.left = TreeNode(int(lst[i]))
                queue.append(node.left)
            i += 1
            if lst[i] != "null":
                node.right = TreeNode(int(lst[i]))
                queue.append(node.right)
        return root

        

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

