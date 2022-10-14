#10
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
print(min(sample_dict.values()))
print(min(sample_dict.keys()))
for k in sample_dict:
    if sample_dict[k]== min(sample_dict.values()):
        print("Key of lowest vale= ",k)
        break

#9
d1={1:'a',2:'b'}
d2={3:'c',4:'d'}
d3=dict(d1)
d3.update(d2)
print(d3)


#8
l1=[1,2,3]
l2=['a','b','c']
#d1={k:v for k,v in l1[l2]}
d1={}
i=0
while i<len(l1):
    d1[l1[i]]=l2[i]
    i+=1
print(d1,type(d1))


#7
d1={1:'a',2:'b'}
d2={3:'c',4:'d'}
d3={5:'e',6:'f'}
d4={}
d4[10]=d1
d4[20]=d2
d4[30]=d3
print(d4)

#6
d1={10:{1:'a',2:'b'},20:{3:'c',4:'d'},30:{5:'e',6:'f'}}
print(d1)
for k in d1:
    print(k,d1[k])
    for i in d1[k]:
        print(i,d1[k][i])


#5
d1={1:'as',2:'sd',3:'df'}
for k in d1:
    print(k)


#4
d1={1:'as',2:'sd',3:'df'}
print(d1)
d1[2]='fg'
print(d1)


#3
d1={1:'as',2:'sd',3:'df'}
for k,v in d1.items():
    print(k,v)


#2
d1={1:'as',2:'sd',3:'df'}
for k in d1:
    print(k,d1[k])


#1
d1={}
i=0
while i<1:
    n=input("Enter your name: ")
    a=input("Enter your age: ")
    g=input("Enter your gender: ")
    b=input("Enter your birthdate: ")
    d1[n]=(a,g,b)
    i+=1
print(d1)

#test
d1={1:'as',2:'sd',3:'df'}
d2=dict(a='5',b={1,2},c=['a','s'])
print(d1)
print(d2)
d3={}
print(type(d3))
d1[4]=(2.3,3.2)
for k in d1:
    print(k)
    print(d1[k])

d4={item: value for (item, value) in d1.items()}
print(d4)

