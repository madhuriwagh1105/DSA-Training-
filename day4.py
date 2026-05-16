# salary=(int(input("Enter your salary:")))
# rating=(int(input("Enter your performance appraisal rating:")))
# increment=0
# if rating>=1 and rating<=3:
#     increment=salary*10/100
# elif rating>=3.1  and rating<=4:
#     increment=salary*30/100
# elif rating>=4.1 and rating<=5:
#     increment=salary*40/100
# else:
#     print('invalid ratiing')
# print('incremented salary:',increment+salary)

#============================================================

# BasicSal=20000

# so we have to calculate the 
# HRA of BasicSal=20%
# TA of----------=30%
# DA of ---------=45%

# calculate grossSal=?

# BasSal=20000
# HRA=BasSal*20/100
# TA=BasSal*30/100
# DA=BasSal*45/100
# total_gross=HRA+TA+DA+BasSal
# print("GrossSalary=",total_gross)

#=============================================================
#binary search
# def binarySeach(array,target):
#     low=0
#     high=len(array)-1
#     while low<=high:
#         mid=(low+high)//2
#         if array[mid]==target:
#             return mid
#         elif array[mid]<target:
#             low=mid+1
#         else:
#             high=mid-1
#     return -1

# array=[2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,50,60,62,63,67,70,72,70]
# target=72
# result=binarySeach(array,target)
# if result==-1:
#     print("Element not found")
# else:
#     print("element found at",result)

#=============================================================
#bubble sort
# def bubbleSort(array):
#     for i in range(len(array)-i-1):
#         for j in range(len(array)):
#             if array[j]>array[j+1]:
#                 temp=array[j]
#                 array[j]= array[j+1]
#                 array[j+1]=temp
#             print(array)
#         print()
    
# array=[64,34,25,12,22,11,90]
# bubbleSort(array)
#incomplete

#=============================================================
#WAP security key check
# input=578378923
# output=3
# mylist=[5,7,8,3,7,8,9,2,3]
# newlist=[]

# for i in range(len(mylist)):
#     count=0
#     key=mylist[i]
#     j=i+1
#     while j<len(mylist):
#         if key==mylist[j]:
#             newlist.append(key)
#         j=j+1
# print(len(newlist))

#try thiss question with nested loop
#========================After Lunch BReak=====================================

#stack implementation without size limit
#stack implementation with size limit

# class Name:
#     age=30  #data member
#     def display(self):  #=========>(self)default argument==== method member or method
#         print("hello world") 

# obj=Name() #========>object-reference varibale 
# print(obj.age)
# obj.display()


#=============================================================

# class Student:
#     def __init__ (self):
#         self.name="prashant"
#         self.age=30

#     def display(self):
#         print("Name=",self.name)
#         print("Age=",self.age)

# StuObj =Student()
# print(StuObj)

#=============================================================

# class Message:
#     def __init__(self):
#         print("I am a contructor")

#     def shows(self):
#         print("class Program")
# obj = Message()
# obj.shows()
# obj2=Message()
# obj2.shows()
#=============================================================

# class StudentInfo:
#     def __init__(self,name,age,roll_no):
#         self.Name=name
#         self.Age=age
#         self.Roll_no=roll_no
    
#     def displayStudentInfo(self):
#         print("Name=",self.Name)
#         print("Age=",self.Age)
#         print("Roll No=",self.Roll_no)

# stuObj=StudentInfo("prashant",34,101)
# stuObj.displayStudentInfo()

#=============================================================

#stack implementation without size limit

# push
# pop
# peek
# isEmpty
# isFull
# Delete
# Display
import sys

class Stack:
    def __init__(self):
        self.mystack=[]

    def push(self,value):
       self.mystack.append(value)
       print("Element pushed")

    def display(self):
       print(self.mystack)

    def isEmpty(self):
        if self.mystack==[]:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.mystack.pop())

    def peek(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.mystack[-1])
        
    def deleteStack():
        self.mystack= None

obj=Stack()
print("stack has created:")

while True:
    print("1.push operation:")
    print("2.Display Stack:")
    print("3.pop operation:")
    print("4.peek operation") #======>return top most element(not remove)
    print("5.Delete operation")
    
    print("7.Exit")
    choice=int(input("Enter your choice:"))
    if choice== 1:
        value=int(input("Enter value to push in stack:"))
        obj.push(value)   
    elif choice==2:
       obj.display()
    elif choice==3:
        obj.pop()
    elif choice==4:
        obj.peek()
    elif choice==5:
        obj.deleteStack()
    else:
        sys.exit()




































































































































