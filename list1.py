# mylist=["prashant","komal","ankush","ashish",77,"sandip","60.52","prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])


# print(mylist)
# mylist[2]="akshay"
# print(mylist)

# if "madhuri" in mylist:
#     print("yes")
# else:
#     print("no")

#======================append function always add value at end or on top (in stack at top)===============
# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)

# mylist.insert(3,"sanket")
# print(mylist)

# mylist.remove("ankush")
# print(mylist)

# newlist=mylist.copy()
# print(newlist)

#===============================================================================================================

# mylist=[["prashant","jha"],['85.60'],[440022,"yyy"]]
# print(mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list2=["madhuri",22,'hello']
# del list2
# del list2[2]
# print(list2)


# list2=["madhuri",22,'hello']
# list2.clear()
# print(list2)

# name="madhuri"
# print(name)
# myname=list(name)
# print(myname)

# mylist=[44,5,90,2,66,61]
# mylist.sort()
# print(mylist)

#======alising==================
# ==============alising one variable reference to another variable===========================
# mylist=[44,55,33,22,11]
# newlist=mylist
# print(id(mylist))
# print(id(newlist))

# mylist=[11,20,55,0,99,200,606]
# for i in mylist:
#     print(i)

# list1=[0,1,4,0,2,5]
# o=[1,4,2,5,0,0]

# for i in list1:
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)


#=========second largest elements====================
# mylist=[7,3,9,2,8]
# mylist.sort()
# print(mylist)
# print(mylist[-2])

# =======MCQ1===========
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)

#output=error
# because  1=10,3=20,5=30,7=40,9=50 ,60==?

#========MCQ2============
# a=[1,2,3,4,5]
# print(a[3:0:-1])
# output=[4,3,2]
# because N-1

#=========MCQ3=========
# arr=[[1,2,3,4],
#      [4,5,6,7],
#      [8,9,10,11],
#      [12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

#output=4,7,11,15
# because it pops the last elements

#=========MCQ4=========
# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]

# for i in range(0,6):
#     print(arr[i],end=" ")

#========MCQ5=============(H.W)
# fruit_list1=['apple','berry','cherry','papaya']
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]='guava'
# fruit_list3[1]='kiwi'

# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0]=='guava':
#         sum +=1
#     if ls[1]=='kiwi':
#         sum+=20
# print(sum)

#===========MCQ6==============
#common elements from 3 list
# list1=[1,2,3]
# list2=[2,3,4]
# list3=[3,4,5]

# for i in list1:
#     if i in list2 and i in list3:
#         print(i)

#===========MCQ7==============
#abs is used to convert neg to pos
# mylist=[]
# n=int(input("Enter the value of n:"))#5
# for i in range(n):
#     val=int(input("Enter the value:"))
#     mylist.append(val)
# print(len(mylist))

# sum=0
# for i in range(len(mylist)-1):
#     if i in range(len(mylist)):
#         sum+=abs(mylist[i]-mylist[i+1])
# print(sum)

#=====================

