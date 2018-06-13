#Q1
x=int(input("Enter The Radius Of Circle"))
def area(x):
    area=3.14*x*x
    return area
print(area(x))

#Q2:
i=0
num=int(input("enter the range"))
def perfect(num):
    add=0
    for i in range(1, num):
        if (num%i==0):
            add=add+i
    if (add==num):
        print("This is a prefect number")
    else:
        print("This is not a prefect number")
print(perfect(num))

#Q3
def num_table(n, table=1):
    if table==11:
        return
    print(str(n)+"x"+str(table)+"="+str(n*table))
    num_table(n,table+1)
num_table(12)

#Q4
user_a=int(input("Enter the number"))
user_b=int(input("Enter the other number"))
def power(user_a,user_b):
    if(user_b==1):
        return user_a
    else:
        return (user_a*power(user_a,user_b-1))
print(power(user_b,user_a))

#Q5:
number=int(input("Enter The Number To Factorial"))
def f(number):
    if number==0:
        return 1
    s=number*f(number-1)
    return s
a=f(number)
d={number:a}
print(d)
