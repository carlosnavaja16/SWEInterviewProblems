class QueueNode():

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue():

    def __init__(self):
        self.first = None
        self.last = None
    
    def add(self, value):

        newNode = QueueNode(value)

        if self.last:
            self.last.next = newNode
            self.last = newNode
        else:
            self.last = newNode
        
        if not self.first:
            self.first = newNode
    
    def remove(self):

        if not self.first:
            raise Exception("Queue empty!")
        else:
            value = self.first.value
            self.first = self.first.next

            if self.first == None:
                self.last = None
            return value
    
    def peek(self):
        return self.first.value
    
    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False