
#Q1
f=open("file.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number "))
for i in range(0,n):
    print(a[i])
f.close()

#Q2
a="movies"
f=open("file2.txt","r")
k=f.read()
m=k.split()
print(k.count(a))

#Q3

f=open("file.txt",encoding="utf8")
a=(f.readlines())
c=open("file7.txt","w")
c.writelines(a)

#Q4

i=0
f=open("file4.txt",encoding="utf8")
a=(f.readlines())
b=open("file5.txt",encoding="utf8")
c=(b.readlines())
d= open("file6.txt","w")
for i,j in zip(a,c):
    d.write(i+j)
f.close()
b.close()
d.close()

#Q5


l=[]
global str
j=[]
import json
import random
for i in range(0,10):
    l.append(random.randint(1,10))
f=open("file8.txt","w")
for t in l:
    h="".join(str(t))
    f.write(h)
f.close()
d=open("file8.txt","r")
a=d.read()
for x in a:
    if(x.isdigit()):
        m="".join(x)
        j.append(m)
j.sort()
c=open("file9.txt","w")

c.write(str(j))


