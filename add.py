#why python is dynamic 
# age=20
# pi=3.14
# name="madhuri"
# result=True
# print(type(age))
# print(type(pi))
# print(type(name))
# print(type(result))


#id is use to retun address
# age=20
# pi=3.14
# name="madhuri"
# result=True
# print(id(age))
# print(id(pi))
# print(id(name))
# print(id(result))

#why all fundamentals datatypes are immutable(non changeble)
# math=50
# chem=50
# print(id(math))
# print(id(chem))


# print(2+2)
# print("2"+"2")
# a=int(input("Enter a :"))#str="2"
# b=int(input("enter b:"))#str="2"
# print(a+b)
# Output=22
# here we need type casting

# int()used to convert in interger 3.14=int=3
# print(int(3.14))
# print(int(10+5j))
# print(int(True))#1
# print(int(False))#0
# print(int("4.22"))
# print(int("4"))
# print(int("madhuri"))
#we cannot convert complex value into int
#we cannot convert floating value string into int
#can't convert string name into int
#=======================================================


#float() used to convert
# print(float(3))
# print(float(10+2j))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))
# print(float("name"))
#we cannot convert complex value to float
#can't covert string name to float
#=================================================

#complex() used to convert
# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))


#bool() used to convert
# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(""))

#========================================================================================
#simple if
#interpreter checks every condition
# a=int(input("Enter any single digit:"))
# if a>0:
#     print("positive number")
# if a<0:
#     print("negavtive number")
# if a==0:
#     print("zero")

#===================task1======================
# day=input("Enter a day:")
# if day=="sat" or day=="SAT" or day=="sun" or day=="SUN":
#     print("holiday")
# else :
#     print("working day")

#===================task2======================
# per=65
# if per>65:
#     print("grade A")
# elif per<=65 and per>=50:
#     print("grade B")
# else:
#     print("fail")

#===================task3======================
#ord is used to convert the character to asc value
# chr=ord(input("Enter any one character:"))#
# if chr>=65 and chr<=90:
#     print("uppercase")
# elif chr>=97 and chr<=132:
#     print("lowercase")
# elif chr>=48 and chr<=57:
#     print("digit")
# else:
#     print("special character")

#===============================================================
#membership operator 
#in 
#not in

# name="help4code"
# print('z' not in name)

#================================================================
#identity operator(address comparison)
#is
#is not

# math=50
# chem=55
# print(math is not chem)

#=================================================================
#for loop is used when range is given

# for i in range(5):# initial i=0
#     print(i)

# for i  in range(2,11):# initial i=2
#     print(i)

# for i  in range(2,11,2):
#     print(i)

#dec
# for i in range (10,5,-1):
#     print(i)


#===========task============
# for i in range (1,21):
#     print("\n")
#     for j in range (1,11):
#         print(i*j)

# for i in range(1,11):
#     print(i*1," ",i*2," ",i*3," ",i*4," ",i*5)
# print("========================== ")
# for i in range(1,11):
#     print(i*11," ",i*12," ",i*13,i*14," ",i*15)
        
#==========================task==========================    
# write a paper  to accept marks and calculate total,per,check 
# if she/he is passes in all subject so print pass else print fail   
# if per is greater then 65 and gender ="male" so he is eligible for placment else not eligible        

# maths=int(input("Enter maths marks:"))
# sci=int(input("Enter sci marks:"))
# phy=int(input("Enter phy marks:"))
# total=maths+sci+phy
# print(total)
# per=(total*100)/300 #total/3.0
# print(per)

# if maths>40 and sci>40 and phy>40:
#     print("pass")
# else :
#     print("fail")
    
# gender=input("Enter a gender m/f:")
# if per>=65 and gender=="f":
#     print("your eligible")
# else:
#     print("not eligible")

# for i in range(1,5):
#     if i ==3:
#         break
#     print(i)

#=======================task=======================
#tcs nqt
#zip() we can take multiple range function inside zip fun
# output
# 1   5
# 2   4
# 4   2
# 5   1

for i,j in zip(range(1,6),range(5,0,-1)):
    if i ==3 and j==3:
        continue
    print(i," ",j)
#=============================================================
