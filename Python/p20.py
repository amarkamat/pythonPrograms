#10
def checkAnagram(s1,s2):
    ret=False
    if len(s1)==len(s2):
        for e in s1:
            if e not in s2:
                ret=False
            else:
                ret=True
    else:
        ret=False
    return ret
s1="brush"
s2="shrub"
if True==checkAnagram(s1,s2):
    print("Strings are anagram")
else:
    print("Strings are not anagram")


#9
def checkPangram(set1):
    letset="abcdefghijklmnopqrstuvwxyz"
    set2=set(letset)
    if len(set2.difference(set1))==0:
        print("String is pangram")
    else:
        print("String is not pangram")
#s2="abcdefghijklmnopqrstuvwxyz"
#s2="adgh"
s2="The quick brown fox jumps over the lazy dog"
set1=set(s2.lower())
print(set1)
checkPangram(set1)


#8
from curses.ascii import islower, isupper
def countLetters(s1):
    up=0
    low=0
    for e in s1:
        if isupper(e)==True:
            up+=1
        elif islower(e)==True:
            low+=1
        else:
            pass
    print("Letters Upper: ",up,"Lower: ",low)
countLetters("AbSdee1")

#7
def f1():
    print("Inside f1")
def f2():
    print("Inside f2")
    f1()
f2()


#6
def squareNum():
    print([e*e for e in range(1,31,1)])
squareNum()


#5
def minNum(a,b,c):
    return a if a<c else c if a<b else b if b<c else c
a,b,c=0,3,-1
print("Numbers: ",a,b,c)
print("Minimum: ",minNum(a,b,c))


#4
def checkPalindrome(str):
    if str == str[-1::-1]:
        print("String is Palindrome")
    else:
        print("String is not pandrome")
instr="Krark"
checkPalindrome(instr.lower())


#3
def evennum(list):
    l1=[]
    for e in list:
        if e%2==0:
            l1.append(e)
    print("Even numbers: ",l1)
evennum([1,2,3,4,5,6,7,8,9,11,22,33,44,55])


#2
def checkforprime(num):
    i=2
    while i<num:
        if num%i==0:
            return False
        i+=1
    else:
        return True
if True==checkforprime(11):
    print("Number is Prime")
else:
    print("Number is not prime")


#1
def f1(list):
    s1=set(list)
    print(list)
    l1=[e for e in s1]
    return l1

l1=f1([1,2,3,4,1,3])
print(l1)


