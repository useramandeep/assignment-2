l=[]                               #Q.1- Create a list with user defined inputs.
a=input("Enter Number")            #OutPut: Enter Number 2
l.append(a)                         # ['2']
print(l)

b=input("Enter The String")        #Q.2- Add the following list to above created list:
l.append(b)                        #Output: ['2', 'hello']
print(l)

emotions=["love","hate","happy","single","happy","sad","happy","single"] #Q.3- Count the number of time an object occurs in a list.
print(emotions.count("happy"))                                                 #output:3

a=[1,4,2,5,6]     #Q.4- create a list with numbers and sort it in ascending order.
b=[6,4,2,8,9]      #output: [1, 2, 4, 5, 6]
a.sort()
print(a)
b.sort()        #Q.5- Given are two one-dimensional---------in ascending order. [List]
l=(a+b)         #outout [1, 2, 2, 4, 4, 5, 6, 6, 8, 9]
l.sort()
print(l)

l=[1,2,3,4,5]    #Q.6-Implement a stack and queue using lists.
(l.append(6))    #output: [1, 2, 3, 4, 5, 6] insertion 6
print(l)                  #[1, 2, 4, 5, 6]    deletion 3
l.pop(2)
print(l)
