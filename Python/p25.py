#1 #2 #3 #4
from re import sub


class Profile:

    platform="railway"

    @classmethod
    def getplatform(cls):
        return cls.platform
    @classmethod
    def setplatform(cls,pf):
        cls.platform=pf

    def __init__(self,name,email,age):
        self.name=name
        self.__email=email
        self.__age=age
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_email(self):
        return self.__email
    def set_email(self,email):
        self.__email=email
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age=age

p1=Profile("Bill","b@gmail.com",22)
print(Profile.get_name(p1),Profile.get_email(p1),Profile.get_age(p1))

Profile.set_name(p1,"Jack")
Profile.set_email(p1,"a@gmail.com")
Profile.set_age(p1,21)
print(Profile.get_name(p1),Profile.get_email(p1),Profile.get_age(p1))

print(Profile.getplatform())
Profile.setplatform("bus")
print(Profile.getplatform())


#5 #6
class Calculator_2:
    def __init__(self):
        pass
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

class Calculator(Calculator_2):
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b


c1=Calculator()
print("Add",c1.add(10,20))
print("Substract",c1.sub(20,30))
print("Multiplication",c1.mul(2,4))
print("Division",c1.div(12,23))


#7 #8 #9 #10
class Phone:
    def __init__(self):
        pass
    def call(self):
        print("Calling")
    def sms(self):
        print("Sending sms")

class Smartphone(Calculator_2,Phone):
    def __init__(self):
        pass
    def method(self,tc):
        tc.fetchname()
        tc.addentry()

class Truecaller:
    def __init__(self):
        pass
    def fetchname(self):
        print("Fetching the name")
    def addentry(self):
        print("Adding entry")


sp=Smartphone()
tc=Truecaller()
sp.sms()
sp.call()
sp.method(tc)


