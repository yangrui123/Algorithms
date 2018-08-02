#!/usr/bin/env python
# coding:utf-8
__author__ = 'yangrui'


"两个队列实现一个栈"

class Stack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, value):
        if self.queue2:
            self.queue2.append(value)
        else:
            self.queue1.append(value)
        queue = self.queue1 + self.queue2
        print(queue)
        return

    def pop(self):
        if self.queue1:
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.pop(0))
            self.queue1.pop()
            queue = self.queue2
        else:
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.pop(0))
            self.queue2.pop()
            queue = self.queue1
        print(queue)
        return queue


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.pop()
stack.push(4)