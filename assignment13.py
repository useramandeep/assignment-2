#Q.1

'''
class handle(Exception):
   pass
try:
    a=3
    if(a<4):
        a=a/(a-3)
        raise handle
except ZeroDivisionError:
    print("zero division error")

#it is zero division error

'''
#Q.2
#l=[1,2,3]
#print(l[3])

class Deep(Exception):
    pass
try:
    import Deep
    l=[1,2,3]
    print(l[3])
except Exception:
    print("enter correct index value")


#Q.3 -
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print
    "An exception"
    raise  # To determine whether the exception was raised or not

#output- #Raise Error



#Q.4-

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output= -5.0
#        a/b result in 0


#Q.5-
#1. Import Error
try:
    import deep
except ImportError:
    print("enter a valid import file")

#2. Value Error

try:
    a = int(input("enter no"))
    print(a)
except(ValueError):
    print("Value Error")


#3.
try:
    l=[1,2,3]
    print(l[5])
except IndexError:
    print("index error")


#Q.6-
class AgeError(Exception):
    pass
a=True
while(a):
    try:
        age=int(input("enter age"))
        if(age>=18):
            a=False
            raise AgeError
        else:
            print(age)
    except AgeError:
        print("age is greater than 18")
    except ValueError:
        print("only int allowed")
