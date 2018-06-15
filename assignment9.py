#Q1
class Circle():
    def __init__(self,r):
        self.radius=r

    def getArea(self):
        return self.radius**2*3.14

    def getCircumference (self):
        return 2*self.radius*3.14
x=Circle(4)
print("Area of circle:",x.getArea())
print("Circumference of circle:",x.getCircumference())

#2
class Student():
    def __init__ (self,name,rolln):
        self.n=name
        self.r=rolln
x=Student('Aman', 8)
print("Name Is:", x.n)
print("Roll Number Is:", x.r)

#Q3
class Temprature():
    def __init__(self,celsius_temp):
        self.c=celsius_temp
    def fahrenheit(self):
        return 9/5*self.c+32
    def celsius(self):
        return self.c
x=Temprature(37.5)
print("degree Fahrenheit", x.fahrenheit())
print("ss",x.celsius())



#Q5
class Expenditure():
    def __init__(self,expenditure,total_saving,total_salary=0):
        self.exp=expenditure
        self.s=total_saving
        self.t=0
    def display(self):
        print("total Expenditure:",self.exp)
        print("total saving:",self.s)
    def total_salary(self):
        self.t=self.exp+self.s
    def display_salary(self):
        return self.t
user_input=int(input("enter the expenditure"))
user_input1=int(input("enter saving"))
x=Expenditure(user_input,user_input1)
x.display()
x.total_salary()
print("total salary:",x.display_salary())