#!/usr/bin/env python
# coding: utf-8

# 1. What exactly is []?
# Solu: The square brackets are used to define that it is a List comprehension . likewise we have different brackets for example ()- for set and dictionary. which in return perform different operations based on the collection we have opted to use .

# In[4]:


#2. In a list of values stored in a variable called spam, 
#how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

spam=[2,4,6,8,10]
spam.insert(2,'hello')
spam


# 1.Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.
# Solu: 
#     spam=['a','b','c','d']
# 2. What is the value of spam[int(int('3' * 2) / 11)]?
# solu:
#     d
#     explanation: string'3'*2=33; typecast it to int (33/11)=3;spam[3]=d from the list .
# 3. What is the value of spam[-1]?
# Solu:
#     d
#     -1 in the list starts from the end so it will print the last value that is 'd'
# 4. What is the value of spam[:2]?
# Solu:
#     [:2] means it will take by default as [0:2] so output will be ['a','b']
# 

# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 6. What is the value of bacon.index('cat')?
# solu:
#     bacon.index only gives the index value of the object which comes first in the list: index number= 1
# 7. How does bacon.append(99) change the look of the list value in bacon?
# solu: 
#     It will add the 99 at the end list.
#     [3.14, 'cat', 11, 'cat', True, 99]
# 8. How does bacon.remove('cat') change the look of the list in bacon?
# solu: 
#     It will remove the first occurance of the object in the list. 
#     [3.14, 11, 'cat', True]
#     
#     
#     
#     
# 

# 9. What are the list concatenation and list replication operators?
# solu:
#     LIST CONCATENATION-
#         list concatenation is used to add two lists using "+" arithematic operator. It adds the second list at the end of the first list .
#     for example 
#     L1=[1,2,3]
#     L2=[4,5,6]
#     print(L1+L2)
#     output: [1,2,3,4,5,6]
#     
#     LIST REPLICATION -
#     list replication is similar to multiplying a string value. It uses arithematic (*) to multiply the lists .
#     list replication produces the duplicate values of the same list .
#     for example:
#     L1=[8,5,2]*2
#     print(L1)
#     output: [8,5,2,8,5,2]

# 10. What is difference between the list methods append() and insert()?
# solu: 
# APPEND:
# List method append is used to add a new element into the list ,it by default adds the element at the end of the list.
# for example:
#     l1=[1,2,3]
#     l1.append(4)
#     print(l1)
#     output: [1,2,3,4]
# INSERT:
# List method insert is used to insert a particular object into the list by using the index values.
# for example:
#     l2=['1','2','3','4']
#     l2.insert(3,'5')
#     print(l2)
#     output: ['1','2','3','5','4']
#     
#     

# 11. What are the two methods for removing items from a list?
# solu:
#         list has two methods to remove from a list 
#             1.pop method 
#             2.remove method

# 12. Describe how list values and string values are identical.
# solu:
#         All the values that are stored in list are stored in the type of strings.

# 13. What's the difference between tuples and lists?
# Solu:
# lists and tuples are used to represent group of elements into a single entity or object by using []-for lists and ()- for tuples.
# LIST:
# 1)Each element in list is comma separated.
# 2)It allows duplicate elements in list .
# 3)Every element is represented by a unique value index.
# 4) List accepts both positive and negative indexes .
# 5)It allows heterogeneous data .
# 6)List objects are mutable ..
# 7) We can perform list functions and operations on the list using indexes.
# 
# TUPLES:
# 1)It allows duplicate elements in Tuple.
# 2)Every element is represented by a unique value index.
# 3)Tuple accepts both positive and negative indexes
# 4)It allows heterogeneous data .
# 5) Tuples objects are immutable objects .
# 6) we can perfom only retrieval operations on the Tuple .
# 7) Tuple is a collection which is ordered and unchangeable .
# 

# 14. How do you type a tuple value that only contains the integer 42?
# Solu:
# Since tuples are immutable if we add only one value to it we can't append new elements into it .
# 
# By default the python takes the element in '' as string . But, inorder to differentiate a tuple from a string we need to add a comma symbol simultaneously after declaring the the element in the tuple .
# for example,
# t = [('abc'), ('def'), ('ghi', 'jkl')]
#  type( ('abc') )
# <type 'str'>
# t = [('abc',), ('def',), ('ghi', 'jkl')]
#  type( ('abc',) )
# <type 'tuple'>
# 

# 15. How do you get a list value's tuple form? How do you get a tuple value's list form?
# solu:
# 
# There are multiple way like defining a function and calling the list into the function by adding a (,)comma the end of each element in the list or else by type casting it can be done effortlessly.
# for example,
# l1=['a','b','c','d']
# t1=tuple(l1)
# print(t1)
# 
# l2=list(t1)
# print(l2)

# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
# Solu:
# Since the list elements are strings variables that contain list values are not necessarily lists themselves but they can be of string form .
# for example,
# l1=['a','b','c','d']
# for i in l1:
#     print(type(i))

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?
# Solu:
# copy() function in lists only creates the reference object of the list in the memory that means both the newly created variable reference is pointed out to the same list which was previously created.
# But where as in deepcopy() it creates new/both the object of the list as well as the elements of the list in the memory that means there will be two list variables pointing out to their respective list elements .

# In[ ]:




