# class Name:
#     def greet(self,name):
#         print(f"hello{name}") 
class Student:
    # name=""
    # rollno=0
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
        pass
    def display(self):
        print(f"name is {self.name} and has{self.rollno}")
        print(f"name is {self.name} and has {self.rollno}")
stu1=Student("swetha",26)
stu2=Student("lucky",20)
print(stu1.name)
print(stu1.rollno)
stu1.display()
stu2.display()