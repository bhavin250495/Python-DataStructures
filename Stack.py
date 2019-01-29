class Stack :

    stackDS = []
    head = 0

    def __init__(self,startStack):
        self.stackDS.append(startStack)


    def printTop(self):
        print(self.stackDS[self.head])



    def push(self,data):
        self.stackDS.append(data)

    def pop(self):
        self.head +=1
        return self.stackDS[self.head]



s = Stack(12)
s.push(10)
s.push(90)
s.printTop()
s.pop()
s.printTop()