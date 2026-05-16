# name ="prashsnatjha"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[15])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

#====================================================================

# s="Python are High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

#=====================================================================

# name="prashnat"
# sal =5000
# age=28
# print("{} sal is {} age  is {} ".format(name,sal,age))
# print("{0} sal is {1} age  is {2} ".format(name,sal,age))
# print("{x} sal is {y} age  is {z} ".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")

#=====================================================================

# name="prashant"
# for i in name:
#     print(i)

#i/p=prashnat
#o/p=prashnt
# name="prashant"
# newname=" "
# for i in name:
#     if i not in newname:
#         newname += i
# print(newname)

#=====================================================================

# name="prashant"
# newname=""
# for i in name:
#     newname=i+newname
# print(newname)

# another way

# name="prashant"
# newname=""
# N=len(name)
# for i in range(N-1,-1,-1):
#     newname +=name[i]
# print(newname)      
#=====================================================================

#palindrome:
 
# name="racecar"
# newname=" "
# N=len(name)
# for i in range(N-1,-1,-1):
#     newname+=name[i]
# print(newname)
# if newname==name:
#     print("palindrome")
# else:
#     print("not palindrome")

# another way================

# name="help4code"
# print(name)
# print(name[::-1])
# if name == name:
#     print("palindrome")
# else:
#     print("not palindrome")

#=======================================================================

#anagram
# i/p="listen","silent"
# output=anagram


#=======================================================================

# vowels=['a','e','i','o','u']
# name="hello"
# cons =0
# vows=0
# for i in name:
#     if i in vowels:
#         vows+=1
#     else:
#         cons+=1
# print(cons)
# print(vows)

#=======================================================================

#count a word in string
# i/p=this is a sentence
# o/p=4

# sen="this is a sentence"
# word=0
# space=0
# for i in sen:
#     word=word+i
#     continue
# else:
#     space+=1

#=======================================================================

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

#=======================================================================
# i/p=gasgg54@#vscsd!s*
# i/p=4
# incuding whitespace and special character

# sample="0gasgg54@#vscsd!s*"
# count=0
# for i in sample:
#     if i.isalnum():
#         continue
#     elif i==" ":
#         count=count+1
#     else:
#         count=count+1
# print(count)

# another way

# var="0gasgg54@#vscsd!s*"
# count=0

# z=ord(i)
# print(z)

# if z>=97 and z<=122:
#     continue
# elif z>=48 and z<=57:
#     continue


#=======================================================================
# sample="this is test"
# print(sample.title())

#=======================================================================

# print('prashnatjha777'.isalnum())
# print('prashnatjha'.isalpha())
# print('777f'.isdigit())
# print('sssddssdss'.islower())
# print(''.islower())
# print('PRASHANTj'.isupper())
# print('My Name Is Prashant'.istitle())
# print(''.istitle())
# print(' '.isspace())
# print('Hello'.startswith("He"))
# print('Hello'.endswith("lo"))


# print("Prashant".find("r"))
# print("Prashant".index("z"))
# print("Prashant jha".count("a"))

#=======================================================================
#   1  2  3 
# 1   
# 2
# 3

#i= ,j=  (i,j=)
# for i in range(1,4):#==>row
#     for j in range(1,4):#==>col
#         print(i,end=" ")
#     print()

# output===>  1   1   1
#             2   2   2               
#             3   3   3

#=======================================================================

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

#=======================================================================

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()

#=======================================================================

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

#=======================================================================
# import time
# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     print(" "*(n-i),end=" ")
#     for j in range(1,i+1):
#         time.sleep(2)
#         print("*",end=" ")
#     print()

#=======================================================================
#  given an array return an array where each element is the product of all elements in the array except itself
# use two passes,one from left to right,one from right to left to calculate products.
# input=[1,2,3,4]
# output=[24,12,8,6]


# sample=[1,2,3,4]
# for i in sample:
#     sample[i]*sample[i+1]
#    incomplet

#==================Lunch Break=========================








#find the maximum number of consecutive 1s in a binary array
# input:[1,1,0,1,1,1,0,1,1,1,1]
# output:4
# count=0
# max_count=0
# sample=[1,1,0,1,1,1,0,1,1,1,1,]
# for i in sample:
#     if i==1:
#         count=count+1
#         if count>max_count:
#             max_count=count 
#     else:
#         count=0
# print(count)

#=================================================================

# write a program to count the number ofocurenence of substring in a given string
# input:abababab and ab
# output:4

sample=["abababab"]
count=0
for i in sample:
    if sample=="ab":
        count=count+1
print(count)

#=================================================================

