#Q1
class Animals():
    def animal_attributes(self):
        print("Tiger")


class Tiger(Animals):
    def king(self):
        print("King Of Jungle")


k=Tiger()
k.animal_attributes()
k.king()

#Q2
#A B
#A B

#Q4
class Shape():
    def __init__(self, l, b):
        self.length=l
        self.breadth=b
    def area(self,):
        area=self.length*self.breadth
        print("shape:",area)
class Rectangle(Shape):
    def area(self):
        area=self.length*self.breadth
        print("rectangle:",area)
class Square(Shape):
    def area(self):
        area=self.length*self.breadth
        print("square:",area)

x=Rectangle(4,5)
y=Square(2,2)
x.area()
y.area()

#Q3
class Cop:
    def __init__(self,name,age,work__experience,designation):
        self.name=name
        self.age=age
        self.work__experience=work__experience
        self.designation=designation
    def display(self):
        print("before update")
        print("Name=",self.name)
        print("Age=",self.age)
        print("Work experience=",self.work__experience)
        print("Designation=",self.designation)
    def __update__(self,name,age,work__experience,designation):
        self.name = name
        self.age = age
        self.work__experience = work__experience
        self.designation = dessignation
class Mission(Cop):
    def add_mission_detail(self,name,age,work__experience,designation):
        print("updated cop details are")
        print("Name=", end="")
        self.name = name
        print(name)
        print("Age=", end="")
        self.age = age
        print(age)
        print("Work Experience=", end="")
        self.work__experience = work__experience
        print(work__experience)
        print("Designation=", end="")
        self.designation = designation
        print(designation)

x=Mission("Aman",20,7,"DSP")
name=input("Enter Name")
age=int(input("Enter Age"))
work__experience=(input("Enter Work Experience"))
designation=input("Designation")
x.display()


y=Mission(name,age,work__experience,designation)
y.add_mission_detail(name,age,work__experience,designation)
