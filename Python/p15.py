#10
a=int(input("Enter a number: "))
b=str(a)
print(a,type(a))
print(b,type(b))


#9
a=input("Enter a string: ")
print("String contains only alphabets" if True==a.isalpha() else "String does not contain only alphabets")


#8
a=input("Enter a string: ")
print("String contains only numbers" if True==a.isdigit() else "String does not contain only numbers")

#7
a="Knowledge"
b="ge"
print("Substring not found" if a.find(b) < 0 else "Substring found")

#6
a="iNeuron"
print(a[-1:-8:-1])

#5
a="iNeuron"
print(a,len(a))

#4
a="Learning"
b="Python"
c=a+' '+b
print(c)


#3
y="Hello Learners"
print(y[2:6:1])

#2
x='iNeuron'
print(x[0:6:1])


#1
a="string"
b='next'
c=str("best")
print(a,b,c)