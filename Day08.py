# 22. Remove Leading Zeros from a List of Integers:
# Question: Write a function to remove leading zeros from a list of integers.
# Logic: Use list slicing or a loop to remove zeros until a non-zero element is encountered
# Sample Input: [0, 0, 1, 2, 0, 3, 0, 0, 4]
# Output:[1,2,0,3,0,0,4]

# arr = [0,0,1,2,0,3,0,0,4]
# i = 0
# # Skip leading zeros
# while i < len(arr) and arr[i] == 0:
#     i += 1
# # Slice from first non-zero element
# result = arr[i:]
# print(result)

#===========================================================================================
# 24. Find the First Missing Positive Integer:
# Question: Write a function to find the first missing positive integer in a list of unsorted integers.
# Logic: Use a loop and reposition elements to place each positive integer at its respective index.
# Sample Input: [3, 4, -1, 1]
# Expected Output: 2
# arr=[3,4,-1,1]
# arr.sort()
# for i in arr(1,len(arr)):
# print(arr)


#===========================================================================================
# 25. Find the Smallest Missing Positive Integer:
# Question: Write a function to find the smallest missing positive integer in a list of unsorted integers. I
# Logic: Use a loop and reposition elements to place each positive integer at its respective Index.
# Sample Input: [7, 8, 9, 11, 12]
# Expected Output: 1

#===========================================================================================
#=========================================Tree==============================================
#===========================================================================================
#may ask u to draw a tree in interview
# MCQ asked on this topic
# identify which Type of tree 

# 1.full binary tree
    # each node has either 0 or 2
    # no node has a single child

# 2.complete binary tree
    #all level except possibly the last are completely filled
    #nodes in the last level are filled from left to right

# 3.perfectc binary tree
    #all internal nodes have exactly two nodes
    #all leaf nodes are at the same level

# 4.
    #
    #
#===========================================================================================
# part of Depth first search---->

# PreOrder=RootNode->Left Node->Right Nodes
#Inorder=Left Node-> RootNode->Right Nodes
#postOrder=Left Node->Right Nodes-> RootNode

# we have to check time complexity in each level
#===========================================================================================

# class BSTNode:
#   def __init__(self, data):
#     self.data = data
#     self.leftChild = None
#     self.rightChild = None

# def insertNode(rootNode, nodeValue):
#   if rootNode.data == None:
#     rootNode.data = nodeValue
#   elif nodeValue <= rootNode.data:
#     if rootNode.leftChild is None:
#       rootNode.leftChild = BSTNode(nodeValue)
#     else:
#       insertNode(rootNode.leftChild, nodeValue)
#   else:
#     if rootNode.rightChild is None:
#       rootNode.rightChild = BSTNode(nodeValue)
#     else:
#       insertNode(rootNode.rightChild, nodeValue)

# #preorder - 70, 50, 30, 20, 10, 40, 60, 90, 80, 100
# #inorder - 10, 20, 30, 40, 50, 60, 70, 80, 90, 100
# #postorder - 10, 20, 40, 30, 60, 50, 80, 100, 90, 70

# def preOrderTraversal(rootNode):
#   if not rootNode:
#     return
#   print(rootNode.data, end=" ")
#   preOrderTraversal(rootNode.leftChild)
#   preOrderTraversal(rootNode.rightChild)

# def inOrderTraversal(rootNode):
#   if not rootNode:
#     return
#   inOrderTraversal(rootNode.leftChild)
#   print(rootNode.data, end=" ")
#   inOrderTraversal(rootNode.rightChild)

# def postOrderTraversal(rootnode):
#   if not rootnode:
#     return
#   postOrderTraversal(rootnode.leftChild)
#   postOrderTraversal(rootnode.rightChild)
#   print(rootnode.data, end=" ")

# def searchNode(rootNode, nodeValue):
#   if rootNode.data == nodeValue:
#     print("The value is found")
#   elif nodeValue < rootNode.data:
#     if rootNode.leftChild.data == None:
#       print("The value is not found")
#     elif rootNode.leftChild.data == nodeValue:
#       print("The value is found")
#     else:
#       searchNode(rootNode.leftChild, nodeValue)
#   else:
#     if rootNode.rightChild.data == None:
#       print("The value is not found")
#     elif rootNode.rightChild.data == nodeValue:
#       print("The value is found")
#     else:
#       searchNode(rootNode.rightChild, nodeValue)

# newBST = BSTNode(None)
# insertNode(newBST, 70)
# insertNode(newBST, 50)
# insertNode(newBST, 90)
# insertNode(newBST, 30)
# insertNode(newBST, 60)
# insertNode(newBST, 80)
# insertNode(newBST, 100)
# insertNode(newBST, 20)
# insertNode(newBST, 40)
# insertNode(newBST, 10)
# print("Pre Order Traversal : ")
# preOrderTraversal(newBST)
# print("\nIn Order Traversal : ")
# inOrderTraversal(newBST)
# print("\nPost Order Traversal : ")
# postOrderTraversal(newBST)
# print("\n")

# searchNode(newBST, 10)
#===========================================================================================

# try:
#     a= int(input("Enter first number :"))
#     b=int(input("Enter second number:"))
#     print(a/b)
# except ZeroDivisionError:
#   print("cant divide by zero")
# except ValueError:
#    print("Enter only integer value:")
# except:
#    print("ABC")
# finally:
#    print("i always execute...")
# else:
#     print("everything is okay")

#--------------------------------------------------------------------------------------------
# try:
#     a= int(input("Enter first number :"))
#     b=int(input("Enter second number:"))
#     print(a/b)
# except(ZeroDivisionError,ValueError) as msg:
#    print(msg)
#===========================================================================================
# import logging
# logging.basicConfig(filename="newfile.txt",level=logging.DEBUG)
# try:
#    a=int(input("Enter first integer no:"))
#    b=int(input("Enter first integer no:"))
#    print(a/b)

# except(ZeroDivisionError,ValueError)as message:
#    print(message)
#    logging.exception(message)
#    print("Logging Level is set up.check 'newfile.txt' for log details")

#===========================================================================================
# =========whenever we want to store data parmenetly we use exception handling===============
#===========================================================================================
# import csv
# f=open("employee.csv",'a')
# a=csv.writer(f)
# # a.writerow(["EmpID","EMP Name","Emp Age"])
# empid=int(input("Enter the empID"))
# empname=input("Enter the name")
# empage=int(input("Enter the age"))
# a.writerow([empid,empname,empage])
# print("file has created")
#===========================================================================================
# student
# input:id,name,phy,maths,chem
# calculate:total,percentage
# check condition of all paper marks >=40 pass else fail

import csv
f=open("studnet.csv",'a')
a=csv.writer(f)
a.writerow(["StudentID","Student Name","phy","chem","maths","Total","Percentage","Pass\fail"])
stdid=int(input("Enter the Studnet ID:"))
stdname=input("Enter the name:")
phy=int(input("Enter the phy marks:"))
chem=int(input("Enter the chem marks:"))
maths=int(input("Enter the maths marks:"))
total=phy+chem+maths
percentage=total/0.3
if percentage>=40:
    print("pass")
else:
    print("fail")
a.writerow([stdid,stdname,phy,chem,maths])

print("file has created")