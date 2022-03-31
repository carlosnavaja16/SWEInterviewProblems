class StackNode():

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Stack():
    def __init__(self) -> None:
        self.top = None
    
    def pop(self):
        if not self.top: 
            raise Exception("Empty stack!")
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        if not self.top: 
            raise Exception("Empty stack!")
        return self.top.value
    
    def push(self, value):
        newNode = StackNode(value)
        newNode.next = self.top
        self.top = newNode
    
    def isEmpty(self):
        if self.top == None: return True
        else: return False