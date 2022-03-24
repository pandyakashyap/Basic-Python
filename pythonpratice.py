import module
print('hello world')

a=10
b=20
c=5


#************************************************    Condition   ****************************************************

if a>b:
    print('a is bigger')
elif b>a:
    print('b is bigger')
else:
    print('not any')



#**********************************************      Operator    *******************************************************
     #And , Or ,Not
if a>b or b>c:
    print('both condition are true')
else:
    print('not true')



    #== , >= , <= , !=
if a==b:
    print('YES')
    if a>=b:
        print('both YES')
    else:
        print('both not')
else:
    print('NOT')


    #+,-,*,/
print('Sum Is :- ',a+b)



    #in , not in
a=['kashyap','ravi','sujit']
if('kashyap' in a):
    print(a)
else:
    print('not match name')



#***********************************************    Loops   ************************************

car=['BMW', 'I20' ,'Verna']
for x in car:
    print(x)


i=1
while i<=5:
    print(i)
    i+=1;

#***************************************  Break - Continue ************************************

a=[1,2,3,4,5]
for b in a:
    if b==3:
        break
    print(b)


for b in a:
    if b==4:
        continue
    print(b)



#*************************************      Function    *****************************************


def show():
    print('Hello Python Function')
show()


def sum(a,b):
    c=a+b
    print(c)
sum(10,5)



#***********************************  Lambda Function   ********************************************
#can take any number of arguments, but can only have one expression.

a = lambda x,y,z:x+y+z
print(a(10,5,2))


#array
a=['name','surname','location']
print(a)

b=a[2]
print(b)


#class - object
class abc:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
p=abc('kashyap','pandya')
print(p.name)
print(p.surname)


#Exception Handling
a=10
b=0

try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Zero Division Error")
else:
    print("Succesfully Run")
finally:
    print("Always Executed")


#module(package) concept
#create module.py file on dekstop check it 
module.sum()













