class Node:
    
    def __init__(self, x: int):
        self.value: int = x
        self.left: Node = None
        self.right: Node = None
            
    def insert(self, incomingNode): 
        if incomingNode.value >= self.value:
            if self.right == None:
                self.right = incomingNode
            else:
                self.right.insert(incomingNode)
        elif incomingNode.value < self.value:
            if self.left == None:
                self.left = incomingNode
            else:
                self.left.insert(incomingNode)
    def toList(self):
        treeList = []
        if self.left != None:
            treeList = treeList + self.left.toList()
        treeList.append(self.value)
        if self.right != None:
            treeList = treeList + self.right.toList()
        return treeList
    
class Tree: 
    
    def __init__(self):
        self.root = None
        
    def add(self, incomingInt: int):
        incomingNode = Node(incomingInt)
        if self.root == None:
            self.root = incomingNode
        else:
            self.root.insert(incomingNode)
    
    def toList(self):
        treeList = []
        if self.root == None:
            return treeList
        else:
            treeList = treeList + self.root.toList()
            return treeList
        

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        t = Tree()
        for n in nums1:
            t.add(n)    
        for n in nums2:
            t.add(n)
        
        combinedList = t.toList()        
        combinedLen = len(combinedList)
        halfCombinedLen = int(len(combinedList)/2)
        
        if combinedLen%2 == 0:
            median = (combinedList[halfCombinedLen] + combinedList[halfCombinedLen-1])/2
            return median
        else: 
            median = combinedList[halfCombinedLen]
            return median
