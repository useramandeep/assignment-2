#Q1
import threading
import time
class mythread(threading.Thread):
    def __init__(self, i):
        self.h=i
        threading.Thread.__init__(self)


    def start(self):
        time.sleep(5)
        print("Hey This Is Aman",self)

t=mythread(1)
t.start()

#Q2
import threading
import time
class T(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i+1
        time.sleep(1)
    def run(self):
        print(self.h)
for i in range(10):
    thread1=T(i)
    thread1.run()

#Q3
import threading
import time
sec=[2,4,6,8,10]
class T(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i

    def run (self,counter):
        time.sleep(counter)
        print(self.h)

for i in sec:
    thread1=T(i)
    thread1.run(i)

#Q4
import threading
import math
class T(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        a=self.h
        b=math.factorial(a)
        print("Factorial is =",b)
user=int(input("Enter Number To Get Factorial"))
thread=T(user)
thread.start()