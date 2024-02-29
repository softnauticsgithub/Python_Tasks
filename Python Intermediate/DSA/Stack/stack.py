"""

Stack: A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (
FILO) manner. In stack, a new element is added at one end and an element is removed from that end only. The insert
and delete operations are often called push and pop.

Functions associated with stack:

- empty() – Returns whether the stack is empty – Time Complexity: O(1)
- size() – Returns the size of the stack – Time Complexity: O(1)
- top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
- push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
- pop() – Deletes the topmost element of the stack – Time Complexity: O(1)


"""

# Initializing a Stack
stack = list()

# Using append() function to push data into stack

stack.append("a")
stack.append("b")
stack.append("c")

print(f"Initial Stack: {stack}")

"""
Stack using collection.deque for faster operations over list
Preferred method

"""

from collections import deque

stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")

print(f"Initial Stack: {stack}")

# Popping element out of stack
print(stack.pop())

print(f"Stack after Popping top element: {stack}")

"""
Implementation using Queue Module

Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function
and get() takes data out from the Queue.

There are various functions available in this module:

maxsize – Number of items allowed in the queue.
empty() – Return True if the queue is empty, False otherwise.
full()  – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default),
then full() never returns True.
get() – Remove and return an item from the queue. If the queue is empty, wait until
an item is available.
get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available,
raise QueueFull.
qsize() – Return the number of items in the queue.

"""

from queue import LifoQueue

# Init stack

stack_q = LifoQueue(maxsize=3)

print(f"Qsize: {stack_q.qsize()}")

# Put elements in stack
stack_q.put('a')
stack_q.put('b')
stack_q.put('c')

print(f"Is Stack Full: {stack_q.full()}")
print(f"Qsize: {stack_q.qsize()}")

# Using get() to pop elements from stack

print(f"Element popped from stack: {stack_q.get()}")
print(f"Element popped from stack: {stack_q.get()}")
print(f"Element popped from stack: {stack_q.get()}")
print(f"Is Stack Empty: {stack_q.empty()}")

"""
Implementation of Stack using singly Linked List

The linked list has two methods addHead(item) and removeHead() that run in constant time. These two methods are 
suitable to implement a stack.

getSize()– Get the number of items in the stack.
isEmpty() – Return True if the stack is empty, False otherwise.
peek() – Return the top item in the stack. If the stack is empty, raise an exception.
push(value) – Push a value into the head of the stack.
pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.

"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    """
    Class to create stack
    """

    def __init__(self):
        self.head = Node("head")
        self.size = 0

    def __str__(self):
        current = self.head.next
        out = ""
        while current:
            out += str(current.value) + "->"
            current = current.next
        return out[:-2]

    def getsize(self) -> int:
        """
        Get size of stack
        :return :size
        """
        return self.size

    def isEmpty(self) -> bool:
        """
        To check if stack is empty
        :return boolean:
        """
        return self.size == 0

    def peek(self) -> any:
        """
        getting top item from stack
        :return:
        """
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value

    def push(self, value) -> None:
        """
        Pushing value to stack
        :param value : Value to be pushed
        :return:
        """
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self) -> any:
        """
        Popping value from stack
        :return: removed value
        """
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value


if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Popped Item: {remove}")
    print(f"Stack after Popping: {stack}")
