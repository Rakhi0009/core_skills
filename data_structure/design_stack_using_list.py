class Stack:
    
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
        
