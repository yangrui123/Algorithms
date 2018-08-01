#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

"从头到尾打印链表"
"输入一个链表的头节点，从尾到头反过来打印出每个节点的值"

from ListNode import Node


# 不修改链表的结构,栈实现
def print_list_reversingly(head):
    if not head:
        print('list is null.')
    lst = []
    node = head
    while node:
        lst.append(node.val)
        node = node.next

    while lst:
        print(lst.pop())


# 修改链表的结构
def print_list_reversingly_2(head):
    if not head:
        print('list is null.')
    last = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = last
        last = cur
        cur = temp
    while last:
        print(last.val)
        last = last.next

node = Node()
nums = [1,2,3,4,5,6,7,8,9]
head = node.creat_listnode(nums)
print_list_reversingly(head)
# print_list_reversingly_2(head)


