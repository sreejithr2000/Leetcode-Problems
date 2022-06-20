class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        self.stack.pop()
    
    def top(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    
    def getLength(self):
        return len(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
s.push(40)
s.push(50)
s.pop()
s.push(60)
s.pop()

print(s.stack)
print(s.top())
print(s.getLength())

    