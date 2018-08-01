#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        pass

    def creat_treenode(self):
        pass

    def print_treenode_level_traversal(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)