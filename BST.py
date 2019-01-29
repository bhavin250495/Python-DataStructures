class Node:

    data = None
    right = None
    left = None

    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def minValue(self):
        if self.left:
            return self.left.minValue()
        else:
            return self.data    
    
    def maxValue(self):
        if self.right:
            return self.right.maxValue()
        else:
            return self.data 
    
    def isLeaf(self):
        if (self.right is None) and (self.left is None):
            return True
        return False


    def delete(self,val):

        if val < self.data:
           self.left =  self.left.delete(val)
           return self

        elif val > self.data:
            self.right =  self.right.delete(val)

        elif self.data == val:

            #Remove if is leaf
            if self.left is None and self.right is None :
                return None

            #Remove with one child   
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
                 
            else:
                minVal = self.right.minValue() 
                self.delete(minVal)
                print(minVal)  
                self.data = minVal

        return self
       

    def findVal(self,val):
        if self.data == val:
            print('Found',val)
            return self
        elif self.data < val and self.right:
            return self.right.findVal(val)
        elif self.data > val and self.left:
            return self.left.findVal(val)
        else:
             return None          
 
    def insert(self,data):

        if self.data:
            
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data) 
            else:
                 self.data = data

 #Traversal
    def printInorderTree(self):

        if self.left:
            
            self.left.printInorderTree()   
        print(self.data)  
        if self.right:
            
            self.right.printInorderTree()

    def printPostOrderTree(self):

        if self.left:
            self.left.printPostOrderTree()
        if self.right:
            self.right.printPostOrderTree()
        print(self.data)    

    def printPreOrderTree(self):
        print(self.data)
        if self.left:
            self.left.printPreOrderTree()
        if self.right:
            self.right.printPreOrderTree()    


root = Node(8)
root.insert(10)
root.insert(14)
root.insert(13)
root.insert(5)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)

root.printPreOrderTree()   

