#10
def f10(num):
    return True if num%2==0 else False
a=30
b=f10(a)
print("Is ",a," even number? ",b)


#9
def f9(num,range):
    print(num,range)
    for e in range:
        if e==num:
            return True
    else:
        return False
a=1
b=f9(a,range(1,10,1))
print("Result is ",b)

#8
def f8(nums):
    print(nums)
    mul=1
    for e in nums:
        mul=mul*e
    return mul
n=f8([1,2,3,4])
print("Multiply is ",n)


#7
def f7(nums):
    print(nums)
    return sum(nums)
n=f7([1,2,3,4])
print("Sum is ",n)


#6
def f6(nums):
    print(nums)
    num=max(nums)
    return num
n=f6([2,3,1,4])
print("Max is ",n)


#5
def f5(list):
    print(list)
f5([1,2,3])

#4
def f4(a,b,c):
    print(a,b,c)
f4(a=2,c=True,b='as')

#3
def f3(*t):
    print(t)
f3(1,2,3,4,5,"string",[1,2,3],{1,2,3},(1,2,3),range(10))

#2
def f2(a,b):
    print(a,b)
f2(10,20)

#1
def f1():
    print("MySirG")
f1()
