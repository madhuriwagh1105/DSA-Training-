# import re
# count=0
# pattern=re.compile("function")
# matcher=pattern.finditer("A function in python is defined by a def statment .the general syntax looks like this:" \
# "def function-name(parameter list):statements,i.e. the function body.the parameter python list consists of none or more parameter.")
# # matcher=pattern.finditer("Lilies carry deep historical and cultural meanings. They are most commonly associated with purity, rebirth, " \
# # "devotion, and love. However, meanings can shift by")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("the number of occurences:",count)

#==============================================================================================================
# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurence:",count)

#==============================================================================================================

# import re
# obj=input("Enter the character")
# objmatch=re.finditer(obj,"a7b @k9z")

# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())

#============================================================================================================== 
#match is used to find the string at the beginning or end
# import re
# a=input("Enter a string to perform match opertation:")
# mtch=re.match(a,"python is very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at beginning level")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("there isno matching at beginning level")
#==============================================================================================================
# fullmatch()
# # if it match full string it return the object it will not return the object
# import re
# a=input("Enter a string to perform match opertation:")
# mtch=re.fullmatch(a,"pythoisvery")
# print(mtch)
# if mtch!=None:
#     print("match found")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("full match not found")

#==============================================================================================================
# import re
# s=input("Enter mail ID:")
# # m=re.fullmatch("\w[a-zA-Z0-9.]*@gmail.com",s)
# # m = re.fullmatch(r"\w[\w.]*@.in", s)
# m = re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._]*@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", s)

# if m!=None:
#     print("Valid Email ID")
# else:
#     print("Invalid email ID")

#==============================================================================================================
# import re
# m=input("Enter number:")
# obj=re.fullmatch("[6-9]\d{9}",m)
# if m!=None:
#     print("Valid number")
# else:
#     print("Invalid number")

#==============================================================================================================
# # search()
# import re
# a=input("Enter a string to perform match opertation:")
# mtch=re.search(a,"python sss dynamic lann")
# print(mtch)
# if mtch!=None:
#     print("match found")
#     print(mtch.start()," ",mtch.end())
# else:
#     print("full match not found")

#==============================================================================================================
# import re
# mtch=re.findall('[a-zA-Z0-9]',"abch3hdh5bk7ZQ$&*")
# print(mtch)
#==============================================================================================================
# import re
# obj=re.sub('[a-zA-Z]','#','2345 ABC habc deFF')
# print(obj)
#==============================================================================================================
#find and replace the character
# import re
# obj=re.subn('[0-7]','@','ab3gd6nkl7')
# print(obj)
# print("the string is=",obj[0])
# print("the number of replacement is=",obj[1])

#==============================================================================================================

# import re

# f1 = open("textfile.txt", "r")
# # f2 = open("output.txt", "w")
# a = input("Enter a string to perform match operation: ")
# for line in f1:
#     mtch = re.search(a, line)   
#     if mtch:
#         print("Match found")
#         print(mtch.start(), " ", mtch.end())         
#     # else:
#     #     print("No match found")

# f1.close()
# # f2.close()

#==============================================================================================================
# import os,sys
# fname=input("Enter the file name:")
# if os.path.isfile(fname):
#     print("file exists:",fname)
#     f=open(fname,"r")
# else:
#     print("FIle does not exist",fname)
#     sys.exit()
# lcount=wcount=ccount=0
# for line in f:
#     lcount=lcount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("The number of lines:",lcount)
# print("The number of words:",wcount)
# print("The number of character:",ccount)

#==============================================================================================================
# adjacency matrix 
# class Graph:
#     def __init__(self,vertices):
#         self.v=vertices

#         self.matrix = [[0 for _ in range(vertices)] 
#                        for _ in range(vertices)]
        
#     def display(self):
#         for row in self.matrix:
#             print(row)

#     def add_edge(self,v,u):
#         self.matrix[u][v]=1
#         self.matrix[v][u]=1

#     def remove_edge(self,u,v):
#         self.matrix[u][v]
#         self.matrix[v][u]
# g=Graph(4)

# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)

# g.remove_edge()
# print("Adjacency matrix:")
# g.display()

#==============================================================================================================

class HashTable:
  def __init__(self, size):
    self.size = size
    self.table = [[] for _ in range(size)]

  def hash_function(self, key):
    return key % self.size

  def insert(self, key):
    index = self.hash_function(key)
    self.table[index].append(key)
  
  def display(self):
    print(self.table)

h = HashTable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()


