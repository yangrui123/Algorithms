#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

"二叉树的下一个节点"
"给定一棵二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？树中的节点除了有两个分别指向左、右子节点的指针，" \
"还有一个指向父节点的指针"

from TreeNode import TreeNode, Tree


def get_next(node):
    if not node.right:
        if node.parent.left == node:
            return node.parent
        temp = node.parent
        last = node
        while temp.parent:
            temp = temp.parent
            last = last.parent
        if temp.left == last:
            return temp
        return None
    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node


tree = Tree()
root = tree.creat_treenode(['a','b','c','d','e','f','g',None, None,'h','i'])
# tree.print_treenode_level_traversal(root)
node = get_next(root.right.right)
print(node)
if node:
    print(node.val)

