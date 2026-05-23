# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None


# class Linkedlist:
#     def __init__(self):
#         self.head=None

#     def __iter__(self):
#         curNode=self.head
#         while curNode:
#             yield curNode   #return data sequencially
#             curNode=curNode.next

# class stack:
#     def __init__(self):
#         self.linkedlist=Linkedlist()

#     def __str__(self):
#         values=[str(x.value)for x in self.linkedlist]
#         return '\n'.join(values)

#     def push(self,value):
#         node=Node(value)
#         node.next=self.linkedlist.head
#         self.linkedlist.head=node

#     def isEmpty(self):
#         if self.linkedlist.head==None:
#             return True
#         else:
#             return False
    
#     def pop(self):
#         if self.isEmpty():
#             return "There is no Element in the stack"
#         else:
#             nodeValue=self.linkedlist.head.value
#             self.linkedlist.head=self.linkedlist.head.next   
#             return nodeValue     

#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element is stack"
#         else:
#             nodeValue=self.linkedlist.head.value
#             return nodeValue
        
#     def delete(self):
#         self.linkedlist.head=None

# customerStack= stack()     
# customerStack.push(1)
# customerStack.push(2)
# customerStack.push(3)
# print(customerStack)

# print("Display top value")
# print(customerStack.peek())

# print("pop top element")
# print(customerStack.pop())

# print("now check stack again")
# print(customerStack)

#==========================================================================================

# class Node:
#     def ___init__(self,value=None):
#         self.value=value
#         self.next=None

#     def __str__(self):
#         return str(self.value)
    
# class linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None

#     def __iter__(self):
#         curNode=self.head
#         while curNode:
#             yield curNode
#             curNode=curNode.next

# class Queue:
#     def __init__(self):
#         self.linkedlist=linkedlist()

#     def __str__(self):
#         values=[str(x) for x in self.linkedlist]
#         return ' '.join(values)

# def enqueue(self,value):
#     newNode=Node(value)
#     if self.linkedlist.head==None:
#         self.linkedlist.head=newNode
#         self.linkedlist.head=newNode
#     else:
#         self.linkedlist.tail.next=newNode
#         self.linkedlist.tail=newNode

#     def isEmpty(self):
#         if self.linkedlist.head==None:
#             return True
#         else:
#             return False
        
#     def dequeue(self):
#         if self.isEmpty():
#             return "There is not any node in Queue"
#         else:
#             tempNode=self.linkedlist.head
#             if self.linkedlist.head==self.linkedlist.tail:
#                 self.linkedlist.head=None
#                 self.linkedlist.tail=None
#             else:
#                 self.linkedlist.head=self.linkedlist.head.next
#             return tempNode
    
#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element is queue"
#         else:
#             nodeValue=self.linkedlist.head.value
#             return nodeValue
        
#     def delete(self):
#         self.linkedlist.head=None
#         self.linkedlist.tail=None

# customerqueue = Queue()     
# customerqueue.enqueue(1)
# customerqueue.enqueue(2)
# customerqueue.enqueue(3)
# print(customerqueue)

# print("Display 1st  value")
# print(customerqueue.peek())

# print("deleete 1st element")
# print(customerqueue.delete())

# print("now check queue again")
# print(customerqueue)
    
        
#==========================================================================================
#===========================================Graph==========================================
#==========================================================================================

# class Graph:
#     def __init__(self):
#         self.adjacency_list={}

#     def add_vertex(Self,vertex):
#         if vertex not in Self.adjacency_list.keys():
#             Self.adjacency_list[vertex]=[]
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex,":",self.adjacency_list[vertex])

#     def add_edge(self,vertex1,vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].append(vertex2)
#             # self.adjacency_list[vertex2].append(vertex1)

#             return True
#         return False
    
#     def remove_vertex(self,vertex1,vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].remove(vertex2)
#             # self.adjacency_list[vertex2].remove(vertex1)
#             return True
#         return False
    
#     # def remove_edge():


# my_graph=Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")


# my_graph.add_edge("A","B")
# my_graph.add_edge("A","C")
# my_graph.add_edge("A","D")

# my_graph.add_edge("B","A")
# my_graph.add_edge("B","E")

# my_graph.add_edge("C","D")
# my_graph.add_edge("C","A")

# my_graph.add_edge("D","C")
# my_graph.add_edge("D","A")
# my_graph.add_edge("D","E")

# my_graph.add_edge("E","B")
# my_graph.add_edge("E","D")

# my_graph.remove_vertex("A","D")

# my_graph.print_graph()


#==========================================================================================
#=======================================Static_Method======================================
#==========================================================================================

# class Student:
#     #by using class name we can access static method
#     @staticmethod
#     def get_personal_details(firstname,lastname):
#         print("your personal details=",firstname,lastname)
#     @staticmethod
#     def contact_details(mobil_no,roll_no):
#         print("your contact details=",mobil_no,roll_no)

# Student.get_personal_details("prashant","jha")
# Student.contact_details(9970545664,1001)

#==========================================================================================
#=====================================Inheritance==========================================
#==========================================================================================

#single level inheritance
# class college:
#     def college_name(self):
#         def college_name(self):
#             print("Modern College")

# class Student(college):
#     def student_info(Self):
#         print("name: Prashnat jha")
#         print("branch: Mechanical")

# obj=Student()
# obj.college_name()
# obj.student_info()

#==========================================================================================

# multilevel inheritance

# class college:
#     def college_name(self):
#         def college_name(self):
#             print("Modern College")

# class Student(college):
#     def student_info(Self):
#         print("name: Prashnat jha")
#         print("branch: Mechanical")

# class exam(Student):
#     def subject(self):
#         print("subject1: Design Engineering")
#         print("Sbject2: Maths")
#         print("Subject3: C-Language")


# obj=exam()
# obj.college_name()
# obj.student_info()
# obj.subject()

#==========================================================================================

# multiple inheritance
# class subjmarks:
#     maths=int(input("Enter marks fot maths:"))
#     DE=int(input("Enter marks for DE"))
#     C=int(input("Enter marks for C"))
#     English=int(input("Enter marks for English"))

# class PractMarks:
#     cpract=int(input("Enter the marks for language:"))

# class Result(subjmarks,PractMarks):
#     def total(self):
#         if (self.maths >=40 and self.DE>=40 and self.C>=40 and self.English>=40 and self.cpract>=20):
#             print("pass")
#         else:
#             print("Fail")

# obj=Result()
# obj.total()

#==========================================================================================
#python only supports operator overloading
# if child class want to write its own property which is already define in parent class 
# child can use operator overloading
#==========================================================================================
class Loan:
    def Home_loan(self):
        print("Home Loan ROI=8%")
    
    def edu_loan(self):
        print("Edu loan intrest= 9%")

class Sbi:
    def edu_loan(Self):
        print("Eduction loan=10%")
        super().edu_loan()

obj=Sbi()
obj.edu_loan()
#==========================================================================================

# class Rbi:
#     def __init__(self):
#         print("Parent class Constructor")

# class Sbi(Rbi):
#     def __ini__(Self):
#         print("Child class Constructor")

# obj=Sbi()