# Find the First Non-Repeating Character:
# Question: Write a function to find the first non-repeating character in a string.
# Logic: Define a function that uses loops to count characters and find the first non-repeating character.
# Sample Input: "leetcode"
# Expected Output: "I"

# def first_non_repeating(s):
#     for ch in s:
#         if s.count(ch) == 1:
#             print(ch)
#             return ch
#     return None
# # Sample Input
# text = "leetcode"
# # Function Call
# result = first_non_repeating(text)
# print("First non-repeating character:", result)

#================================================================================================
# =====================================recursion=================================================
#================================================================================================
# when main pronlem is diveded into similar sub problem
# like in a tree we have to perform same problem 
# Recursion use the tack memory
#------------------------------------------------------------------------------------------------
#interview question
# comparison between recusion and iteration for time and space complexity and easy code
#================================================================================================
#Factorial Solution
# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(4))

#================================================================================================
# def capitalizeFirst(arr):
#     Result=[]
#     if len(arr)==0:
#         return Result
    
#     Result.append(arr[0][0].upper()+arr[0][1:])
#     return Result+capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car','taco','banana']))
#================================================================================================
# def power(base,exponent):
#     if exponent == 0:
#         return 1
#     return base*power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))
#================================================================================================
#product of array using recusion

# def productOfArray(arr):#3[1,2,3]
#     if len(arr)==0:
#         return 1
#     return arr[0]*productOfArray(arr[1:])

# print(productOfArray([1,2,3]))# 1*2*3*1=6
# print(productOfArray([1,2,3,10]))# 1*2*3*10*1=60


#================================================================================================
# reversing string using Recursion
# def reverse(strng):
#     if len(strng)<=1:#python
#         return strng
#     return strng[len(strng)-1] + reverse(strng[0:len(strng)-1])
#                 # n+o+h+t+y+p
# print(reverse('python'))
# print(reverse('appmillers'))
#================================================================================================

# recursiveRange Solution
# def recursiveRange(num):
#     if num<=0:
#         return 0
#     return num + recursiveRange(num-1)

# print(recursiveRange(6))
# 6+5+4+3+2+1

#================================================================================================
# def palindrome(strng):
#     if len(strng)==0:
#         return True
#     if strng[0]!=strng[len(strng)-1]:
#         return False
#     return palindrome(strng[1:-1])

# print(palindrome('awesome'))
# print(palindrome('foobar'))
# print(palindrome('tacocat'))
# print(palindrome('amanaplanacanalpanama'))
#================================================================================================
# someRecursive Solution
# def someRecursive(arr,cb):
#     if len(arr)==0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:],cb)
#     return True
 
# def isOdd(num):
#     if num%2==0:
#         return False
#     else:
#         return True
    
# print(someRecursive([1,2,3,4],isOdd))
# print(someRecursive([4,6,8,9],isOdd))
# print(someRecursive([4,6,8],isOdd))
#=============================================After Lunch break===================================================

# A game company has designed an online lottery game, Bingo. In this game, N number cards are displayed. 
# Each card has a value on it. The value can be negative or positive. The player must
# choose two cards. To win the game, the product of the values of the two cards must be the maximum value
# possible for any pair of cards in the display. The winning amount will be the sum of the two cords chosen by the player.
# Write an algorithm to find the winning amount as the sum of the values of the two cards whose product value is maximum
# Input:
# The first line of the input consists of an integer num Cards, representing the number of cards (N) The second fine consists 
# of N space-separaled integers the values on the cards. valt val2 vall representing
# Output:
# Print an integer representing the sum of the values of the two cards wirose product value is maximum

# input:7 9 -3 8 -6 -7 8 10
# output:19
# product of two max value=9*10


# arr = [7, 9, -3, 8, -6, -7, 8, 10]
# first = second = float('-inf')

# for num in arr:
#     if num > first:
#         second = first
#         first = num
#     elif num > second:
#         second = num 
# print(first * second)

#================================================================================================
#================================================Tree============================================
#================================================================================================
# list represntation of tree
# class tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]
    
#     def __str__(self,level=0):
#         ret=" "*level+str(self.data)+"\n"
#         for ch in self.child:
#             ret+=ch.__str__(level+1)
#         return ret
        
    
#     def addChild(self,object):
#         self.child.append(object)
#         print("Tree node is added")

# rootNode    =   tree("drinks")
# Hot         =   tree("Hot")
# Cold        =   tree("Cold")
# Tea         =   tree("Tea")
# Coffee      =   tree("Coffee")
# NonAlcholic =   tree("NonAlcholic")
# Alchoholic  =   tree("Alchoholic")

# rootNode.addChild(Hot)
# rootNode.addChild(Cold)
# Hot.addChild(Tea)
# Hot.addChild(Coffee)
# Cold.addChild(NonAlcholic)
# Cold.addChild(Alchoholic)

# print(rootNode)

#================================================================================================

# class tree:
#     def __init__(self,data):
#         self.data=data
#         self.child=[]
    
#     def __str__(self,level=0):
#         ret=" "*level+str(self.data)+"\n"
#         for ch in self.child:
#             ret+=ch.__str__(level+1)
#         return ret
        
    
#     def addChild(self,object):
#         self.child.append(object)
#         print("Tree node is added")

# rootNode    =   tree("N1")
# N2          =   tree("N2")
# N3          =   tree("N3")
# N4          =   tree("N4")
# N5          =   tree("N5")
# N6          =   tree("N6")
# N7          =   tree("N7")
# N8          =   tree("N8")


# rootNode.addChild(N2)
# rootNode.addChild(N3)
# N2.addChild(N4)
# N2.addChild(N5)
# N3.addChild(N6)
# N4.addChild(N7)
# N4.addChild(N8)


# print(rootNode)
#================================================================================================
# Array Rotation:
# Question: Rotate an array to the right by a given number of steps.
# Logic: Use array slicing or create a new array to rearrange elements according to the rotation steps.
# Sample Input: [1, 2, 3, 4, 5]rotated by 2 steps
# Expected Output: '[4, 5, 1, 2, 3]

# arr="1 2 3 4 5"
# a,b=arr.split()
# print(b,a)

# arr = [1, 2, 3, 4, 5]
# k = 2
# result = arr[-k:] + arr[:-k]
# print(result)