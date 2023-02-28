#10 Write a python script to check whether a given number 
# is prime or armstrong number using 2 different threads.
from threading import *
from time import sleep
class T1(Thread):
    def run(self):
        while 1:
            n=int(input("T1-Enter a number: "))
            print("Even number" if n%2==0 else "Odd number")
            sleep(1)
class T2(Thread):
    def run(self):
        while 1:
            n=int(input("T2-Enter a number: "))
            print("Even number" if n%2==0 else "Odd number")
            sleep(1)
t1=T1()
t2=T2()
t1.start()
t2.start()

"""
#9 Write a python script to join 2 threads after printing 
# completing the first Question.
#8 Write a python script to change the name of the Thread.
from threading import *
from time import sleep
class T1(Thread):
    def run(self):
        sleep(1)
t1=T1()
t1.start()
print(t1.name)
t1.name="Navin Reddy"
print(t1.name)
t1.join()
print(t1.is_alive())


#7 Write a python script to create a clock where 1st thread will 
# print the current time every second and 2nd will print “1 Minute Completed” 
# after every 1 minute.
from threading import *
from time import sleep
class T1(Thread):
    def run(self):
        second=0
        while 1:
            print(second," Seconds")
            second+=1
            if second==60:
                second=0
            sleep(1)
class T2(Thread):
    def run(self):
        second=0
        while 1:
            second+=1
            if second==60:
                second=0
                print("1 minute completed")
            sleep(1)
t1=T1()
t2=T2()
t1.start()
t2.start()

#6 Write a python script to create 5 threads to fill a list with random numbers till 100.
from secrets import randbelow
from threading import *
from time import sleep
l1=[]
class T1(Thread):
    def run(self):
        while 1:
            l1.append(randbelow(100))
            print(l1)
            sleep(1)
class T2(Thread):
    def run(self):
        while 1:
            l1.append(randbelow(100))
            print(l1)
            sleep(1)
class T3(Thread):
    def run(self):
        while 1:
            l1.append(randbelow(100))
            print(l1)
            sleep(1)
class T4(Thread):
    def run(self):
        while 1:
            l1.append(randbelow(100))
            print(l1)
            sleep(1)
class T5(Thread):
    def run(self):
        while 1:
            l1.append(randbelow(100))
            print(l1)
            sleep(1)
t1=T1()
t2=T2()
t3=T3()
t4=T4()
t5=T5()
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()


#5 Write a python script to create 2 threads to add all the values from 1 to 100.
from threading import *
class add(Thread):
    def run(self):
        print(sum([e for e in range(101)]))
        
a1=add()
a1.start()

#4 Write a python script to create two Threads. First thread will print 
# all Even numbers and Second thread will print all Odd numbers till 100.
from threading import *
from time import sleep
class Even(Thread):
    def run(self):
        for e in range(50):
            print(self.even)
            self.even+=2
            sleep(1)
class Odd(Thread):
    def run(self):
        for e in range(50):
            print(self.odd)
            self.odd+=2
            sleep(1)
e1=Even()
e1.even=2
o1=Odd()
o1.odd=1
e1.start()
o1.start()


#2 Write a python script to create a user account class with 2 instance variables
#  (userid and balance). Create 3 user objects and add all the users using 
# operator overloading.
#3 Write a python script to create a to print the above user account object using
#  operator overloading (hint __str__ method).
class User:
    def __init__(self,uid,bal):
        self.uid=uid
        self.bal=bal
    def __add__(self,uTemp):
        return User(0,self.bal+uTemp.bal)
    def __str__(self):
        return str.format("User ID: {} \nUser balance: {}",self.uid,self.bal)
u1=User(101,1000)
u2=User(102,2000)
u3=User(103,3000)
print("Total balance: ",(u1+u2+u3).bal)
print(u1)
print(u2)
print(u3)

#1 Write a python script to multiple 2 or 3 or 4 numbers with a single multiply
#  method in a class using method overloading.
class Maths:
    def __init__(self):
        pass
    def multiply(self,a,b=1,c=1,d=1):
        return a*b*c*d
m1=Maths()
print(m1.multiply(2,3))
print(m1.multiply(2,3,4))
print(m1.multiply(2,3,4,5))



"""