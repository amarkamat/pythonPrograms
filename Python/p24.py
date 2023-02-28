#1
class user:
    name="Ravi"
    age=21
    email="abc@gmail.com"

    @classmethod
    def greet(cls):
        print("Hello ",cls.name)

    def __init__(self,name,age,email):
        self.name=name
        self.age=age
        self.email=email

    @staticmethod
    def youngest(u3,u4,u5):
        return u3.name if u3.age<u5.age else u5.name if u3.age<u4.age else u4.name if u4.age<u5.age else u5.name


print(user.name)
print(user.age)
print(user.email)


#2
user.greet()


#3 #4
u1=user("Jack",21,"a@gmail.com")
u2=user("Sam",22,"b@gmail.com")
print(user.name,user.age,user.email)
print(u1.name,u1.age,u1.email)
print(u2.name,u2.age,u2.email)

#5
del(user.age)

#6
u3=user("dad",20,"c@gmail.com")
u4=user("fes",24,"d@gmail.com")
u5=user("pow",19,"e@gmail.com")
print("Youngest: ",user.youngest(u3,u4,u5))


#7

class Laptop:

    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def showConfig(self):
        print("Laptop details: ",self.brand,self.ram,"GB",self.cpu,self.hdd)

#8
l1=Laptop("Apple",16,"AMD","128GB")
l1.showConfig()
l2=Laptop("Lenovo",8,"Intel","64GB")
l2.showConfig()
l3=Laptop("Dell",4,"Intel","256GB")
l3.showConfig()

l_dict={l1.ram:l1,l2.ram:l2,l3.ram:l3}
l_list=sorted([l1.ram,l2.ram,l3.ram])
l_sorted_list=[l_dict[l_list[0]].brand,l_dict[l_list[1]].brand,l_dict[l_list[2]].brand]
print(sorted(l_list))
print(l_sorted_list)



#9
class School:
    District="Troy"

    def __init__(self,name,address,pin):
        self.name=name
        self.address=address
        self.pin=pin

s1=School("Bemis","Somer","48084")


#10
class Employee:
    def __init__(self,id=0,name="",sal=0):
        self.empid=id
        self.name=name
        self.salary=sal

    def input(self,id,name,sal):
        self.empid=id
        self.name=name
        self.salary=sal
    
    def display(self):
        print(self.empid,self.name,self.salary)

e1=Employee()
e1.input(11,"Jack",1200)
e1.display()

