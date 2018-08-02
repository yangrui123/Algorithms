#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'

"两个栈实现队列"
"用两个栈实现一个队列，队列的声明如下，请实现它的两个函数appendTail 和 deleteHead， " \
"分别完成在队列尾部插入节点和删除节点的功能"

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, value):
        self.stack1.append(value)
        return self.stack2[::-1]+self.stack1

    def delete_head(self):
        if self.stack2:
            self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.stack2.pop()
        return self.stack2[::-1]+self.stack1


queue = Queue()
queue.append_tail(1)
queue.append_tail(2)
queue.append_tail(3)
queue.delete_head()
res = queue.append_tail(4)
res = queue.delete_head()
print(res)


