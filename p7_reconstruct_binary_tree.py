#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

"重建二叉树"
"输入某二叉树的前序遍历序列和中序遍历序列的结果，请重建该二叉树"

from TreeNode import TreeNode, Tree


def reconstruct_binarytree(preorder, inorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    idx = inorder.index(preorder[0])
    left = reconstruct_binarytree(preorder[1:idx+1], inorder[:idx])
    right = reconstruct_binarytree(preorder[idx+1:], inorder[idx+1:])
    root.left = left
    root.right = right
    return root


preorder = [1,2,4,7,3,5,6,8]
inorder = [4,7,2,1,5,3,8,6]
root = reconstruct_binarytree(preorder, inorder)
tree = Tree()
tree.print_treenode_level_traversal(root)


