# Reverse Each Word in a String:
# Question: Write a program to reverse each word in a string.
# Logic: Split the string into words, reverse each word, and join them I back together.
# Sample Input: "Hello world"
# Expected Output: "olieH dirow"

# s="Hello world"
# a,b=s.split()
# print(a[::-1],b[::-1])

# Reverse Each Word in a String

# s = "Hello world"
# words = s.split()
# reversed_words = []
# for word in words:
#     reversed_words.append(word[::-1])
# result = " ".join(reversed_words)
# print(result)

#====================================================================================

# 17. Check for Valid Parentheses:
# Question: Write a program to check if a string containing parentheses is valid.
# Logic: Use a stack to keep track of open and close parentheses.
# Sample Input:"({[()]))"
# Expected Output:Valid


# s = "({[()]})"
# stack = []
# pairs = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }
# valid = True
# for char in s:
#     # If opening bracket
#     if char in "({[":
#         stack.append(char)
#     # If closing bracket
#     else:
#         if stack and stack[-1] == pairs[char]:
#             stack.pop()
#         else:
#             valid = False
#             break
# # Stack should be empty for valid parentheses
# if valid and not stack:
#     print("Valid")
# else:
#     print("Invalid")

#====================================================================================
#insertion sort
# arr=[5,3,8,6,2]
# for i in range(1,len(arr)):
#     key=arr[i]
#     j=i-1
#     while j>=0 and key<arr[j]:
#         arr[j+1]=arr[j]
#         j=j-1
#     arr[j+1]=key
# print(arr)
#example-->

#====================================================================================
#bubble sort
# arr = [5,3,8,6,2]
# n = len(arr)
# for i in range(n):
#     for j in range(0,n-i-1):
#         if arr[j]>arr[j+1]:
#             arr[j],arr[j+1]=arr[j+1],arr[j]
#             print(arr)
#     print(arr)
#====================================================================================
#selection sort
# arr=[20,12,10,15,2]
# for i in range(len(arr)):
#     min=i
#     j=i+1
#     while j<len(arr):
#         if arr[j]<arr[min]:
#             min=j
#         j=j+1
#     arr[i],arr[min]=arr[min],arr[i]
# print(arr)

#===================================After Lunch Break=================================================
# 30. Find All Duplicates in a List:
# Question: Write a function to find all the elements that appear more than once in a list.
# Logic: Use a loop and a dictionary to count occurrences.
# Sample Input: [4, 3, 2, 7, 8, 2, 1, 5, 5]
# Expected Output: [2, 5]

# s=[4, 3, 2, 7, 8, 2, 1, 5, 5]


#====================================================================================
# Sort Dictionary by Key or Value:
# Question: Write a function to sort a dictionary by keys or values in ascending or descending order.
# Logic: Use the sorted() function with a custom key or use list comprehension.
# Sample Input: {"C": 3, "B": 2, "A": 1}
# Expected Output (Ascending by Key): ("A": 1, "B": 2, "C": 3)
# Expected Output (Descending by Value): ("C": 3, "B": 2, "A": 1}
# s={"C": 3, "B": 2, "A": 1}


#====================================================================================
# Types of variables

# class New:
#     def __init__(self):
#         self.a=10

# obj1=New()
# obj2=New()
# obj3=New()
# obj1.a=20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
#====================================================================================

# class New:
#     a=10

#     def __init__(self):
#         self.name="Prashant"

# obj1=New()
# obj2=New()
# obj3=New()
# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#====================================================================================
#Que in interview
#  differece between instance and static variable

# class collage:
#     collagename="Modern College" #static Variable
#     def __init__(self):
#         self.studentname="Prashant" #instance Varibale

# principal = collage() #object creation
# teacher = collage()
# accountant = collage()
# print("Principal=",principal.collagename,"....",principal.studentname)
# print("teacher=",teacher.collagename,"....",teacher.studentname)
# print("accountant=",accountant.collagename,"....",accountant.studentname)
# collage.collagename="HBD" #Seconf way to add static varible
# principal.studentname="Prashant jha"
# print("Principal=",principal.collagename,"|",principal.studentname)
# print("teacher=",teacher.collagename,"|",teacher.studentname)
# print("accountant=",accountant.collagename,"|",accountant.studentname)

#====================================================================================
#====================================linkedList======================================
#====================================================================================

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class Linkedlist:
#     def __init__(self):
#         self.head=None

# Linkedlist = Linkedlist()

# Linkedlist.head = Node(5)
# Second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)

# #connecting nodes
# Linkedlist.head.next=Second
# Second.next=third
# third.next=fourth

# #display a linkedlist
# while Linkedlist.head !=None:
#     print(Linkedlist.head.data,"|",Linkedlist.head.next,"->" ,end=" ")
#     Linkedlist.head=Linkedlist.head.next

#====================================================================================
# import sys
# class Node:
#     def __init__(self,data):
#         self.data=data #instance Varibale(5)
#         self.next=None

# class Linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def addNode(self,value):
#         self.node=Node(value)
#         if self.head is None:
#             self.head=self.node
#             self.tail=self.node
#         else:
#             self.tail.next=self.node
#             self.tail=self.node
        
#     def displayNode(self):
#         while self.head is not None:
#             print(self.head.data,'|','->',end=' ')
#             self.head=self.head.next

#     def addnodeBeginning(self,value):
#         print("Added node beginning")
#         self.node=Node(value)
#         if self.head is None:
#             self.head=self.node
#             self.tail=self.node
#         else:
#             self.node.next = self.head
#             self.head=self.node

#     # Insert node in between
#     def addInBetween(self, prev_value, value):
#         temp = self.head
#         # Search node
#         while temp is not None and temp.data != prev_value:
#             temp = temp.next
#         if temp is None:
#             print("Previous node not found")
#             return
#         new_node = Node(value)
#         # insertion logic
#         new_node.next = temp.next
#         temp.next = new_node
#         # if inserted at last update tail
#         if new_node.next is None:
#             self.tail = new_node

#     def addAtEnd(self, value):
#         new_node = Node(value)
#     # if linked list is empty
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
        
# if __name__=='__main__':
#     object=Linkedlist()
#     while True:
#         print('1.Add Node Linkdlist:')
#         print('2.Add Node at beginng:')
#         print('3.Add Node in between:')
#         print('4.Add Node in end:')
#         print('5.display Linkedlist :')
#         print('6.Exit:')
#         ch=int(input("Enter your choice:"))
#         if ch==1:
#             value=int(input("Enter value for node:"))
#             object.addNode(value)
#             print("Node added successfully in single linkedlist:")
#         elif ch==2:
#             value=int(input("Enter value for node:"))
#             object.addnodeBeginning(value)
#             print("Node added at beginning successfully in single linkedlist:")
#         elif ch==3:
#             prev=int(input("Enter previous node value:"))
#             value=int(input("Enter new node value: "))
#             object.addInBetween(prev,value)
#             print("Node added between successfully in single linkedlist:")
#         elif ch==4:
#             value=int(input("Enter the value of node to add at end:"))
#             object.addAtEnd(value)
#             print("Node added at end successfully in single linkedlist:")
#         elif ch==5:
#             object.displayNode()
#         elif ch==6:
#             sys.exit()

