# -*- coding: utf-8 -*-
"""Implement Stack using Queues.ipynb
Implement Stack using Queues
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""

class MyStack(object):

    def __init__(self):
        self.stack= []

    def push(self, x):
        self.stack.append(x)
        return self.stack

    def pop(self):
        if len(self.stack)>0:
           return self.stack.pop()
        else:
           return None

    def top(self):
       if len(self.stack)>0:
          return self.stack[-1]
       else:
           return None

    def empty(self):
       if len(self.stack)==0:
           return True
       else:
           return False