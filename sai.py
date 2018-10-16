Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #to find area and perimeter of the circle
>>> pi=3.14
>>> r=int(input("enter the radius of circle"))
enter the radius of circle15
>>> A=pi*r*r
>>> p=2*pi*r
>>> 
>>> print('area of circle',A)
area of circle 706.5
>>> print('perimeter of circle',p)
perimeter of circle 94.2
>>> 
>>> 
>>> 
>>> #to find area and perimeter of a reactangle
>>> pi=3.14
>>> l=int(input("enter the length of reactangle"))
enter the length of reactangle100
>>> b=int(input("enter the breath of  reactangle"))
enter the breath of  reactangle50
>>> a=l*b
>>> p=2*l+2*b
>>> 
>>> print("area is",a)
area is 5000
>>> print("perimeter is",p)
perimeter is 300
>>> 
>>> 
>>> 
>>> #to find area and perimeter of a square
>>> s=int(input("enter the side"))
enter the side10
>>> a=s*s
>>> p=4*s
>>> 
>>> print("area is",a)
area is 100
>>> print("perimeter is",p)
perimeter is 40
>>> 
>>> 
>>> 
>>> 
>>> 
>>> #to find area and perimeter of a tringle
>>> b=int(input("enter the base"))
enter the base50
>>> h=int(input("enter the hight"))
enter the hight60
>>> a=0.5*b*h
>>> print("area is",a)
area is 1500.0
>>> 
>>> 
>>> 
>>> 
>>> #creating and printing the list
>>> L1=[1,2,3,4]
>>> L2=['sainath','rahul','aditya']
>>> L3=[1,2,'sainath','rahul',3,4]
>>> 
>>> print[L1]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print[L1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> PRINT(L1)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    PRINT(L1)
NameError: name 'PRINT' is not defined
>>> print(L1)
[1, 2, 3, 4]
>>> print(L3)
[1, 2, 'sainath', 'rahul', 3, 4]
>>> print[(L1)+(L2)]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print[(L1)+(L2)]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(L1+L2)
[1, 2, 3, 4, 'sainath', 'rahul', 'aditya']
>>> L4=[]
>>> del(L4)
>>> print(L4)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    print(L4)
NameError: name 'L4' is not defined
>>> L2[2]="atul"
>>> print(L2)
['sainath', 'rahul', 'atul']
>>> print(L2[1])
rahul
>>>exit()








