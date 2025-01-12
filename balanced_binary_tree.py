# -*- coding: utf-8 -*-
"""Balanced_Binary_Tree.ipynb
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        def height(node):
          if not node:
            return 0
          left_height = height(node.left)
          if left_height == -2 :
            return -2
          right_height = height(node.right)
          if right_height == -2:
            return -2
          if abs(left_height - right_height) > 1:
            return -2
          return max(left_height, right_height) + 1
        return height(root) != -2