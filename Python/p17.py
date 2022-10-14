#10
s1={1,2,3,4}
print(s1)
print(max(s1))
print(min(s1))


#9
thisset = {"Python", "Django", "JavaScript", "SQL"}
for e in thisset:
    print(e)


#8
thisset = {"Python", "Django", "JavaScript","SQL"}
print(thisset)
del(thisset)
#print(thisset)

#7
thisset = {"Python", "Django", "JavaScript","SQL"}
print(thisset)
#thisset.remove("SQL")
thisset.pop()
#thisset.discard("SQL")
print(thisset)


#6
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
print(thisset,mylist)
for e in mylist:
    thisset.add(e)
print(thisset,mylist)


#5
s1={"Java","Python","SQL"}
s2={"C","CPP","NOSQL"}
s3=s1.union(s2)
print(s1,s2,s3,sep='\n')


#4
thisset={"Java","Python","Django"}
for e in thisset:
    if e=="Python":
        print("Python found")

s3=thisset.intersection({"Python"})
print(s3)

b=thisset.issuperset({"Python"})
print(b)

#3
s2={1,2,3}
print(type(s2),s2)


#2
a=input("Enter name: ")
b=int(input("Enter age: "))
c=input("Enter gender: ")
d=int(input("Enter birthday: "))
s1={a,b,c,d}
print(s1)


#1
lang={"Java","C","C++","Python","Fortran","Basic","Pascal","C"}
lang.update((3,4))
lang.add((1,2))
print(lang,type(lang))