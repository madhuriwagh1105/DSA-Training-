#====================WiproTest==========================
# The garments company Apparel wishes to open outlets at various locations. The company shortlisted several plots in these locations and wishes to select only plots that are square-shaped.
# Write an algorithm to help Apparel find the number of plots that it can select for its outlets.
# Input
# The first line of the input consists of an integer numOfMots, representing the number of plots shortlisted by the company for outlets (N).
# The second line consists of N space-separated integers - areal, areal,....., areaN representing the area of the N plots selected for outlets.
# Output==>
# Print an integer representing the number of plots that will be selected for outlets.

# Input:
# 8
# 79 77 54 81 48 34 25 16

# Output:
# 3
# Explanation:
# The areas that are in square form are 81, 25 and 16. So, the output is 3.

# import math

# area=81
# p=math.sqrt(area)
# print(p)
#----------------
# size=int(input("Enter the size of array:"))
# area=list(map(int,input().split()))
# count=0
# for area in area:
#     root=int(math.sqrt(area))

#     if root*root==area:
#         count+=1
# print(count)

#=============================MCQ================================
# def func(value,values):
#     var=1
#     values[0]=44
# t=3
# v=[1,2,3]
# func(t,v)
# print(t,v[0])

# 1.1 44
# 2.3 1
# 3. 3 44
# 4.1 1

#=============================MCQ================================
# def f(i,values=[]):
#     values.append(i)
#     print(values)
# f(1)
# f(2)
# f(3)

# 1.[1][2][]
# 2.[1,2,3]
# 3.[1][1, 2][1, 2, 3]
# 4.1 2 3 

#============================Queue================================

# 1.EnQueue()
# 2.DeQueue()
# 3.Display()
# 4.isEmpty()
# 5.isFull()
# 6.Delete()
# 7.peek()

# import sys

# class Queue:
#     def __init__(self,size):
#         self.myQueue=[] #creating stack
#         self.Queuesize=size  #stack size defined

#     def isFull(self):
#         if len(self.myQueue)==size:
#             return True
#         else:
#             return False
    
#     def enQueue(self,value):
#         if self.isFull():
#             print("Queue is full")
#         else:
#             self.myQueue.append(value)            


#     def display(self):
#         print(self.myQueue)
        

#     def isEmpty(self):
#         if self.myQueue==[]:
#             return True
#         else:
#             return False
        
#     def DeQueue(self):
#         if self.isEmpty():
#             print("Queue is Empty")
#         else:
#             self.myQueue.pop(0)
#             self.display()

#     def peek(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue[0])

#     def deleteQueue(self):
#         self.myQueue=None

# size=int(input("Enter the size of Queue:"))
# obj=Queue(size)
# print("============================================================")
# print("Queue has created:")

# while True:
#     print("1.push operation:")
#     print("2.Display Queue:")
#     print("3.DeQueue operation:")
#     print("4.peek operation") #======>return top most element(not remove)
#     print("5.Delete operation")
#     print("5.Delete operation")
#     print("7.Exit")
#     print("============================================================")
#     choice=int(input("Enter your choice:"))
#     if choice== 1:
#         value=int(input("Enter value to add in Queue:"))
#         obj.enQueue(value)   
#     elif choice==2:
#        obj.display()
#     elif choice==3:
#         obj.DeQueue()
#     elif choice==4:
#         obj.peek()
#     elif choice==5:
#         obj.deleteQueue()
#     else:
#         sys.exit()

#============================MCQ================================
# fruit={}
# def addone(index):
#     if index in fruit:
#         fruit[index]+=1
#     else:
#         fruit[index]=1
# addone('apple')
# addone('Apple')
# addone('Banana')
# print(len(fruit))

# a.1
# b.2
# c.3
# d.4

#===============================================================
#  Write a program to accept student name and marks from the keyboard 
# and creates a dictionary. Also display student marks by taking student name
#try this with switch case

# n=int(input("enter th number of students:"))
# d={}
# for i in range(n):
#     name=input("Enter student name:")
#     marks=input("Enter marks of students:")
#     d[name]=marks
# while True:
#     name=input("enter the students name to get marks:")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("Student not found")
#     else:
#         print("the marks of",name,"are",marks)
#     option=input("do you want to find another students marks[YES|NO]:" )
#     if option=="NO":
#         break
#     else:
#         print("thank you for using our application")

#================================After Lunch Break====================================           
# Write a program to access each character of string in forward and backward direction by using while loop?
# "Learning Python is very easy"

# s="Learning Python is very easy"
# i=0
# print("======Forward firection========")
# while i<len(s):
#     print(s[i],end="")
#     i+=1

# print("======Backward firection========")
# i=len(s)-1
# while i>=0:
#     print(s[i],end="")
#     i-=1

# s="Learning Python is very easy"
# n=len(s)
# i=0
# print("======Forward firection========")
# while i<n:
#     print(s[i],end="")
#     i+=1

# print("======Backward firection========")
# i=-1
# while i>=-n:
#     print(s[i],end="")
#     i-=1

#====================================================================
# A company provides network encryption for secure data transfer. The data string is encrypted prior to transmission 
# and gets decrypted at the receiving end. But due to some technical error, the encrypted data is lost and the received
# string is different from the original string by 1 character. Arnold, a network administrator, is tasked with finding the 
# character that got lost in the network so that the bug does not harm other data that is being transferred through the network.
# Write an algorithm to help Arnold find the character that was missing at the receiving end but present at the sending end.

# Input:
# The input consists of two space-separated strings - stringSentand string Rec, representing the string that was sent through 
# the network, and the string that was received at the receiving end of the network, respectively.

# input:abcdfjerj abcdfjer
# output:j

# s="abcdfjerj abcdfjer"
# a,b=s.split()
# print(a)
# print(b)
# i=0
# if i<len(s):
#     if a[i]!=b[i]:
#         print(a[i])
#         i+=1
#     else:
#         print(a[-1])

#====================================================================
# v=['a','e','i','o','u']
# w=input("Enter the word where we will search the vowels:")
# found=[]
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels=',found)
# print("Unique vowels=",len(found),'from the given word=',w)

#====================================================================

# A company wishes to provide cab service for their N employees. The employees have distance ranging from 0 to N-1. 
# The company has calculated the total distance from an employee's residence to the company, considering the path to
# be followed by the cab is a straight path. The distance of the company from itself is O. The distance for the employees 
# who live to the left side of the company is represented with a negative sign. The distance for the employees who live to 
# the right side of the company is represented with a positive sign. The cab will be allotted a range of distance. 
# The company wishes to find the distance for the employees who live within the particular distance range.
# Write an algorithm to find the distance for the employees who live within the distance range.

# Input
# The first line of the input consists of three space-separated integers-num, start and end representing the 
# size of the list (N); the starting value of the range: and the ending value of the range, respectively. 
# The second line of the input consists of N space-separated integers representing the distances of the employees 
# from the company

# Input:
# 6 30 50
# 29 38 12 48 39 55
# Output:
# 38 48 39

# Explanation:
# There are three employees with distances 38, 48 and 39 whose distance from the office lies within the given range.

# x, y, z =map(int, input().split())
# mylist=[]
# for i in range(x):
#     a=int(input())
#     mylist.append(a)

# for j in mylist:
#     if j>=y and j<=z:
        # print(j,end=" ")
#incomplete

#====================================================================
# import datetime
# date=datetime.datetime.now()
# print("its now:{:%d/%m/%y %H:%M:%S}".format(date))

#====================================================================
# in this address is compared
# x=['a','b','c']
# y=['a','b','c']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)

#====================================================================
# list comprehension
# val=[2**i for i in range(1,6)]
# print(val)

# val=[i**i for i in range(1,11)]
# print(val)

#====================================================================
#dictionary comprehension
# squares={x:x*x for x in range(1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

#====================================================================
#how to read multiple value from keyboard in a single line

# a,b=[int(x)for x in input("Enter 2 numbers:").split()]
# print("product is :",a*b)

# write a program  to read 3 float number from keyword in single line using space

# a,b,c=[float(x) for x in input("Enter 3 float numbers:").split(',')]
# print("the sum is :",a+b+c)

#====================================================================
# we can use else block with for loop in python
# mycart=[10,20,800,60,70]
# for item in mycart:
#     if item>400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("you have purchased eveything")
    
#====================================================================
# ````
# while True:
#     name=input("enter username:")
#     password=input("enter password:")
#     if name=="admin" and password=="admin":
#         print("login successfully..")
#         break
#     else:
#         print("invalid")

#====================================================================
#Tower of Hanoi
# import time
# class Tower:
#     def __init__(self):
#         print("================WELCOME TO TOWER OF HANOI GAME================")
#         print()
#         print("Given problem A=[3,2,1] B=[] C=[]")
#         print()
#         print("Expected Outpur A=[] B=[] C=[3,2,1]")
#         self.A=[]
#         self.B=[]
#         self.C=[]

#     def tower(self,item):
#         self.A.append(item)
#         time.sleep(3)
#         print("A=",self.A)
#         print("Item in Tower A \n")
    
#     def pass1(self):
#         self.temp=self.A.pop(2)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A   ," ","B=",self.B  ,"  ","C=",self.C)
#         print("========================================Pass one Completed========================================\n")

#     def pass2(self):
#         self.temp=self.A.pop(1)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A   ," ","B=",self.B  ,"  ","C=",self.C)
#         print("========================================Pass two Completed========================================\n")

#     def pass3(self):
#         self.temp=self.C.pop(0)
#         self.B.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A   ," ","B=",self.B  ,"  ","C=",self.C)
#         print("========================================Pass three Completed========================================\n")

#     def pass4(self):
#         self.temp=self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A   ," ","B=",self.B  ,"  ","C=",self.C)
#         print("========================================Pass four Completed========================================\n")

#     def pass5(self):
#         self.temp=self.B.pop(1)
#         self.A.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A   ," ","B=",self.B  ,"  ","C=",self.C)
#         print("========================================Pass five Completed========================================\n")

#     def pass6(self):
#         self.temp=self.B.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A   ," ","B=",self.B  ,"  ","C=",self.C)
#         print("========================================Pass six Completed========================================\n")

#     def pass7(self):
#         self.temp=self.A.pop(0)
#         self.C.append(self.temp)
#         time.sleep(3)
#         print("A=",self.A   ," ","B=",self.B  ,"  ","C=",self.C)
#         print("========================================Pass seven Completed========================================\n")

# obj=Tower()
# obj.tower(3)
# obj.tower(2)
# obj.tower(1)
# obj.pass1()
# obj.pass2()
# obj.pass3()
# obj.pass4()
# obj.pass5()
# obj.pass6()
# obj.pass7()
