#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Node:
    def __init__(self):
        pass

    def creat_listnode(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        node = head
        for val in values[1:]:
            node.next = ListNode(val)
            node = node.next
        return head

    def print_listnode(self):
        pass