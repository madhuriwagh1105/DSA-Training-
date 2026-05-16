#while loop
# i=1
# while i<=5:
#     print(i)
#     i+=1

#====================================function==================================
# self contained block which can be excuted as much as it called
# def hello():
#     print("hello world")
# hello() #calling function

#=========================================================================
#yes,it is possible to return multiple value at once 
# def arithmatic():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     sum=a+b
#     diff=a-b
#     div=a/b
#     mul=a*b
#     return sum,diff,mul,div
# result=arithmatic()
# print("arithmatic=",result)

#=========================================================================
#how many types of arguments we can pass in function?
# 1.positional arguments
# 2.keyword arguments
# 3.default arguments
# 4.variable length argument/variable number of arguments


#=========================================================================
# 1.positional arguments
# def arithmatic(a,b):
#     sum=a+b
#     diff=a-b
#     div=a/b
#     mul=a*b
#     return sum,diff,mul,div
# result=arithmatic(5,5) #===>positional arguments
# print("arithmatic=",result)

#=========================================================================
# 2.keyword arguments
#keyword name and parameter must be same 
# def credential(username,password):#===>parameter
#     if username==password:
#         print("login siccessfully")
#     else:
#         print("invalid credentials")
# credential(username="admin",password="admin")#====>keyword


#=========================================================================
# 3.default arguments
# def cityName(city="pune"):#==>default 
#     print(city)
# cityName("ngp")
# cityName("Mumbai")
# cityName()

#=========================================================================
# 4.variable length argument/variable number of arguments

# def cityName(*name):#========> * is used to select all argument to print
#     print(name)

# cityName("ngp","delhi","mumbai","pune")

#=========================================================================
# modularity approach in function
# import sys

# def add():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a+b)

# def sub():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a-b)

# def div():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)

# def mul():
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a*b)

# while True:
#     print("1.addition")
#     print("2.subtraction")
#     print("3.division")
#     print("4.multiplication")
#     print("exit")
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         add()
#     elif choice==2:
#         sub()
#     elif choice==3:
#         div()
#     elif choice==4:
#         mul()
#     elif choice==5:
#         sys.exit()
#=========================================================================


#===========================DSA Time complexity============================
#find biggest number

# def findBiggestNumber(sampleArray):
#   biggestNumber = sampleArray[0]#=========>o(1)
#   for index in range(1, len(sampleArray)):#=========>o(N)
#     if sampleArray[index] > biggestNumber:#=========>o(1)
#       biggestNumber = sampleArray[index]#=========>o(1)
#   return biggestNumber#=========>o(1)

# sampleArray = [5, 7, 9, 2, 3, 4]
# findBiggestNumber(sampleArray)

# O(1) +O(1) +O(1) +O(1) +O(N)=O(N)
#==============================================================

#linear search

# def linearSearch(array,target):
#   for i in range(0,len(array)): #i=1  #===========>O(N)
#     if array[i]==target:#1==7   #===========>O(1)
#       return i  #===========>O(1)
#   return-1    #===========>O(1)
# array=[1,2,3,4,7,8,9]
# target=9
# result=linearSearch(array,target)
# if result==-1:
#   print("target not found!")
# else:
#   print("Element fount at index number",result)

# rstrip()====>to remove space from right hand side
# lstrip()======>to remove space from left hand side
# strip() ========>remove space from both side

# city=input("Enter your city name:")
# scity=city.strip()
# if scity=='Hydrabad':
#     print("Hello Hydrabadi..Adab")
# elif scity=='chennai':
#     print("Hello Madarsi...Vannakam")
# elif scity=='Bangalore':
#     print("Hello Kannadiga...Shubhudaya")
# else:
#     print("your entired city is invalid")

#=================================================================
# mylist=[ [100,198,333,323],
#   [122,232,221,111],
#   [223,656,245,764]
# ]

# newlist=[]
# for i in range(3):
#   j=0
#   max=mylist[i][j]
#   for j in range(4):
#       c_max=mylist[i][j]
#       if max<c_max:
#         max=c_max
#   newlist.append(max)
# print(newlist)

#==================================TCS===============================
# input=prashant*is*good*programmer
# output=****prashantisgoodprogrammer
    
# # Input string
# s = "prashant*is*good*programmer"
# # Count number of *
# count = s.count('*')
# # Remove all *
# new_string = s.replace('*', '')
# # Add * at the beginning
# output = '*' * count + new_string
# print(output)


# name='prashant*is*a*good*programmer'
# newname=''
# val=''
# for i in name:
#     if i!='*':
#         newname+=i
#     else:
#         val+=i
# # print(newname)
# print(str(val+newname))

#================================= tcs===========================================
# input=aaabbbbccceeeee
# Output=a3b4c3e5

# Input string
# s = "aaabbbbccceeeee"
# # Dictionary to store character counts
# freq = {}
# # Count frequency of each character
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# # Create output string
# output = ""
# for key, value in freq.items():
#     output += key + str(value)
# print(output)

#15/05/2026
# ------------------TCS(asked 4 times)-------------------
name='aaabbbbccceeeee'
newname={}
for i in range(len(name)):
    key=name[i]
    count=0
    for j in range(len(name)):
        if key ==name[j]:
            count+=1
    newname[key]=count
for i,j in newname.items():
    print(i,j,sep='',end='')

#===========================================================