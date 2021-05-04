#!/usr/bin/env python
# coding: utf-8

# # Assignment-2

# 1.What are the two values of the Boolean data type? How do you write them?
# Solu:
# values of boolean data types are True and False . 
# They can be written as true  and false. 
# They can also be mentioned as 1-for true and 0-for false

# 2. What are the three different types of Boolean operators?
# Solu:
# AND,OR and NOT(NOR,NAND) are considered as boolean operators 

# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# Solu: AND truth table -
#         true true =true 
#         true false=false
#         false true=false 
#         false false =false 
#      OR truth table -
#         true true =true 
#         true false =true 
#         false true =true 
#         false false =false 
#      NOR truth table -Gives opposite of OR Operator 
#         true true=false 
#         true false =false 
#         false true =false 
#         false false =true  
#     NAND truth table -Gives opposite of AND Operator 
#         true true =false 
#         true false=true 
#         false true = true 
#         false false =true

# 4. What are the values of the following expressions?
# solu:
# (5 > 4) and (3 == 5)------>false
# not (5 > 4)------>false
# (5 > 4) or (3 == 5)------>true
# not ((5 > 4) or (3 == 5))------>false
# (True and True) and (True == False)------>false
# (not False) or (not True)------>true
# 

# 
# 5. What are the six comparison operators?
# solu:
# Less than (<),Greaterthan(>),Equal to (==),Notequal (!=), lessthan or equal to (<=) and Greaterthan or equal to (>=)
# 

# 
# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# solu:
# assignment operator is used to assign the value to the variable.
# Equal to operator is used to check the value is true or false.
# 
# x=10---> assigned 10 to x 
# y=20---> assigned 20 to y 
# z=20---> assigned 20 to z 
# z==y--->Check whether z and y are same which returns whether the condition is true or false .

# 7. Identify the three blocks in this code:
# spam = 0
# if spam == 10:
#     print('eggs')
# if spam > 5:
#     print('bacon')
# else:
#     print('ham')
#     print('spam')
#     print('spam')
# 
# solu:(I have taken the proper indentations in between the if conditions or else it throw a indentation error )
# ham 
# spam 
# spam

# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# solu:
# spam=int(input("enter a number"))
# print("Hello") if spam==1 else print ("Howdy")if spam==2 else print("Greetings!")

# 9.If your programme is stuck in an endless loop, what keys you’ll press?
# Solu:
# Press the interrupt key besides the run button in jupyter notebook,close the tab and restart the jupyter notebook again from the anaconda command line . 
# 
# 

# 
# 10. How can you tell the difference between break and continue?
# Solu:
# Break statement : Terminates the loop statement and transfer the execution to the statement immediately following the loop.
# Continue statement : It causes to skip the particular item which staisfies the condition before continue and immediately retests its condition to move forward as expected.

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
# Solu:
# 
# range(10),range(0,10)and range(0,10,1) all of them produce the same output that is it generates (0-9) when been used with a for loop . The difference between each range function mentioned is they have mentioned the syntax in place with default values . Usually a range function takes range(start,end,step).
# The default value for step is one so even if we don't mention the step it will print the numbers based on default step size of 1. 

# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# Solu:
# For loop:
# 
# for i in range(1,11):
#     print(i)
#     
#     
# While Loop:
# 
# i=1
# while (i<11):
#     print(i)
#     i=i+1

# 	
# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# Solu:
# 
# step 1: import spam 
# step 2: spam.bacon() # calling the function inside the module of spam with Dot(.) after the module name.
# 
