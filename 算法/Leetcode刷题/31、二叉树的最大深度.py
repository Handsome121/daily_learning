"""
给定一个二叉树，找出其最大深度
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        nodes = []
        level = 0
        if not root:
            return level
        nodes.append(root)
        while nodes:
            level += 1
            templennodes = []
            for node in nodes:
                if node.left:
                    templennodes.append(node.left)
                if node.right:
                    templennodes.append(node.right)
            nodes = templennodes
        return level
