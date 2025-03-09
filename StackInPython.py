class StackInPython:
    def __init__(self, size):
        self.l=[]
        self.size=size
        self.top=-1
    def Push(self,e):
        if self.top==self.size-1:
            print("stack is overflow")
        else:
            self.top+=1
            self.l.append(e)
    def Pop(self):
        if self.top==-1:
            print("stack is underflow")
        else:
            self.top-=1
            self.l.pop()
    def Traverse(self):
        for i in range(self.top+1):
            print(self.l[i])

ob=StackInPython(4)
ob.Push(2)
ob.Push(4)
ob.Pop()
ob.Traverse()
