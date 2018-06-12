Q1:
i=0
l=[]
while(i<10):
    user=int(input("Enter The Number"))
    l.append(user)
    i=i+1
for i in l:
    print(i)

Q2:

while(True):
    print("infinte")



Q3:
user=[]
user_sqr=[]
for a in range (0,5):
    num=int(input("Enter You Number"))
    user.append(num)
print(user)
for num in user:
    b=num*num
    user_sqr.append(b)
print(user_sqr)

#q4
i=0
l=[5,6,"Hello",3.1]
a=[]
b=[]
c=[]
for i in l:

    if (type(i)==int):
        a.append(i)
    elif (type(i)==str):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)

Q5:
even=[]
odd=[]
for i in range (1,101):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

Q6:
star=4
for i in range(0,star):
    for i in range(0,i+1):
        print("*",end="")
    print("\r")

Q7:
d={'Name':'Aman','Age':20}
for i in d:
    print(d[i])

Q8:
i=0
c=[]
while(i<5):
    a=int(input("enter number"))
    c.append(a)
    i=i+1
a=int(input("remove the number "))
for i in c:
         if(a==i):
             c.remove(i)
print(c)
