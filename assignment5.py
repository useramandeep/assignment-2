#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input("Enter The Year"))
if (year%4==0):
    print("Leap Year")
else:
    print("Not Leap Year")

 #Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.

l=int(input("Enter Length"))
b=int(input("Enter Breadth"))
if (l==b):
    print("Square")
else:
    print("Rectangle")

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.

a=int(input("Enter The Age Of First Person"))
b=int(input("Enter The Age Of Second Person"))
c=int(input("Enter The Age Of Third Person"))
#for oldest
if (a>b and a>c):
    print("%d First Person Is oldest"%(a))
elif (b>c and b>a):
    print("%d 2nd Person Is oldest"%(b))
elif (c>a and c>b):
    print("%d 3rd Person is oldest"%(c))

#for Youngest
if (a<b and a<c):
    print("%d First Person Is Youngest" % (a))
elif (b<c and b<a):
    print("%d 2nd Person Is Youngest" % (b))
elif (c<a and c<b):
    print("%d 3rd Person is Youngest" % (c))

else:
    print("All Are Same Age")
#Q.4
point=int(input("Enter The Number Upto 200"))
if (point>=1 and point<=50):
    print("No Prize")
elif (point>=51 and point<=150):
    print("Congratulations! You won a Wooden Dog!")
elif (point>=151 and point<=180):
    print("Congratulations! You won a Book")
elif (point>=181 and point<=200):
    print("Congratulations! You won a Chocolates")


#Q5
q=int(input("Enter The Quantity"))
price=q*100
if (price>1000):
    print(price-0.10*price)
else:
    print("Total Amout",price)