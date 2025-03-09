class Students:

    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    
    def showdata(self):
        print(self.name)
        print(self.roll)

    def showmarks(self):
        print(self.marks)


name = input("Enter the name of the student : ")
roll = int(input("Enter roll : "))
marks = list(map(int, (input("Enter the marks seperated by space : ").split())))

ob=Students(name, roll, marks)
ob.showdata()
ob.showmarks()
