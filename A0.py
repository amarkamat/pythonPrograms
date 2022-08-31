from A1 import x

print(x)

a=int(input("Enter a number"))
if a>0:
    print("Positive number")
else:
    print("Non positive Number")


b=int(input("Enter your marks"))
if b<=100 and b>90:
    print("A grade")
elif b<=90 and b>80:
    print("B grade")
elif b<=80 and b>70:
    print("C grade")
else:
    print("D grade")

#c=input("Enter gender")
d=print("Male") if input("Enter gender")=='M' else print("Female")
print(d)

match int(input("Enter a number")):
    case 1:
        print("Hi")
    case 2:
        print("Hello")
    case _:
        print("No")

