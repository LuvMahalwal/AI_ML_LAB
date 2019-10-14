#VARIABLES
print("Hello World!")
intx=4
floatx=4.5
strx="Hello"
boolx=True
print("The value of intx is {}".format(intx))
print("Data type of 4 is",type(intx))
print("Data type of 4.5 is",type(floatx))
print('Data type of "Hello" is',type(strx))
print('Data type of True is',type(boolx))
#ARITHMETIC OPERATORS
print("-"*5+"Arithmetic Operators"+"-"*5)
a=25
b=20
print("a:",a)
print("b:",b)
print("Addition(a+b):",a+b)
print("Subtraction(a-b):",a-b)
print("Product(a*b):",a*b)
print("Division(a/b):",a/b)
print("Floored Division(a//b):",a//b)
print("Modulus(a%b):",a%b)
print("Exponentiation(a**b):",a**3)
#RELATIONAL OPERATORS
print("-"*5+"Relational Operators"+"-"*5)
print("a:",a)
print("b:",b)
print("> :",a>b)
print("< :",a<b)
print("== :",a==b)
print(">= :",a>=b)
print("<= :",a<=b)
print("!= :",a!=b)
#LOGICAL OPERATORS
print("-"*5+"Logical Operators"+"-"*5)
val1=True
val2=False
print("val1:",val1)
print("val2:",val2)
print("and :",val1 and val2)
print("or :",val1 or val2)
print("not val1 :", not val1)
print("not val2 :", not val2)
#STRINGS
print("-"*5+"Strings"+"-"*5)
string1="First"
string2="String"
string3=string1+" "+string2
print(string1.upper())
print(string1.lower())
print(string3)
print(string3[0])
print(string3[2:7])
print(string3[-2])
print(string1*5)
string4="Hello,Hi,Hey"
list1=string4.split(",")
print(list1)
print("%".join(list1))
#LISTS
print("-"*5+"Lists"+"-"*5)
templist1=[1,2,3,4]
print(templist1)
templist1.append("Hello")
print(templist1)
templist1.pop()
print(templist1)
templist1.remove(3)
print(templist1)
list2=list1.copy()
print(list2)
templist1.extend(list2)
print(templist1)
templist2=[3,1,4,2,5,0]
print(templist2)
templist2.sort()
print(templist2)
templist2.reverse()
print(templist2)
#DICTIONARIES
print("-"*5+"Dictionaries"+"-"*5)
dict1={
       1:"value1",
       2:"value2",
       "3":"value3"
       }
print(dict1[1])
print(dict1["3"])
dict1["newkey"]="newvalue"
print(dict1["newkey"])
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1)
dict1.popitem()
print(dict1)
dict1.pop(1)
print(dict1)
#TUPLES
print("-"*5+"Tuples"+"-"*5)
tuple1=(1,2,3,4)
print(tuple1)
print(tuple1[2])
listfromtuple=list(tuple1)
print(listfromtuple)
#If-else
print("-"*5+"If-Else"+"-"*5)
var1=int(input("Enter the value: "))
if var1>5:
    print("Greater than 5")
elif var1<2:
    print("Less than 2")
else:
    print("Less than 5 and greater than 2")
#LOOPS
i=1;
while i<10:
    print(i)
    i+=1
tempL=["apple","banana","mango","orange"]
for fruit in tempL:
    print(fruit)
for i in range(5,104):
    print(i)