#10
k=input("Enter your favourite color: ")
l=k.split()
for m in l:
    match m:
        case "yellow":
            print("Monday")
        case "blue":
            print("Tuesday")
        case "orange":
            print("Wednesday")
        case "white":
            print("Thursday")
        case "black":
            print("Friday")
        case "red":
            print("Saturday")
        case "green":
            print("Sunday")
        case "indigo":
            print("Sunday")


#9
j=int(input("Enter a year: "))
if j%4!=0:
    print("Common year")
    if j%100!=0:
        print("NCNLY")
    else:
        print("CNLY")
elif j%100!=0:
    print("Leap year")
    if j%100!=0:
        print("NCLY")
    else:
        print("CLY")
elif j%400!=0:
    print("Common year")
    if j%100!=0:
        print("NCNLY")
    else:
        print("CNLY")
else:
    print("Leap year")
    if j%100!=0:
        print("NCLY")
    else:
        print("CLY")


#8
m=input("Enter first string: ")
n=input("Enter second string: ")
match "order" if n>m else "inorder" if m!=n else "identical":
    case "order":
        print("As per dictionary")
    case "inorder":
        print("Not as per dictionary")
    case "identical":
        print("Identical")


#7
l=int(input("Enter a number: "))
match ('-' if l<0 else '+') if l!=0 else '0':
    case '-':
        print("Negative")
    case '0':
        print("Zero")
    case '+':
        print("Positive")
    case _:
        print("Invalid")


#6
j=input("Enter a string: ")
print("Word count: ",len(j.split()))
match len(j.split()):
    case 1:
        print("Single word string")
    case _:
        print("Multiword string")


#5
i=int(input("Enter a number: "))
if i>0 and i%2==0:
    print("Saurabh shukla")
elif i<0 and i%2!=0:
    print("Prateek jain")
elif i>0 and i%2!=0:
    print("Aditya Choudhary")
else:
    print("Invalid")

#4
h=int(input("Enter your age: "))
if 0<h<10:
    print("Kid")
elif 10<=h<20:
    print("Teen")
elif 20<=h<40:
    print("Young")
elif 40<=h<60:
    print("Experienced")
elif 60<=h:
    print("Senior citizen")
else:
    print("Invalid")

#3
e=int(input("Enter 3 sides of a triangle: \n"))
f=int(input())
g=int(input())
if (e==f and f!=g) or (f==g and g!=e) or (e==g and g!=f):
    print("Isosceles triangle")
if e!=f and f!=g and g!=e:
    print("Right angle triangle")
if e==f==g:
    print("Equilaterel triangle")

#2
b=input("Enter operation to be performed (+,-,*,/): ")
c=float(input("Enter first number: "))
d=float(input("Enter second number: "))
match b:
    case '+':
        print("Result: ",c+d)
    case '-':
        print("Result: ",c-d)
    case '*':
        print("Result: ",c*d)
    case '/':
        print("Result: ",c/d)
    case _:
        print("Invalid")

#1
a=int(input("Enter Month in numeric format: "))
match a:
    case 1:
        print("31 days")
    case 2:
        print("28 days")
    case 3:
        print("31 days")
    case 4:
        print("30 days")
    case 5:
        print("31 days")
    case 6:
        print("30 days")
    case 7:
        print("31 days")
    case 8:
        print("31 days")
    case 9:
        print("30 days")
    case 10:
        print("31 days")
    case 11:
        print("30 days")
    case 12:
        print("31 days")
    case _:
        print("Invalid")