# imports
from collections import deque

# MyStack
class MyStack:
    # Create
    def __init__(self, type):
        self.stack = []
        self.stackType = type
    # Add
    def push(self, elem):
        if type(elem) is self.stackType:
            self.stack.append(elem)
        else:
            raise Exception("The type of the new element is not the same as the type of the stack")
    
    # Remove
    def pop(self):
        if self.empty():
            raise Exception("Stack is empty. Cannot delete elements from an empty stack")
        else:
            return self.stack.pop()
    
    # Top
    def top(self):
        if self.empty():
            raise Exception("No elements in the stack")
        else:
            return self.stack[-1]
    
    # Empty
    def empty(self):
        return len(self.stack) == 0

# MyQueue
class MyQueue:
    # Create
    def __init__(self, type):
        self.queue = deque()
        self.queueType = type
    def enqueue(self, elem):
        if type(elem) is self.queueType:
            self.queue.append(elem)
        else:
            raise Exception("Element of the element is not the same as the element of the queue")
    def front(self):
        if self.empty():
            raise Exception("Cannot return elements from an empty queue")
        else:
            return self.queue[0]
    def empty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if self.empty():
            raise Exception("Cannot delete elements from an empty queue")
        else:
            return self.queue.popleft()

# Testing code for stack
s = MyStack(int)
print(s.empty())
s.push(5)
s.push(8)
print(s.pop())
s.push(3)
print(s.empty())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop()) # should generate an error
# Testing code for Queue
q = MyQueue(int)
print(q.empty())
q.enqueue(5)
q.enqueue(8)
print(q.dequeue())
q.enqueue(3)
print(q.empty())
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue()) # should generate an error