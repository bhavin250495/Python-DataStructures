
 

class Node :
    data = None;
    next = None;

    def __init__(self,data:None,next:None):
        
        self.data = data
        self.next = next

class LinkedList:
    head = None
    # Utility function to print the linked list 
    def printList(self): 
        temp = self.head 
        while (temp): 
            print(temp.data) 
            temp = temp.next

    def append(self,data):

        new_node = Node(data,None)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while(last.next != None):
            last = last.next

        last.next = new_node

    def reverse(self):

        temp = self.head

        while temp == None:

            next = temp.next
            prev = temp
            next.next = prev
            self.head = temp

            temp = temp.next

    def printAll(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
            

    def printHead(self):
        print(self.head.data)


    def insert(self,a):
        if self.head == None:
            self.head = Node(a,None)
        else:
           newNode = Node(a,self.head)
           self.head = newNode
                 

                  
                     
                
                     

            
   


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.printList()





   
   
    

 



