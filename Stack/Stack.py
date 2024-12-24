'''
Stack implementation
'''
from typing import Any

class Stack:
    def __init__(self) -> None:
        self.stack: list = []
    
    def isEmpty(self) -> bool:
        '''
        To check if the stack is empty
        '''
        return len(self.stack) == 0

    def push(self, element: Any) -> None:
        '''
        To push an element into the stack
        '''
        self.stack.append(element)

    def peek(self) -> Any:
        '''
        Returns the last value in stack
        '''
        return self.stack[-1]
    
    def size(self) -> int:
        '''
        Returns the number of elements in the stack
        '''
        return len(self.stack)
    
    def pop(self) -> Any:
        '''
        Removes the last item added to the list
        '''
        return self.stack.pop()

""" s = Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
s.push(8.4)
s.pop()
s.pop()
print(s.size()) """