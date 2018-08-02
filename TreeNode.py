#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None
        self.parent = None


class Tree:
    def __init__(self):
        pass

    # def creat_treenode(self, values):
    #     if not values:
    #         return None
    #     root = TreeNode(values[0])
    #     queque = [root]
    #     i = 1
    #     for j in range(1, len(values), 2):
    #         node = queque[i]
    #         if not node:
    #             i += 1
    #             continue
    #         p = (i - 1) // 2
    #         if p != 0:
    #             node.parent = queque[p]
    #         i += 1
    #         left = None
    #         right = None
    #         if values[j]:
    #             left = TreeNode(values[j])
    #             node.left = left
    #         if values[j+1]:
    #             right = TreeNode(values[j+1])
    #             node.right = right
    #         queque.append(left)
    #         queque.append(right)
    #     return root
    def creat_treenode(self, values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if values[i]:
                left = TreeNode(values[i])
                left.parent = node
                node.left = left
                queue.append(left)
            if values[i+1]:
                right = TreeNode(values[i+1])
                right.parent = node
                node.right = right
                queue.append(right)
            i += 2
        return root


    def print_treenode_level_traversal(self, root):
        queue = [root]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)