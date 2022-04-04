class FixedMultiStack():
    
    def __init__(self, stackCapcity: int) -> None:
        self.numberOfStacks = 3
        self.stackCapcity = stackCapcity
        self.values = [0] * (self.stackCapcity * self.numberOfStacks)
        self.sizes = [0] * self.numberOfStacks
    
    def push(self, stackNum: int, value: int) -> None:
        if self.isFull(stackNum):
            print(f'Stack {stackNum} is full')
            return
        
        #increment size of the respective stack
        self.sizes[stackNum] += 1
        #place new value at the top of that stack
        self.values[self.indexOfTop] = value
    
    def pop(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            print(f'Stack {stackNum} is empty')
            return
        
        #get the index of the top element
        indexOfTop = self.indexOfTop(stackNum)

        #get the value to later returned
        value = self.values[indexOfTop]
        
        #reset that index to 0
        self.values[indexOfTop] = 0

        #decrease the stack size
        self.sizes[stackNum] -= 1

        return value

    def peek(self, stackNum: int) -> int:
        if self.isEmpty(stackNum):
            print(f'Stack {stackNum} is empty')
            return
        
        value = self.values[self.indexOfTop(stackNum)]
        return value
    
    def isEmpty(self, stackNum: int) -> bool:
        if self.sizes[stackNum] == 0: 
            return True
        return False
    
    def isFull(self, stackNum: int) -> bool:
        if self.sizes[stackNum] == self.stackCapacity: 
            return True
        return False
    
    def indexOfTop(self, stackNum) -> int:
        offset = self.stackCapcity * stackNum
        size = self.sizes[stackNum]
        return offset + size - 1