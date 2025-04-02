# # # def p(n):
# # #     if n==1:
# # #         print('i is not a prime num')
# # #
# # #     if n==2:
# # #         print('2 is prime num')
# # #     for i in range(2,n):
# # #         if n%i==0:
# # #             print('is not a prime number')
# # #             break
# # #         else:
# # #             print('it is prime number')
# # #             break
# # # p(7)
# # #
# # #
# #
# # # adding numbers in the list
# # # def add(l):
# # #     z = 0
# # #     for i in l:
# # #         z = z + i
# # #     return (z)
# # # print(add([1,2,3]))
# #
# # # l=[1,2,3,4,5,6,7,8,9]
# # # z=0
# # # for i in l:
# # #
# # #     z=z+i
# # # print(z)
# #
# # n=int(input('enter the numbre:'))
# # z=0
# # for i in range(0,n):
# #     z=z+i
# # print(z)
# # import datetime
# # a= datetime.datetime(2001,4,25)
# # print(a)
# # print(a.strftime("%m"))
# # import random
# # l=['heads','talis']
# # x=random.choice(l)
# # print(x)
# # y=random.randint(1,10)
# # print(y)
# # import uk
# # b=uk.add(4,2)
# # print(b)
# # a= lambda a:a**2
# # b=int(input('enter the number'))
# # print(a(b))
# #
# # def a(x):
# #     return (x**2)
# # print(a(10))
# # def a(x):
# #     return (x+2)
# # x=int(input())
# # print(a(x))
# # from itertools import repeat
# # from math import trunc
# # from random import randint
#
# # def sum(a,b,c):
# #     return (a+b+c)
# # print(sum(10,20,30))
# # d=lambda x,y,z:x+y+z
# # print(d(10,20,30))
# # def a(n):
# #     return lambda a:a*n
# # mydoubler=a(2)
# # # print(mydoubler(11))
#
#  #objacts and classes in python
#
# # class A:
# #     x=10
# #     y=10
# # obj1=A()
# # print(obj1.y)
#
# #file halddling inp python
# # f=open("U:/u.txt",'r')
# # print(f.read())
# # f=open("U:/u.txt",'w')
# # print(f.write("hiii "
# #               "every one my name is uday kiran"))
# # f=open("U:/u.txt",'a')
# # print(f.write("\n my numbre is \n 525151515151"))
# # f=open("U:/u.txt",'r')
# # print(f.read())
# # print("hi my name is uday kiran \n uday is my name ")
#
# # f=open("U:/code/demo.py",'x')
# # f=open("U:/code/demo.py",'w')
# # print(f.write("print('hello world')"))
# # f=open("U:/code/demo.py",'r')
# # print(f.read())
# # f=open("U:/code/demo.py",'a')
# # print(f.write("\n print('hello bro')"))
# # f=open("U:/code/demo.py",'r')
# # print(f.read())
# # import os
# # from idlelib.help_about import version
# #
# # # from os import remove
# # #
# # # f=remove('U:/cod
# # import
#
#
#
# import numpy as np
# # import random
# # l=['heads','tails']
# # x=random.choice(l)
# # print(x)
# # def s():
# #     print('do you want to shuffele press 1 to shfuul or 2 to exit')
# #     c = int(input('enter the number '))
# #     if c=='s':
# #         print('your random choice is ouver')
# #     while c == 'n':
# #         x = random.choice(l)
# #         print(x)
# #         s()
# #         break
# # s()
#
# # m=[]
#
# #this id the first program you did on your own using while and it was ypur own idea
#
# # a=int(input('enter the number '))
# # b=int(input('enter the number '))
# # bu=randint(a,b)
# # print(bu)
# # def s():
# #     print('do you want to shuffele press 1 to shfuul or 2 to exit')
# #     c = int(input('enter the number '))
# #     if c==2:
# #         print('your random choice is ouver')
# #     while c == 1:
# #         bu = randint(a, b)
# #         print(bu)
# #         s()
# #         break
# # s()
#
# import random
#
# # while True:
# #     l = ['heads', 'tails']
# #     x = random.choice(l)
# #     print(x)
# #     while True:
# #         repeat = input('click yes to continue,no to exit')
# #         if repeat == "no" or repeat == "NO" or repeat == "n" or repeat == "N":
# #             print('finished')
# #             break
# #         if repeat == "yes" or repeat == "YES" or repeat == "Yes" or repeat == "s":
# #             x1 = random.choice(l)
# #             break
# # def cal():
# #         c=None
# #         while True:
# #             if c is None:
# #                 a = int(input("enter first number:"))
# #                 b = int(input("enter second number"))
# #             else:
# #                 a=c
# #                 b = int(input("enter second number"))
# #
# #             co = input("select the operator")
# #             if co == "+":
# #                 c = a + b
# #                 print('sum of the numbers', c)
# #             elif co == "-":
# #                 c = a - b
# #                 print('sub of the numbers', c)
# #             elif co == "*":
# #                 c = a * b
# #                 print('mul of the numbers', c)
# #
# #             d=input(" do you wnat to contunuee")
# #             if d=='no'  :
# #                 break
# # cal()
#
# # a=5
# # for i in range(1,a+1):
# #     print(i*"*")
# #
# # for i in range(a,0,-1):
# #     print(i*"*")
# #
# for i in range(1,a+1):
#
#     for j in range(1,i+1):
#
#         print(j,end="")
#     print( )
# # for i in range(1, a + 1):
# #
# #     for j in range(i,0,-1):
# #         print(j, end=" ")
# #     print()
# # for i in range(1,a+1):
# #
# #     for j in range(1,i+1):
# #
# #         print(i,end=" ")
# #     print( )
# # for u in range(1,11):
# #
# #     for k in range(1,u+1):
# #
# #         print(u*k,end=" ")
# #     print( )
# #
# # for f in range(1,6):
# #     for g in range(5,f,-1):
# #         print(' ', end=" ")
# #     for l in range(f):
# #         print(f,end=" ")
# #     print( )
# #
# #
# print("this is problem 3")
# for i in range(1,6):
#     for j in range(5,i,-1):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
# #
# #     print( )
# #
# # for i in range(1,a+1):
# #     print(" "* (a-i) + "*" * (2*i-1))
#
#
#
#
# # for i in range(1,a+1):
# #     print(" "* (a-i) + "*" * (2*i-1))
# #
# # for i in range(a-1,0,-1):
# #     print(" "* (a-i) + "*" * (2*i-1))
for  i in range(1,6):

    for j in range(1,i+1):
        print(j, end=" ")
    print( )
a=5
for i in range(6,0,-1):

    for j in range(i,0,-1):

        print(j,end=" ")
    print( )
print("this is problem 3")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print( )
for i in range(1,a+1):
    print(' '*(a-i)+'*'*(2*i-1))












