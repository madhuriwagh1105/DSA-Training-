#stack implementation with size limit
# import sys

# class Stack:
#     def __init__(self,size):
#         self.mystack=[] #creating stack
#         self.stacksize=size  #stack size defined

#     def push(self,value):
#         if self.isFull():
#            print("==========stack is full==============")
#         else:
#             self.mystack.append(value)
#             print("==========Element pushed============")

#     def display(self):
#        print(self.mystack)

#     def isEmpty(self):
#         if self.mystack==[]:
#             return True
#         else:
#             return False
        
#     def pop(self):
#         if self.isEmpty():
#             print("==========Stack is Empty==========")
#         else:
#             print(self.mystack.pop())

#     def peek(self):
#         if self.isEmpty():
#             print("==========stack is empty==========")
#         else:
#             print(self.mystack[-1])
        
#     def deleteStack(self):
#         self.mystack= None

#     def isFull(self):
#         if len(self.mystack)==self.stacksize:
#             return True
#         else:
#             return False
            
# size=int(input("Enter the size of Stack:"))
# obj=Stack(size)
# print("============================================================")
# print("stack has created:")

# while True:
#     print("1.push operation:")
#     print("2.Display Stack:")
#     print("3.pop operation:")
#     print("4.peek operation") #======>return top most element(not remove)
#     print("5.Delete operation")
#     print("7.Exit")
#     print("============================================================")
#     choice=int(input("Enter your choice:"))
#     if choice== 1:
#         value=int(input("Enter value to push in stack:"))
#         obj.push(value)   
#     elif choice==2:
#        obj.display()
#     elif choice==3:
#         obj.pop()
#     elif choice==4:
#         obj.peek()
#     elif choice==5:
#         obj.deleteStack()
#     else:
#         sys.exit()

#============================================================================================
# input=572378233 3
# output=3

mylist=[5,7,2,3,7,8,2,3,3]
newlist={}
for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=1
    while j<len(mylist):
        if key ==mylist[j]:
            count+=1
        j=j+1
    if count>1:
        newdict[key]=count
max=newdict
print(max)


 





















































